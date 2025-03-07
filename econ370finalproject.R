### NAME: Sarayu Thondapu
### Assignment: FINAL PROJECT


library(tigris)
library(sf)
library(ggplot2)
library(tidycensus)
library(tidyverse)
options(tigris_use_cache=TRUE)
options(scipen = 999)

### RESEARCH QUESTION: Are NYC kiosks' locations accessible? Does there exist a correlation between NYC Kiosk Locations, the population of that area, and the number of crashes that occur? 

# DATA LOADED: 
LinkNYC_Kiosk_Locations <- read.csv("~/Desktop/ECON 370/hw3/raw_data/LinkNYC_Kiosk_Locations.csv")
Motor_Vehicle_Collisions_Crashes <- read.csv("~/Desktop/ECON 370/hw3/raw_data/Motor_Vehicle_Collisions_-_Crashes.csv")
newyork_pop_csv <- read.csv("~/Desktop/ECON 370/newyork_pop - Sheet1 (1).csv")


# CLEANING DATA: 

# COLLISIONS
crash_data = crash_data %>% select("BOROUGH", "ZIP.CODE", "LATITUDE", "LONGITUDE", "LOCATION")
cleaned_crashed_data = crash_data %>% filter(!is.na(BOROUGH) & !is.na(ZIP.CODE) & !is.na(LATITUDE) & !is.na(LONGITUDE))
sample_indexes = sample(nrow(cleaned_crashed_data), size = 10000, replace = FALSE)
sampled_crash_data = cleaned_crashed_data[sample_indexes, ]
colnames(sampled_crash_data)[3:4] = c("Latitude", "Longitude")

# POPULATION
cleaned_pop_data = pop_zipcode_data[pop_zipcode_data$most_current_pop_year == "2022",]
cleaned_pop_data = cleaned_pop_data[cleaned_pop_data$population != 0,] # omitted zip codes with 0 reported pop. 
colnames(cleaned_pop_data) = c("ZIP.CODE", "Year", "Population")

# KIOSKS
kiosks = kiosk_data[kiosk_data$Installation.Status == "Live",] 
colnames(kiosks)[13] = "ZIP.CODE"
kiosks = kiosks %>% select("Planned.Kiosk.Type", "ZIP.CODE", "Borough", "Latitude", "Longitude")
colnames(kiosks)[1] = "Kiosk.Type"
cleaned_kiosk_data = kiosks %>% filter(!is.na(Kiosk.Type) & !is.na(Borough) & !is.na(ZIP.CODE) & !is.na(Latitude) & !is.na(Longitude))


# MERGING TABLES, ZIP CODES, AND CREATING PLOT OF NEW YORK CITY WITH KIOSK LOCATIONS

ny_zips <- zctas(state = "NY", class = "sf", year = 2010) # zips only available in 2010
head(ny_zips)
urb <- urban_areas(year=2022) |> filter(grepl("New York",NAME10)) 
ny_urb_zips <- st_join(ny_zips,urb) |> filter(!is.na(NAME10))
colnames(ny_urb_zips)[2] = "ZIP.CODE"

options(digits = 5) 
new_vals = as.double(ny_urb_zips$ZIP.CODE) 
ny_urb_zips$ZIP.CODE = new_vals # making it a double, so merging will be easier

k_merged_table = ny_urb_zips |> left_join(kiosks, by = "ZIP.CODE") # merging zips and kiosks on zip code
c_merged_table = ny_urb_zips |> left_join(sampled_crash_data, by = "ZIP.CODE") # merging crashes and zips on zip code, originally for its own graph, but ended up using it for a more accurate rendering of the boroughs


k_merged_table = k_merged_table |> left_join(cleaned_pop_data, by = "ZIP.CODE") # merging new merged tables to add a population col
c_merged_table = c_merged_table |> left_join(cleaned_pop_data, by = "ZIP.CODE") # merging new merged tables to add a population col

sf_kiosks_zips = k_merged_table  # renaming merged to sf for clarity
sf_crashes_zips = c_merged_table # renaming merged to sf for clarity 

