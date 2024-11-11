# Question: Who were the most aggressive quarterbacks in 2021?
# This script finds a table of the quarterbacks who have the largest adot
# Code from Chapter 1 of Football Analytics With Python And R (Eager & Erickson)

import pandas as pd
import nfl_data_py as nfl

pbp_py = nfl.import_pbp_data([2021])

# Filter out passing data
filter_crit = 'play_type == "pass" & air_yards.notnull()'
pbp_py_p = (
    pbp_py.query(filter_crit)
    .groupby(["passer_id", "passer"])
    .agg({"air_yards": ["count", "mean"]})
)

# Format adot table
pbp_py_p.columns = list(map("_".join, pbp_py_p.columns.values))
sort_crit = "air_yards_count > 100"
print(
    pbp_py_p.query(sort_crit)
    .sort_values(by="air_yards_mean", ascending=[False])
    .to_string()
)

