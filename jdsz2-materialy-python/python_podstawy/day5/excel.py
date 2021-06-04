import xlrd

zeszyt = xlrd.open_workbook("budownictwo_mieszkaniowe_iii_kwartal_2018.xlsx")
for arkusz in zeszyt.sheets():
    print(arkusz.name)

ark = zeszyt.sheet_by_index(0)

for wiersz in range(ark.nrows):
    for komorka in ark.row(wiersz):
        if komorka.ctype != xlrd.XL_CELL_EMPTY:
            if komorka.ctype == xlrd.XL_CELL_NUMBER:
                print(komorka.value)
            elif komorka.ctype == xlrd.XL_CELL_TEXT:
                print(komorka.value)