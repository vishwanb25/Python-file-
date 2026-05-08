import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df=pd.read_csv(r"C:\Users\vishw\Downloads\python\icici balance sheet.csv")
x= df["EquityCapital"]
y= df[["TotalAssets","Reserves","Deposits"]]
model=LinearRegression()
model.fit(x.values.reshape(-1,1),y)
coef=pd.Series(model.coef_.flatten(),index=y.columns)
coef.plot(kind="bar")
plt.title("Regression Coefficients")
plt.show()