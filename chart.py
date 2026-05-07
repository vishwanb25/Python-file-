import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r"C:\Users\vishw\Downloads\python\icici balance sheet.csv")
df = data.melt("Year",["EquityCapital","Reserves","Deposits","TotalAssets"])
sns.barplot(x="Year",y="value",hue="variable",data=df)
plt.show()

