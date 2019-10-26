import xlrd

path = "book.xlsx"
inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)         

majors = {}

area1 = []
area2 = []
area3a = []
area3b = []
area4 = []
area5a = []
area5b = []

igetcareas = {"area1": area1, "area2" : area2, "area3a": area3a, "area3b": area3b, "area4": area4, "area5alab": area5a, "area5blab":area5b}

index = 0
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
    for inputclass in inputClassesTaken:
        for area in igetcareas:
            if inputclass not in igetcareas[area]:
                outputareas.append(area)
    return outputareas

inputclasses = ["MATH 104", "ENGL 101B", "ART 131", "CHEM 112A"]

print(compareClasses(inputclasses))
            
def compareMajor(major, possibleClasses):
    """
    take in string from major and compare to output of compareClasses to shorten possible list
    """

    return 1

def calculateSemesters():
    """
    Calculate time needed in each semester to finish igetc requirements
    """
    return 1
                                                    