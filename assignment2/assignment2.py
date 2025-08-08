# TO activate virtual environment:
# python3 -m venv .venv
#REMEMBER: Ctrl+s before testing, every time!!!

#%%
# Task 2: Read a CSV File
# Print a title so I can see where Task starts-I keep getting lost
print("\n--- Task 2: ---")

# To read the csv file
import csv

# To show more detailed errors if something goes wrong
import traceback

# To Define a function to read and process the employees file
def read_employees():
    try:
        # To store everything in a dictionary called data
        data = {}

        # This list to hold all the rows from the CSV (except header)
        rows = []

        # Open the employees.csv file
        with open("../csv/employees.csv", "r", newline='') as file:
            reader = csv.reader(file)

            # Loop through the rows; first row has headers
            for i, row in enumerate(reader):
                if i == 0:
                    # First row = header, store as "fields"
                    data["fields"] = row
                else:
                    # Remaining rows = actual employee data
                    rows.append(row)

            # Add collected data rows to the dictionary
            data["rows"] = rows

        # Return dictionary containing both headers and data
        return data

    # To catch the exception and show traceback if there's something wrong
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Message: {trace[3]}'
            for trace in trace_back
        ]

        # Display type of exception
        print(f"Exception type: {type(e).__name__}")

        # Display specific error message
        message = str(e)
        if message:
            print(f"Exception message: {message}")

        # Show stack trace for debugging
        print(f"Stack trace: {stack_trace}")

#%%
# global variable to store result of the function, so other parts of the program can use it
employees = read_employees()

#%%
# To verify the structure and contents of the dictionary just created
print(employees)

#%%
# Task 3: Find Column Index
# Print a title so I can see where Task starts-I keep getting lost
print("\n--- Task 3: ---")

# function to take the name of a column and return its index position (0 for the first column)
def column_index(column_name):
    return employees["fields"].index(column_name)

#%%
# To store the index of the employee_id column in a global variable
employee_id_column = column_index("employee_id")

#%%
# Print to confirm it's working
print(f"Index of 'employee_id': {employee_id_column}")


#%%
# Task 4: Find the Employee First Name by Row Number
# Print a title so I can see where Task starts-I keep getting lost
print("\n--- Task 4: ---")

# To return the first name from a given row index in the employees dataset using column_index() to figure out which column holds the first names,
def first_name(row_num):
    # Get the index of the first_name column
    col = column_index("first_name")

#%%
    # Use row number to grab the row from the employees list
    row = employees["rows"][row_num]

#%%
    # Return value in the correct column
    return row[col]

#%%
# Test call
print(f"First name at row 0: {first_name(0)}")


#%%
# Task 5: Find Employee — Function Inside a Function
# Print a title so I can see where Task starts-I keep getting lost
print("\n--- Task 5: ---")

# To search employee rows for the employee_id.
# To define a small helper function with filter().
def employee_find(employee_id):
    # Define a function inside this one to check each row for a match
    def employee_match(row):
        # To Compare the employee_id in this row with the one passed in and Convert both to int 
        return int(row[employee_id_column]) == employee_id

#%%
    # Use filter to find all rows that match, and convert result to list
    matches = list(filter(employee_match, employees["rows"]))

    return matches

#%%
# Test call — find employee with ID 1
print(f"Matching row(s) for employee_id 1: {employee_find(1)}")


#%%
# Task 6: Find the Employee using a Lambda
# Print a title so I can see where Task starts-I keep getting lost
print("\n--- Task 6: ---")

def employee_find_2(employee_id):
    # Use filter with a lambda to find matching rows
    # Lambda takes each row and compares employee_id values
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

#%%
    return matches

#%%
# Test call — find employee with ID 1 using lambda version
print(f"Lambda match for employee_id 1: {employee_find_2(1)}")


#%%
## Task 7: Sort the Rows by Last Name Using a Lambda

# Print a title so I can see where Task 7 starts-I keep getting lost
print("\n--- Task 7: Sort the Rows by Last Name ---")

#%%
# This function sorts the employee rows alphabetically by last name.
# It modifies employees["rows"] directly (in place).
def sort_by_last_name():
    # Get the index for the "last_name" column
    last_name_col = column_index("last_name")

    # Sort the rows using a lambda to pull the last name from each row
    employees["rows"].sort(key=lambda row: row[last_name_col])

    # Return the sorted list just in case I want to preview or use it later
    return employees["rows"]

# Test call to preview the sorted list
print("Sorted by last name:")
for row in sort_by_last_name():
    print(row)


#%%
# Task 8: Create a dict for an Employee
# Print a title so it’s clear in the output where Task 8 starts
print("\n--- Task 8: Create a dict for an Employee ---")

