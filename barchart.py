import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
PATH = r"C:\Users\vishw\Downloads\python\icici balance sheet.csv"
df   = pd.read_csv(PATH, parse_dates=['Year'])
x = np.arange(len(df))
plt.bar(x - 0.2, df['EquityCapital'],
        width=0.4, label='Equity')
plt.bar(x + 0.2, df['Reserves'],
        width=0.4, label='Reserves')
plt.xticks(x, df['Year'].dt.year, rotation=45)
plt.title('Equity Capital vs Reserves - 12507857 vishwan B')
plt.legend(); plt.tight_layout()
plt.show()
