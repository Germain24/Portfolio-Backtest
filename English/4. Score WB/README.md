# Warren Buffett's Strategy
## Database

### Using our database

Now that our database is created, we are going to import it in a new python file :

````python
import pandas as pd
import numpy as np

df = pd.read_csv('DatabaseWB_2022-10-20.csv', header=0)

df[f"Score WB"] = [0] * len(df[f"Ner Margin n-{i}"])
````

We need to create 5 missing elements that Warren Buffet use:

#### Creation of missing variables

````python
for i in range(10):
    df[f"ROI n-{i}"] = df[f"Revenue n-{i}"] / (df[f"Total assets n-{i}"] + df[f"Total liabilities n-{i}"])
    df[f"Gross Margin n-{i}"] = (df[f"Revenue n-{i}"] - df[f"Cost of revenue n-{i}"]) / df[f"Revenue n-{i}"]
    df[f"Ner Margin n-{i}"] = df[f"Net income n-{i}"] / df[f"Revenue n-{i}"]
    df[f"Earnings per shares n-{i}"] = df[f"Revenue n-{i}"] / df[f"Common stock number n-{i}"]

df[f"CountryZone"] = [2] * len(df[f"Ner Margin n-{i}"])

for i in ["Fr", "De", "At", "Be", "Bg", "Cy", "Hr", "Dk", "Es", "Ee", "Fi", "Gr", "Hu", "Ie", "It","Lv", "Lt", "Lu", "Mt", "Nl", "Gb"]:
    df[f"CountryZone"] += np.where((df[f"Country"] == i ), 1, 0)
````