#%%
# To convert a row into a dictionary of field:value pairs
# Skips the 'employee_id' field
def employee_dict(row):
    # Get the index of employee_id so it can be skipped
    emp_id_col = column_index("employee_id")

    # Create the dictionary by pairing headers with row values
    emp_dict = {}
    for i, field in enumerate(employees["fields"]):
        if i != emp_id_col:  # skip employee_id
            emp_dict[field] = row[i]

    return emp_dict

#%%
# Test call: pass the first row from employees["rows"]
test_employee = employee_dict(employees["rows"][0])
print(test_employee)

#%%
# Task 9: Dicts for All Employees
# Print a title
print("\n--- Task 9: Dicts for All Employees ---")

#%%
# creates a dictionary {Key   = employee_id (from each row), Value = employee's dictionary (from Task 8)}
def all_employees_dict():
    # To get the index of employee_id= key - Same process as a visual basic database way back when...
    emp_id_col = column_index("employee_id")

#%%
    # Build the big dictionary
    all_emps = {}
    for row in employees["rows"]:
        emp_id = row[emp_id_col]
        all_emps[emp_id] = employee_dict(row)

    return all_emps

#%%
# Test call: create the full dictionary and print it
full_employee_dict = all_employees_dict()
print(full_employee_dict)

#%%
# Task 10: Use the os Module
# Title
print("\n--- Task 10: Use the os Module ---")

#%%
import os  # For accessing environment variables & interacting with OS

#%%
# Reads environment variable THISVALUE and returns its value.
def get_this_value():
    return os.getenv("THISVALUE")

#%%
# Test call: Have THISVALUE set in the terminal session
print(f"Value of THISVALUE: {get_this_value()}")


#%%
# Task 11: Creating My Own Module
# Task title
print("\n--- Task 11: Creating My Own Module ---")

#%%
# Import custom module from same folder
import custom_module

# Set the secret in the custom module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Test call: change secret and then print it
set_that_secret("open_sesame")
print(f"Updated secret in custom_module: {custom_module.secret}")


#%%
# Task 12: Read minutes*.csv files
# Task title
print("\n--- Task 12: Read minutes1.csv and minutes2.csv ---")

#%%
# To read two CSV files and return data as dictionaries (like employees),
# covert rows into a tuple so data can be stored in sets after.
# Remember: Tuples are immutable, so they can't be changed!
def read_minutes():
    def read_csv_as_dict(path):
        data = {}
        rows = []
        with open(path, "r", newline='') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(tuple(row))  # convert each row to tuple
            data["rows"] = rows
        return data
    
#%%
    # Read both CSV files from the ../csv directory
    minutes1 = read_csv_as_dict("../csv/minutes1.csv")
    minutes2 = read_csv_as_dict("../csv/minutes2.csv")

    return minutes1, minutes2
#%%
# Store results in global variables
minutes1, minutes2 = read_minutes()

#%%
# Test print to confirm structure
print("Minutes1:", minutes1)
print("Minutes2:", minutes2)


#%%
# Task 13: Create minutes_set
# Task title:
print("\n--- Task 13: Create minutes_set ---")

#%%
# Create a set with unique rows from minutes1 & minutes2
def create_minutes_set():
    # To Convert rows from both dictionaries into sets
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

#%%
    # Combine both sets
    combined = set1.union(set2)

    return combined
#%%
# Store in global variable
minutes_set = create_minutes_set()

# Test print
print("Minutes set:", minutes_set)


#%%
# Task 14: Convert to datetime
# Task title:
print("\n--- Task 14: Convert to datetime ---")

#%%
from datetime import datetime  # converting strings to datetime objects

#%%
# converts date strings in the set from task 13 into datetime objects
def create_minutes_list():
    # Convert set into a list (unordered)
    minutes_list = list(minutes_set)

#%%
    # Map each tuple (name, date_str) to (name, datetime_obj)
    minutes_list = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    )

    return minutes_list

#%%
# Store in global variable
minutes_list = create_minutes_list()

#%%
# Test print to check conversion
print("Minutes list with datetime objects:", minutes_list)


#%%
# Task 15: Write Out Sorted List
# Task title
print("\n--- Task 15: Write Out Sorted List ---")

#%%
# to sort minutes_list by date, convert dates back to strings, write results to a csv
def write_sorted_list():
    # Sort the list - ascending (second element)
    minutes_list.sort(key=lambda x: x[1])

    # Convert datetime objects back to formatted strings
    converted_list = list(
        map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list)
    )
#%%
    # Write the header and rows to minutes.csv in the current folder
    with open("minutes.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])  # header 
        writer.writerows(converted_list)     # sorted data rows

    return converted_list
#%%
# Test call 
sorted_minutes = write_sorted_list()
print("Sorted minutes written to minutes.csv:")
print(sorted_minutes)

