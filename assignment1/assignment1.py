# Task 1
# This is my starter function that doesn’t take any input.
# It just returns the string "Hello!" — kind of like a greeting test.
def hello():
    return "Hello!"


# Task 2
# This function takes a name as input (like "James") and returns "Hello, James!"
# I'm using an f-string here to plug the variable into the sentence.
def greet(name):
    return f"Hello, {name}!"


# Task 3
# This is my calculator function. It takes two values and an operation type
# If no operation is given, it defaults to "multiply".
# I used match-case to make the choices cleaner.
# There are two try-except blocks to catch divide-by-zero and type errors. I wrote them in my "Physics Teacher Voice"

def calc(val1, val2, operation="multiply"):
    try:
        match operation:
            case "add":
                return val1 + val2
            case "subtract":
                return val1 - val2
            case "multiply":
                return val1 * val2
            case "divide":
                return val1 / val2
            case "modulo":
                return val1 % val2
            case "int_divide":
                return val1 // val2  # Floor division
            case "power":
                return val1 ** val2
            case _:
                return "Unknown operation"
    except ZeroDivisionError:
            # The silly version I like: "There is no pizza to split if nobody buys it!"
            # But the test expects this exact text or it fails:
        return "You can't divide by 0!"
    except TypeError:
        # This handles things like trying to multiply two strings
        return "You can't multiply those values!"


# Task 4
# This function tries to convert a value (like a string "110") to a given data type.
# If it can't convert it (like "hello" into an integer), it catches the ValueError and shows a helpful message.

def data_type_conversion(value, type_name):
    try:
        if type_name == "float":
            return float(value)  # convert to float
        elif type_name == "int":
            return int(value)    # convert to integer
        elif type_name == "str":
            return str(value)    # convert to string
    except ValueError:
        # This catches the error and returns a message with the actual inputs
        return f"You can't convert {value} into a {type_name}."

# Task 5
# This function takes any number of test scores (thanks to *args) and averages them.
# It then returns a letter grade based on the average.
# If something weird is passed (like strings), it'll catch the error and return a warning.

def grade(*args):
    try:
        avg = sum(args) / len(args)  # Calculate average from however many values are passed
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except:
        # Catch-all if something non-numeric is passed — protects the function from crashing
        return "Invalid data was provided."

# Task 6
# This one repeats a string however many times I tell it to.
# I’m using a for loop with range here, even though I could just do string * count.
# Good practice with loops.

def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


# Task 7
# This function takes scores in keyword form like student="score" (using **kwargs).
# It can return the name of the top student ("best") or the average of all scores ("mean"). I am definitely using this in my classroom this year!

def student_scores(mode, **kwargs):
    if not kwargs:
        return "No student scores provided."
    
    if mode == "best":
        # Return the student with the highest score
        return max(kwargs, key=kwargs.get)
    elif mode == "mean":
        avg = sum(kwargs.values()) / len(kwargs)
        return avg


# Task 8
# This function makes a string look like a book title.
# It capitalizes the first and last words, and only capitalizes the middle words
# if they aren’t one of the "little words".

def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            # Always capitalize first and last word
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word.lower())  # leave little words lowercase
        else:
            result.append(word.capitalize())
    
    return " ".join(result)


# Task 9
# Hangman time! This function shows guessed letters and hides the rest with underscores.
# If a letter from the secret word is in the guess string, it stays.
# Otherwise, it gets replaced with "_".

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


# Task 10
# This one translates English to Pig Latin. My native language is Spanish, so I never used Pig Latin. I only know it from TV shows!
# Rule: If word starts with a vowel, add "ay" at the end.
# If it starts with consonants, move them to the end and add "ay".
# If it starts with "qu", treat it as a unit and move both.
# My brain hurts trying to understand pig Latin in real life!
# My first try failed, so I spent a bit of more time on this task. 
# Special case: if the word starts with "squ", treat all 3 letters as one sound.
# REMINDER: Python reads letter-by-letter, but "squ" is really just one chunky sound in Pig Latin, apparently. Copilot told me so...

def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if word.startswith("squ"):
            # Special case: "squ" goes to the end
            result.append(word[3:] + "squay")
        elif word.startswith("qu"):
            # Also move "qu" to the end
            result.append(word[2:] + "quay")
        elif word[0] in vowels:
            result.append(word + "ay")
        else:
            # Move initial consonant cluster to the end
            i = 0
            while i < len(word) and word[i] not in vowels:
                # Stop if we hit a vowel
                i += 1
            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)

