import pandas as pd

data = {
    "name" : ["Adarsh", "Saurabh", "Sahil"],
    "Age" : [23, 24, 25],
    "Subject" : ["Python", "C++", ".Net"]
    }

df = pd.DataFrame(data)

print(df)