# Produces a Table with Zipcodes of NYC
ggplot(sf_kiosks_zips) + 
  geom_sf(aes(geometry=geometry, fill = Population), col="black") + 
  scale_fill_viridis_c() +
  ggtitle("Zipcodes of NYC") # generates a zip code plot of urban area of nyc with population

# CREATE SF for all kiosks 
all_kiosks_sf <- st_as_sf(x = kiosks, 
                          coords = c("Longitude", "Latitude"))
all_kiosks_sf <- st_set_crs(all_kiosks_sf, st_crs(sf_kiosks_zips))

ggplot(sf_kiosks_zips |> filter(ZIP.CODE %in% sf_kiosks_zips$ZIP.CODE)) + 
  geom_sf(aes(geometry=geometry, fill = Population), col = "black") + 
  scale_fill_viridis_c() +
  geom_sf(data=all_kiosks_sf, alpha = 0.3, aes(col= Kiosk.Type)) #plots kiosk locations largely concentrared in the bottom left corner


#### KIOSKS AND CRASHES FOR SPECIFIC BOROUGHS (FOR VISUALIZATIONS FOR EACH BOROUGH)
bronx_kiosks = cleaned_kiosk_data[cleaned_kiosk_data$Borough == "Bronx",] 
brooklyn_kiosks = cleaned_kiosk_data[cleaned_kiosk_data$Borough == "Brooklyn",]
statenisls_kiosks = cleaned_kiosk_data[cleaned_kiosk_data$Borough == "Staten Island",]
queens_kiosks = cleaned_kiosk_data[cleaned_kiosk_data$Borough == "Queens",]
manhattan_kiosks = cleaned_kiosk_data[cleaned_kiosk_data$Borough == "Manhattan",]


bronx_crashes = sampled_crash_data[sampled_crash_data$BOROUGH == "BRONX",]
brooklyn_crashes = sampled_crash_data[sampled_crash_data$BOROUGH == "BROOKLYN",]
si_crashes = sampled_crash_data[sampled_crash_data$BOROUGH == "STATEN ISLAND",]
queens_crashes = sampled_crash_data[sampled_crash_data$BOROUGH == "QUEENS",]
manhattan_crashes = sampled_crash_data[sampled_crash_data$BOROUGH == "MANHATTAN",]

## CREATE VISUALIZATIONS FOR CRASHES AND KIOSKS: 


# CRASH and KIOSK BAR CHART (used LLM for assistance in grouping)
number_of_crashes_by_borough = sampled_crash_data %>% group_by(BOROUGH) %>% tally()
colnames(number_of_crashes_by_borough)[1] = "Borough"
number_of_crashes_by_borough$Borough = c("Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island")
number_of_kiosks_by_borough = cleaned_kiosk_data %>% group_by(Borough) %>% tally()
new_table = number_of_kiosks_by_borough %>% left_join(number_of_crashes_by_borough, by = "Borough")
colnames(new_table)[2:3] = c("Kiosks", "Collisions")

long_data = new_table %>% gather(key = "Type", value = "Count", Kiosks, Collisions)

ggplot(long_data, aes(x = Borough, y = Count, fill = Type)) +
  geom_bar(stat = "identity", position = "dodge") +
  xlab("Boroughs") +
  ylab("Sum") + theme(panel.background = element_blank()) + 
  ggtitle("Number of Crashes and Kiosks by Borough") +
  theme(plot.title = element_text(hjust = 0.5))


# BRONX SF FOR KIOSKS:
bronx_sf <- st_as_sf(x=bronx_kiosks,
                          coords=c("Longitude","Latitude"))
bronx_sf <- st_set_crs(bronx_sf, st_crs(ny_urb_zips))

bronx_sf <- st_as_sf(x=bronx_kiosks,
                     coords=c("Longitude","Latitude"))
bronx_sf <- st_set_crs(bronx_sf, st_crs(ny_urb_zips))

bronx_merged <- st_join(bronx_sf, all_kiosks_sf)

bronx_c_sf <- st_as_sf(x=bronx_crashes,
                       coords=c("Longitude","Latitude"))
bronx_c_sf <- st_set_crs(bronx_c_sf, st_crs(ny_urb_zips))

