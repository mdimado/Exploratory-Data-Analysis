import pandas as pd
import numpy as np

df = pd.read_csv("Churn_Modelling.csv")

null_fraction = 0.15  
df.loc[df.sample(frac=null_fraction).index, ["Gender", "Age"]] = np.nan

df.to_csv("Churn_Modelling_with_nulls.csv", index=False)
