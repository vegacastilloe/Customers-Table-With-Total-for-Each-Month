import pandas as pd
import numpy as np
from tabulate import tabulate

df_raw = pd.read_excel(xl, header=1).dropna(axis=1, how='all')
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:4 , :3].copy()

final = (
    df_input
      .pipe(lambda d: d.assign(
          Names=d['Customer'].astype(str).str.split(','),
          Values=d['Sales'].astype(str).str.split(',')
      ))
      .pipe(lambda d: pd.DataFrame([
          [row['Month'], n.strip(), int(v.strip().replace(',', ''))]
          for _, row in d.iterrows()
          for n, v in zip(
              row['Names'] * max(1, len(row['Values'])) if len(row['Names']) < len(row['Values']) else row['Names'],
              row['Values'] * max(1, len(row['Names'])) if len(row['Values']) < len(row['Names']) else row['Values']
          )
          if v.strip().replace(',', '').isdigit()
      ], columns=['Month','Customer','Sales']))
      .pipe(lambda d: pd.DataFrame(
          sum([group.values.tolist() + [['Total Sales', np.nan, group['Sales'].sum()]]
               for _, group in d.groupby('Month', sort=False)], [])
          , columns=['Month','Customer','Sales'])
      .pipe(lambda d: d.fillna(""))
      )
)

print(tabulate(final.values, headers=final.columns, tablefmt='github'))

# 💾 Exportación opcional
# df_input.to_excel("customers_table_total_month_output.xlsx", index=False)
