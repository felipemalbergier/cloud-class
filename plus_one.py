import pandas as pd
import sys

assert len(sys.argv) > 1

filename = sys.argv[1]

df = pd.read_csv(filename)
print(df)
df = df + 1
df.to_csv('output_' + filename, index=False)