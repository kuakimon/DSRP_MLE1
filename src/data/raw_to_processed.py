import pandas as pd
import os

BASE_PATH = "C:/Users/KEVIN/Downloads/DSRP/Machine Learning I/DSRP_MLE1"
os.chdir(BASE_PATH)

raw_df = pd.read_csv("data/raw/winequality-red.csv")

raw_df.to_parquet("data/processed/winequality-red.parquet", engine='pyarrow', compression='GZIP')



