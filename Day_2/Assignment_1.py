
from pathlib import Path

import pandas as pd

csv_path = Path(__file__).with_name('Gold_data (1).csv')
df = pd.read_csv(csv_path)
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
