# Import Module 
import tabula 

# Read PDF File 
# this contain a list 
df = tabula.read_pdf('report.pdf', pages = 1)[0]

df.to_csv('Temp.csv',index=False)

print(df)
