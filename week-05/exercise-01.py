from matplotlib import markers
import pandas as pd
import matplotlib.pyplot as plt

xValues = [1, 2, 3, 4, 6, 7, 8]
yValues = [2 * x + 3 for x in xValues]

df = pd.DataFrame({"x": xValues, "y": yValues})

df.plot(
    kind="line",
    x="x",
    y="y",
    marker="o",
    title="Exercise 1",
)
plt.show()
