import pandas as pd
import matplotlib.pyplot as plt
PATH = (r"C:\Users\vishw\Downloads\python\icici balance sheet.csv")
df   = pd.read_csv(PATH, parse_dates=['Year'])
latest = df.iloc[-1]
labels = ['Fixed Assets +','CWIP',
          'Investments','Other Assets +']
values = [latest[l] for l in labels]
plt.pie(values, labels=labels,
        autopct='%1.1f%%', startangle=140)
plt.title(f'Asset Mix 12507857 vishwan B – {latest["Year"].year}')
plt.show()
