# TO activate virtual environment:
# python3 -m venv .venv

#%%
# Task 1: Diary
# Importing the traceback module to show detailed error info
import traceback

try:
    # Opening diary.txt file in append mode so entries get added to the end of file
    with open("diary.txt", "a") as file:
        # Start with the first prompt
        prompt = "What happened today? "

        # Start an infinite loop to collect user input until "done for now" is entered
        while True:
            # Ask for a diary entry
            entry = input(prompt)

            # Write the input to the file, followed by a newline character
            file.write(entry + "\n")

            # If typing "done for now", break the loop and end the program
            if entry.lower().strip() == "done for now":
                break

            # Change the prompt for all following inputs
            prompt = "What else? "
#%%
# Catch any exception that occurs during the try block
except Exception as e:
    # Get the traceback details for more debugging
    trace_back = traceback.extract_tb(e.__traceback__)
    
    # Format the traceback into a list of readable lines
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(
            f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
        )

    # Print the type of exception
    print(f"Exception type: {type(e).__name__}")

    # Print the exception message
    message = str(e)
    if message:
        print(f"Exception message: {message}")

    # Print the full stack trace
    print(f"Stack trace: {stack_trace}")
