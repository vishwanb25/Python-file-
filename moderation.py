import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\vishw\Downloads\python\icici balance sheet.csv").dropna()
df.columns = df.columns.str.strip()
df = df.select_dtypes(include="number")
Y = "TotalAssets"
moderator = "Borrowing"

explanatory = [c for c in df.columns if c not in [Y, moderator]]

df["FinancialStrength"] = df[explanatory].mean(axis=1)
df["FSxModerator"] = df["FinancialStrength"] *df[moderator]

G = nx.DiGraph()

G.add_edge("FinancialStrength", "TotalAssets")
G.add_edge(moderator, "TotalAssets")
G.add_edge("FSxModerator", "TotalAssets")

pos = {
    "FinancialStrength": (0, 1),
    moderator: (0, -1),
    "FSxModerator": (0, 0),
    "TotalAssets": (2, 0)
}

nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue",
        font_size=10, font_weight="bold", arrows=True)

plt.title("Moderation Model: Financial Strength -> Total Assets")
plt.show()