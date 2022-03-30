import random 
import pandas as pd
import xlsxwriter as xw



#membuat table
from collections import defaultdict
graph = defaultdict(list)

for i in range(10):
  for j in range(random.randint(3,5)):

    y = random.randint(1,10)
    if y not in graph[i+1]:
      graph[i+1].append(y)
    else:
      j-=1


listTable = []
table1 =[]
table2 = []
relasi = []
for k in graph:

  namaTable = "table_"+str(k)
  listTable.append(namaTable)

  for val in graph[k]:
    isi1 = "table_"+str(k)
    isi2 = "table_"+str(val)
    relasi1 = "atribure_"+str(k)+"_"+str(val)
    table1.append(isi1)
    table2.append(isi2)
    relasi.append(relasi1)
    
    

dataTable = {"Nama_Table":listTable}
dataRelasi = {"relasi":relasi,"table1":table1,"table2":table2}


#inisialisasi worksheet
workbook = xw.Workbook('relasi.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write
column = 0
row = 0
#membuat judul tiap tabel
worksheet.write(row,column,"Atribut Relasi")
worksheet.write(row, column+1,"Tabel1")
worksheet.write(row, column+2,"Tabel2")
#memasukan data dari list kedalam excel
for i in range(0,len(table1)):
    worksheet.write(row+1,column,relasi[i])
    worksheet.write(row+1, column+1,table1[i])
    worksheet.write(row+1, column+2,table2[i])
    row+=1
#close workbook
workbook.close()
#tamat

