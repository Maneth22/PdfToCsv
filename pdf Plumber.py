import pdfplumber
import pandas as pd

pdf = pdfplumber.open(r"report.pdf")
page0 = pdf.pages[0]
table = page0.extract_table()
df = pd.DataFrame(table)
print(df)
df.to_csv('temp2.csv', index=False)