## Question: Who were the most aggressive quarterbacks in 2021?
## This script finds a table of the quarterbacks who have the largest adot
## Code from Chapter 1 of Football Analytics With Python And R (Eager & Erickson)

## Import data libraries
library("tidyverse")
library("nflfastR")

## Load in data
pbp_r <- load_pbp(2021)

# Filter data to only positive passing plays
pbp_r_p <-
  pbp_r |>
  filter(play_type == "pass" & !is.na(air_yards))

# Build adot table
pbp_r_p |>
  group_by(passer_id, passer) |>
  summarize(n = n(), adot = mean(air_yards)) |>
  filter(n >= 100 & !is.na(passer)) |>
  arrange(-adot) |>
  print(n = Inf)



