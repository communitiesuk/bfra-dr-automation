library(DBI)
library(odbc)
library(tidyverse)
library(sf)
library(stringdist)
library(janitor)

## Reading in portfolio list
dr_year <- format(lubridate::as_date(paste("01", dr_date), format = "%d %B %Y"), "%Y")
dr_month <- format(lubridate::as_date(paste("01", dr_date), format = "%d %B %Y"), "%B")
  
folder_portfolio_list <- paste0("D:/Users/", username, "/MHCLG/",
                                "BSP Data and Analysis - Publication of Information/",
                                dr_year, "/", paste(dr_month, dr_year), "/")

file_portfolio_list <- list.files(folder_portfolio_list) %>%
  as_tibble() %>%
  rename(file = value) %>%
  filter(str_detect(file, "Portfolio building list")) %>%
  pull()

portfolio_list <- readxl::read_xlsx(paste0(folder_portfolio_list, file_portfolio_list),
                                   sheet = "Building list") %>%
  janitor::clean_names() %>%
  as_tibble()

## Connecting to SQL Server
sql_server <- "dap-sql01\\cds"     
sql_database <- "MasterData"

con <- dbConnect(odbc::odbc(),
                 Driver = "SQL Server",   # or "ODBC Driver 17 for SQL Server"
                 Server = sql_server,
                 Database = sql_database,
                 #UID = uid, # username
                 #PWD = pwd, # password
                 Port = 1433)  # Default port for SQL Server

sql_schema <- "Reference"
sql_db_onspd <- "vw_ONS_PostCode_Database"

onspd_df <- dbGetQuery(con, paste0("SELECT * FROM ", 
                                sql_schema, ".", sql_db_onspd)) %>%
  as_tibble() %>%
  janitor::clean_names()

dbDisconnect(con)

## Reading in ONS WPC Data (July 2024)
pcon_df <- read.csv("data/Constituencies_Names_and_Codes_UK.csv") %>%
  as_tibble() %>%
  janitor::clean_names()

postcode_string <- paste0("(([A-Z]{1,2})([0-9]{1,2})([A-Z]?))",
                          "\\s", "[0-9][A-Z]{1,2}")

## Matching Portfolio List to ONS Data
portfolio_matched <- portfolio_list %>%
  select(building_name:constituency, category, height) %>%
  mutate(across(postcode,
                .fns = ~ {
                  # if there are multiple postcodes, only taking the first one
                  x <- str_remove_all(., "(,|&|\\/|(and)).*")
                  x <- str_remove_all(x, "\\(\\w*(\\s*\\w*)?\\).*")
                  x <- str_remove_all(x, "\\w*\\s(-|=)\\s")
                  x <- str_extract(x, paste0("^", postcode_string))
                  x <- str_trim(x, side = "both")
                  x
                },
                .names = "{col}_clean")) %>%
  left_join(onspd_df %>%
              select(pcds, pcon), # other: pcd, pcd2
            by = c("postcode_clean" = "pcds")) %>%
  left_join(pcon_df %>%
              select(i_pcon24cd, pcon24nm),
            by = c("pcon" = "i_pcon24cd"))

portfolio_matched <- portfolio_matched %>%
  rename(ons_constituency_code = pcon,
         ons_constituency_name = pcon24nm) %>%
  rename(old_constituency = constituency)

portfolio_matched %>%
  select(-old_constituency) %>%
  openxlsx::write.xlsx("Portfolio_WPC_Matched.xlsx")

## Checking which are missing WPC code or name
## These need to be manually matched
portfolio_matched %>%
  filter(is.na(ons_constituency_code) | is.na(ons_constituency_name)) 
  
## Checking which don't match current WPC name
portfolio_matched %>%
  mutate(dist = stringdist::stringdist(ons_constituency_name, 
                                       old_constituency, 
                                       method = "lv")) %>%
  filter(dist > 1) %>% 
  # filter(ons_constituency_code != old_constituency) %>%
  select(building_name, street, post_code, portfolio_id, 
         ons_constituency_code, ons_constituency_name, 
         old_constituency, dist) %>% 
  openxlsx::write.xlsx(paste0(folder_portfolio_list, "Portfolio list with Constituency.xlsx"))
  
## Reading in ONS WPC Boundaries
wpc_england <- sf::read_sf(paste0("data/WPC_July_2024_Boundaries/",
                                  "PCON_JULY_2024_UK_BUC.shp")) %>%
  janitor::clean_names() %>%
  filter(str_detect(pcon24cd, "^E"))

## Aggregating data from Portfolio List to WPC 
portfolio_constituency <- portfolio_matched %>%
  group_by(ons_constituency_code, ons_constituency_name) %>%
  summarise(count = n())

## Matching WPC Boundaries and Portfolio List
portfolio_map <- wpc_england %>%
  left_join(portfolio_constituency,
            by = c("pcon24cd" = "ons_constituency_code",
                   "pcon24nm" = "ons_constituency_name")) 

## Mapping the data
ggplot(data = portfolio_map) +
  geom_sf(aes(fill = count))+
  scale_fill_continuous(low = "white", high = "#00625E",
                        na.value="white")+
  theme_void() +
  labs(title = "Number of buildings with EWS defects", subtitle = "")

