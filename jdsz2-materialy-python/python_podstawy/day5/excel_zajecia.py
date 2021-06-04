import xlrd

zeszyt = xlrd.open_workbook("budownictwo_mieszkaniowe_iii_kwartal_2018.xlsx")

print("Dostepne arkusze:")
for arkusz in zeszyt.sheets():
    print(arkusz.name)

ark = zeszyt.sheet_by_name("2")
for wiersz in range(11, ark.nrows):
    print(ark.row(wiersz)[0].value, ark.row(wiersz)[2].value)
