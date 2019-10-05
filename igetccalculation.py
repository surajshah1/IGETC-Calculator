import xlrd


path = "book.xlsx"
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

majors = []
area1 = []
area2 = []
area3a = []
area3b = []
area4 = []
area5a = []
area5b = []
igetcareas = {"area1": area1, "area2" : area2, "area3a": area3a, "area3b": area3b, "area4": area4, "area5alab": area5a, "area5blab":area5b}
index = 0
for x in igetcareas:
    for y in range(1,inputWorksheet.ncols):
        igetcareas[x].append(inputWorksheet.cell_value(y,index))
    index += 1
print(igetcareas)

class inputClassesTaken:
    area1 = []
    area2 = []
    area3 = []
    area4 = []
    area5a = []
    area5b = []
    def __init__(a1, a2, a3, a4):
        self.area1 = a1
        self.area2 = a2
        self.area3 = a3




def compareClasses(inputClassesTaken : inputClassesTaken):
    return 1

