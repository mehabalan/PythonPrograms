import os
import pandas as pd
import json
filepath=r'C:/Users/Meha/PycharmProjects/TestingProjects/testdata/userdata.xlsx'
# Function to find file type
def findfiletype(filepath):
    filename = os.path.basename(filepath)
    filetype = filename.split(".")[-1].lower()
    return filetype

# Function to extract data based on the file type
def extractdata(filepath):
    filetype = findfiletype(filepath)  # Determine the file type based on filepath
    if filetype == "xlsx":
        df = pd.read_excel(filepath)  # to Read the Excel file read_excel() is a buildin function in pandas
        result = df.to_dict(orient="records")  # Convert the dataframe to a list of records
        print(result)
        return result
    elif filetype == "csv":
        df = pd.read_csv(filepath)  # Read the CSV file
        result = df.to_dict(orient="records")  # Convert the dataframe to a list of records
        return result
    elif filetype == "json":
        with open(filepath, "r", encoding="utf-8") as f:  # Open the JSON file
            result = json.load(f)  # Parse the JSON file
            return result
    else:
        raise ValueError("Unsupported file type")  # Raise an error if the file type is unsupported
    print(result)
extractdata(filepath)
