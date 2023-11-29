import pandas as pd

df = pd.read_csv(r"C:\Users\r14ale\Desktop\Book1.csv",usecols=['Hello',], index_col=False)
print(df.to_csv(r"C:\Users\r14ale\Desktop\Book2.csv", index=False))