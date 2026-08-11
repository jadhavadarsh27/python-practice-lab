import pandas as pd

data = {
    "Name" : ["Adarsh" , "Saurabh", "Sahil"],
    "Age" : [23, 23, 24],
    "Subject" : ["AWS", "Azure", "GCP"]
    }

df = pd.DataFrame(data)

print(df,)

print(df["Name"])
