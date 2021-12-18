from tkinter.filedialog import askdirectory, askopenfile, askopenfilename

excelArray = ["excel", "xlsx", "xl", "x", "exsel", "ex", "e"]
consoleArray = ["console", "c", "concole", "con", "consle"]

pathToExcel = askopenfilename()
print(f"\nOpening the excel document located at: {pathToExcel}")

userOutput = input("\nWhere would you like the output to be? Console or Excel?").lower()
if userOutput in excelArray:
    print("Where would you like to save it?")
    saved = askdirectory()
    print("Saved")
else:
    print("\n")