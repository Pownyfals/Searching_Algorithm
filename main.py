import xlsxwriter as xw

workbook = xw.Workbook('tabel.xlsx')
worksheet = workbook.add_worksheet()

tabel = []
masukan = int(input("masukan jumlah table : "))
for i in range(0,masukan):
    if(i<9):
        tabel.append("Tabel_0"+str(i+1))
    else:
        tabel.append("Tabel_"+str(i+1))

    worksheet.write(0,0,"Nama Tabel")
for i in range(0,masukan):
    worksheet.write(i+1, 0,tabel[i])

workbook.close()
    


