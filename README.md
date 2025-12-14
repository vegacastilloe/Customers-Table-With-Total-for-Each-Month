# 💼 Customers-Table-With-Total-for-Each-Month

![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Customers-Table-With-Total-for-Each-Month)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟  Easy Sunday Excel Challenge No.83 - 2025/12/14 🌟
- 🌟 **Author**: Crispo Mwangi

    - ⭐Pivot the Customers Table
    - ⭐Create a Total for Each Month
    - ⭐Solution MUST be dynamic 


 🔰 Este script toma un DataFrame de Excel con columnas `Month`, `Customer` y `Sales`, la finalidad es normalizar y generar una tabla con el detallade de los clientes y sus ventas. Al final de cada bloque mensual, se agrega una fila con el **Total Sales**.

 🔗 Link to Excel file:
 👉 https://lnkd.in/dZw88Ejj

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Customers-Table-With-Total-for-Each-Month/blob/main/customers_table_total_month.py

---
---

## Pivot Customers Sales with 🐼 Pandas

Este script toma un DataFrame de Excel con columnas `Month`, `Customer` y `Sales`, la finalidad es normalizar y generar una tabla con el detallade de los clientes y sus ventas. Al final de cada bloque mensual, se agrega una fila con el **Total Sales**.



## 📦 Requisitos

- Python 3.9+
- Paquetes:
- Numpy
- pandas openpyxl (para leer .xlsx)
- tabulate (solo para impresión bonita)
- Archivo Excel con al menos:
    - Las columnas: `Month`, `Customer` y `Sales`.
    - En las columnas siguientes : Los resultados esperados para comparación

---

## 🚀 Cómo funciona

1. **Lectura y limpieza inicial**  
   - Se lee el Excel (`pd.read_excel`) y se eliminan columnas vacías.  
   - Se ajustan los nombres de columnas (`.str.strip()`).

2. **Pipeline con `.pipe()`**  
   - Se dividen los nombres y valores en listas (`str.split(',')`).  
   - Se alinean nombres y valores, expandiendo filas.  
   - Se convierten los valores a enteros.  
   - Se agrupan por mes y se inserta una fila `Total Sales` al final de cada bloque.  
   - Se sanitizan valores nulos (`fillna("")`).
---

## 📤 Salida

1. **Salida tabulada**  
   - Se imprime con `tabulate` en formato GitHub.

2. **El script imprime un DataFrame con:**
   - `Month`
   - `Customer`
   - `Sales`

---

## 📊 Output:

```text
| Month       | Customer   |   Sales |
|-------------|------------|---------|
| Jan         | Melissa    |     250 |
| Jan         | Brian      |     350 |
| Total Sales |            |     600 |
| Feb         | Aditya     |     100 |
| Feb         | Aditya     |     200 |
| Feb         | Aditya     |     300 |
| Total Sales |            |     600 |
| Mar         | Aiden      |    1050 |
| Mar         | Adrian     |     950 |
| Mar         | Andy       |     650 |
| Total Sales |            |    2650 |
| Apr         | Ellen      |     200 |
| Total Sales |            |     200 |
---
```
## 🛠️ Personalización

Puedes adaptar el script para:

- Aplicar reglas más complejas
- Exportar el resultado a Excel o CSV

---

## 🚀 Ejecución

import pandas as pd
import numpy as np
from tabulate import tabulate

```python
# 📦 Leer y limpiar el archivo
df_raw = pd.read_excel(xl, header=1).dropna(axis=1, how='all')
df_raw.columns = df_raw.columns.str.strip()

# 🎯 Seleccionar columnas útiles
df_input = df_raw.iloc[:4 , :3].copy()

# 🧠 Flujo del script
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
```
### 💾 Exportación opcional
```python
# df_input.to_excel("customers_table_total_month_output.xlsx", index=False)
```

---
### 📄 Licencia
---
Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.

---