ggplot(sf_kiosks_zips) + 
  geom_sf(aes(geometry=geometry, fill = Population), col="black") + 
  ggtitle("Zipcodes of NYC")

ggplot(sf_kiosks_zips |> filter(ZIP.CODE %in% bronx_c_sf$ZIP.CODE)) + 
  geom_sf(aes(geometry=geometry, fill = Population), col = "black") + 
  scale_fill_viridis_c() +
  geom_sf(data=bronx_sf, alpha = 0.5, col = "black") + 
  ggtitle("Kiosk Locations in Bronx") +
  theme(plot.title = element_text(hjust = 0.5))


# MANHATTAN KIOSK MAPPING
manhattan_sf <- st_as_sf(x=manhattan_kiosks,
                     coords=c("Longitude","Latitude"))
manhattan_sf <- st_set_crs(manhattan_sf, st_crs(ny_urb_zips))

manhattan_merged <- st_join(manhattan_sf, all_kiosks_sf)

manhattan_c_sf <- st_as_sf(x=manhattan_crashes,
                       coords=c("Longitude","Latitude"))
manhattan_c_sf <- st_set_crs(manhattan_c_sf, st_crs(ny_urb_zips))

ggplot(sf_kiosks_zips |> filter(ZIP.CODE %in% manhattan_c_sf$ZIP.CODE)) + 
  geom_sf(aes(geometry=geometry, fill = Population), col = "black") + 
  scale_fill_viridis_c() +
  geom_sf(data=manhattan_sf, alpha = 0.1, col = "black") + ggtitle("Kiosk Locations in Manhattan") +
  theme(plot.title = element_text(hjust = 0.5))

# BROOKLYN KIOSK MAPPING

brooklyn_sf <- st_as_sf(x=brooklyn_kiosks,
                         coords=c("Longitude","Latitude"))
brooklyn_sf <- st_set_crs(brooklyn_sf, st_crs(ny_urb_zips))

brooklyn_merged <- st_join(brooklyn_sf, all_kiosks_sf)

brooklyn_c_sf <- st_as_sf(x=brooklyn_crashes,
                           coords=c("Longitude","Latitude"))
brooklyn_c_sf <- st_set_crs(brooklyn_c_sf, st_crs(ny_urb_zips))

ggplot(sf_kiosks_zips |> filter(ZIP.CODE %in% brooklyn_c_sf$ZIP.CODE)) + 
  geom_sf(aes(geometry=geometry, fill = Population), col = "black") + 
  scale_fill_viridis_c() +
  geom_sf(data=brooklyn_sf, alpha = 0.5, col = "black") + ggtitle("Kiosk Locations in Brooklyn") +
  theme(plot.title = element_text(hjust = 0.5))

# STATEN ISLAND KIOSK MAPPING

si_sf <- st_as_sf(x=statenisls_kiosks,
                        coords=c("Longitude","Latitude"))
si_sf <- st_set_crs(si_sf, st_crs(ny_urb_zips))

si_merged <- st_join(si_sf, all_kiosks_sf)

si_c_sf <- st_as_sf(x=si_crashes,
                          coords=c("Longitude","Latitude"))
si_c_sf <- st_set_crs(si_c_sf, st_crs(ny_urb_zips))

ggplot(sf_kiosks_zips |> filter(ZIP.CODE %in% si_c_sf$ZIP.CODE)) + 
  geom_sf(aes(geometry=geometry, fill = Population), col = "black") + 
  scale_fill_viridis_c() +
  geom_sf(data=si_sf, alpha = 0.5, col = "black") + ggtitle("Kiosk Locations in Staten Island")

# QUEEN ISLAND KIOSK MAPPING

queens_sf <- st_as_sf(x=queens_kiosks,
                        coords=c("Longitude","Latitude"))
queens_sf <- st_set_crs(queens_sf, st_crs(ny_urb_zips))

queens_merged <- st_join(queens_sf, all_kiosks_sf)

queens_c_sf <- st_as_sf(x=queens_crashes,
                    coords=c("Longitude","Latitude"))
