import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/tt.xlsx")
df.replace(
    {
        "koulutus": {
            1: "Peruskoulu",
            2: "2. aste",
            3: "Korkeakoulu",
            4: "Ylempi korkeakoulu",
        }
    },
    inplace=True,
)

df.replace({"sukup": {1: "Mies", 2: "Nainen"}}, inplace=True)

test = pd.crosstab(df["koulutus"], df["sukup"])
