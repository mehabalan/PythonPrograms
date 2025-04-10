import os
def findfiletype(filepath):
    filename=os.path.basename(filepath)
    filetype=filename.split(".")[-1].lower()
    return filetype
findfiletype(r"C:\Users\Meha\PycharmProjects\TestingProjects\testdata\userdata.xlsx")
