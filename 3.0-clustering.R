library(tidyverse)
library(scales)
library(factoextra)
library(superheat)
library(NbClust)

set.seed(666)

prepared_data <- read.csv(file.path(getwd(), "data", "processed_data", "processed_data.csv"), row.names = "Team")

input_data <- prepared_data %>%
  select(OutOfBox, NearShots, Counter, PenaltiesTaken, DribblesTotal, LongBallsAttempted, ShortPassesAttempted, CrossesAttempted, WingPlay, TacklesAttempted, FoulsCommitted, Interceptions, TotalClearances, ShotsBlocked, CrossesBlocked, PassesBlocked)

# Assessing clustering tendency

input_data %>%
  scale() %>%
  get_clust_tendency(n = nrow(input_data) - 1)

distance_correlation <- get_dist(input_scaled, method = "pearson")
fviz_dist(distance_correlation) 

# Determining optimal number of clusters

dissimilarity_matrix <- input_data %>%
  scale() %>%
  get_dist("pearson")

nbcluster_pearson_ward <- input_data %>%
  scale() %>% 
  NbClust(diss = dissimilarity_matrix,
          distance = NULL,
          min.nc = 2,
          max.nc = 20,
          method = "ward.D2", 
          index = "all")


# Visualize clusters
 
hclust_model <- input_data %>%
  scale() %>%
  eclust(FUNcluster = "hclust", hc_metric = "pearson", hc_method = "ward.D2", k = 8)

fviz_dend(hclust_model, palette = "jco", rect = TRUE, rect_border = "jco", rect_fill = TRUE)

fviz_silhouette(hclust_model)

########

png("smoothed_clusters.png", height = 1600, width = 1400)

superheat(input_data, 
          scale = TRUE,  
          membership.rows = hclust_model$cluster, 
          pretty.order.rows = TRUE,
          pretty.order.cols = TRUE,
          bottom.label.text.angle = 90, 
          bottom.label.text.size = 8, 
          left.label.text.size = 5,
          heat.pal = c("blue", "white", "red"),
          left.label = 'variable', 
          grid.vline = FALSE,
          membership.cols = 1:ncol(input_data),
          bottom.label = "variable",
          smooth.heat = TRUE)

dev.off()


########




