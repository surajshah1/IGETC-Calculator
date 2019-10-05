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


print(igetcareas)
class inputClassesTaken:
    """
    Take in data from UI to create a student profile of classes
    """
    area1 = []
    area2 = []
    area3 = []
    area4 = []
    area5a = []
    area5b = []
    igetcsareas = {} 
    def __init__(a1, a2, a3, a4):
        self.area1 = a1
        self.area2 = a2
        self.area3 = a3




def compareClasses(inputClassesTaken: inputClassesTaken):
    """
    Input classes and compare to lists of classes in area to output list of classes required in each area

    """

    return 1

def compareMajor(major, possibleClasses):
    """
    take in string from major and compare to output of compareClasses to shorten possible list
    """
    return 1

def calculateSemesters():
    """
    Calculate time needed in each semester to finish igetc requirements
    """