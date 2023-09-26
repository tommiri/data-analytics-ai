import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/tt.xlsx")
# df.describe()
# df.hist()
# df.info()


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

test = pd.crosstab(df["koulutus"], ["Lukumäärä"], rownames=["Koulutus"]) * 100

test.columns = ["Prosenttiosuus"]
