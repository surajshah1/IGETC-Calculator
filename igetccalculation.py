import xlrd
import sys
path = "book.xlsx"
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

inputClassesTaken = list(sys.argv[1])

area1 = []
area2 = []
area3a = []
area3b = []
area4 = []
area5a = []
area5b = []

igetcareas = {"area1": area1, "area2" : area2, "area3a": area3a, "area3b": area3b, "area4": area4, "area5alab": area5a, "area5blab":area5b}

for x in range(1,4):
    igetcareas["area1"].append(inputWorksheet.cell_value(x,0))

for x in range(1,9):
    igetcareas["area2"].append(inputWorksheet.cell_value(x,1))

for x in range(1,25):
    igetcareas["area3a"].append(inputWorksheet.cell_value(x,2))

for x in range(1,62):
    igetcareas["area3b"].append(inputWorksheet.cell_value(x,3))

for x in range(1,65):
    igetcareas["area4"].append(inputWorksheet.cell_value(x,4))

def compareClasses(inputClassesTaken):
    """
    Input classes and compare to lists of classes in area to output list of classes required in each area
    """
    outputareas = []
    for areas in igetcareas:
        for course in inputClassesTaken:
            if course in igetcareas[areas]:
                outputareas.append(areas)
    return outputareas    

x = compareClasses(inputClassesTaken))
print(x)
sys.stdout.flush() 