queens_c_sf <- st_set_crs(queens_c_sf, st_crs(ny_urb_zips))

ggplot(sf_kiosks_zips |> filter(ZIP.CODE %in% queens_c_sf$ZIP.CODE)) + 
  geom_sf(aes(geometry=geometry, fill = Population), col = "black") + 
  scale_fill_viridis_c() +
  geom_sf(data=queens_sf, alpha = 0.5, col = "black") + ggtitle("Kiosk Locations in Queens") +
  theme(plot.title = element_text(hjust = 0.5))

### TABLES FOR REGRESSION ANALYSIS + CREATING A DISTANCE VAR:


### USED LLMS FOR GUIDANCE ON FINDING MINIMUM DISTANCE
distance_measure = function(c_location, k_location){
  distances = rep(0, 10000)
  for (i in 1:length(distances)){
    dist_mat = st_distance(c_location[i], k_location)
    
    kiosk_idx = which.min(dist_mat)
    min_dist = dist_mat[kiosk_idx]
    
    distances[i] = min_dist
  }
  return(distances)
}

## HOPING TO GET IT IN A GOOD UNIT, THIS SHOULD RETURN IN METERS

all_crashes_sf <- st_as_sf(x = sampled_crash_data, 
                           coords = c("Longitude", "Latitude"))
all_crashes_sf <- st_set_crs(all_crashes_sf, st_crs(sf_crashes_zips))

all_crashes_sf_projected = st_transform(all_crashes_sf, crs = 32633)
all_kiosks_sf_projected = st_transform(all_kiosks_sf, crs = 32633)

nearest_dist = distance_measure(all_crashes_sf_projected$geometry, all_kiosks_sf_projected$geometry)


# KILOMETERS
sampled_crash_data$min_dist = nearest_dist/1000 # returns distance in kilometers

#RETURNS AVERAGE OF EACH ZIP CODE, FOR REGRESSION ANALYSIS
avg_min_dist_by_zip <- sampled_crash_data %>% 
  group_by(ZIP.CODE) %>% 
  summarize(min_dist_avg = mean(min_dist, na.rm = TRUE))

### PREPPING DATA SO THAT I GET NUMBER OF COLLISIONS AND KIOSKS FOR EACH ZIP CODE
number_of_crashes = sampled_crash_data %>% group_by(ZIP.CODE) %>% tally()
colnames(number_of_crashes) = c("ZIP.CODE", "Collisions")
number_of_kiosks = cleaned_kiosk_data %>% group_by(ZIP.CODE) %>% tally()
colnames(number_of_kiosks) = c("ZIP.CODE", "Kiosks")

# assigns each borough its correct zipcode
boroughs_zip = sampled_crash_data %>% select("BOROUGH", "ZIP.CODE") %>% distinct(ZIP.CODE, .keep_all = TRUE) %>% group_by(ZIP.CODE) 

# merges number of crashes, number of kiosks, and boroughs zips to get a nice regression table to work with
reg_table = cleaned_pop_data |> left_join(number_of_crashes, by = "ZIP.CODE") |> left_join(number_of_kiosks, by = "ZIP.CODE") |> left_join(avg_min_dist_by_zip, by = "ZIP.CODE") |>
  left_join(boroughs_zip, by = "ZIP.CODE")

# clears out NAs
cleaned_reg_frame = reg_table %>% filter(!is.na(Collisions) & !is.na(BOROUGH) & !is.na(Population) & !is.na(min_dist_avg) & !is.na(Kiosks))

# gets rid of really large outliers
cleaned_reg_frame = cleaned_reg_frame[cleaned_reg_frame$min_dist_avg <= 50,]

# converts to a data frame
cleaned_reg_frame = data.frame(cleaned_reg_frame)


### REGRESSIONS
fit1 = lm(min_dist_avg ~ Collisions, cleaned_reg_frame)
summary(fit1)

fit2 = lm(min_dist_avg ~ Collisions + BOROUGH, cleaned_reg_frame)
summary(fit2)

fit3 = lm(min_dist_avg ~ Collisions + BOROUGH + Population, cleaned_reg_frame)
summary(fit3)



