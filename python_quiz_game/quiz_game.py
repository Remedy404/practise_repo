import random

def display_header():
    print("=" * 40)
    print("          PYTHON QUIZ GAME")
    print("=" * 40)

def get_questions():
    return [
        # FUNCTIONS (15)
        {"question": "What is a function in Python?", "options": {"A": "A reusable block of code", "B": "A type of computer", "C": "A mathematical symbol", "D": "A Python error"}, "answer": "A", "explanation": "A function is a reusable block of code that performs a particular task."},
        {"question": "Which keyword is used to define a function?", "options": {"A": "function", "B": "def", "C": "make", "D": "fun"}, "answer": "B", "explanation": "Python uses the def keyword to define a function."},
        {"question": "Which symbol comes after a function definition header?", "options": {"A": "Semicolon (;)", "B": "Comma (,)", "C": "Colon (:)", "D": "Full stop (.)"}, "answer": "C", "explanation": "A colon marks the beginning of the function body."},
        {"question": "How do you call a function named greet?", "options": {"A": "call greet", "B": "greet()", "C": "def greet", "D": "run greet"}, "answer": "B", "explanation": "A function is called by writing its name followed by parentheses."},
        {"question": "What does the return keyword do?", "options": {"A": "Repeats a function", "B": "Deletes a function", "C": "Sends a result back", "D": "Prints every variable"}, "answer": "C", "explanation": "return sends a value from a function back to the code that called it."},
        {"question": "What is a parameter?", "options": {"A": "A variable listed in a function definition", "B": "A Python error", "C": "A comment", "D": "A loop"}, "answer": "A", "explanation": "A parameter is a named variable that a function can receive as input."},
        {"question": "What is an argument?", "options": {"A": "The function name", "B": "A value passed when calling a function", "C": "A comment", "D": "A data type"}, "answer": "B", "explanation": "An argument is the actual value supplied to a function call."},
        {"question": "What is the output of this function? def add(): return 2 + 3; print(add())", "options": {"A": "2", "B": "3", "C": "5", "D": "add"}, "answer": "C", "explanation": "The function returns 2 + 3, which is 5."},
        {"question": "Which statement sends a value back from a function?", "options": {"A": "input", "B": "return", "C": "break", "D": "continue"}, "answer": "B", "explanation": "The return statement sends a result back to the caller."},
        {"question": "What happens if a function has no return statement?", "options": {"A": "It returns None by default", "B": "It always crashes", "C": "It returns zero", "D": "It repeats forever"}, "answer": "A", "explanation": "A Python function without a return statement returns None."},
        {"question": "Which is a valid function definition?", "options": {"A": "def greet():", "B": "function greet:", "C": "greet def()", "D": "define greet()"}, "answer": "A", "explanation": "The correct syntax starts with def, then the function name and parentheses."},
        {"question": "Why are functions useful?", "options": {"A": "They make code reusable", "B": "They stop Python", "C": "They remove all variables", "D": "They replace the computer"}, "answer": "A", "explanation": "Functions help organise code and avoid repeating the same instructions."},
        {"question": "What is a default parameter value?", "options": {"A": "A value used when no argument is supplied", "B": "A value that must be deleted", "C": "A type of loop", "D": "A syntax error"}, "answer": "A", "explanation": "A default value is used when the caller does not provide that argument."},
        {"question": "What does len() do?", "options": {"A": "Converts text to a number", "B": "Returns the length of an object", "C": "Prints a message", "D": "Defines a function"}, "answer": "B", "explanation": "len() returns the number of items or characters in an object."},
        {"question": "Which built-in function displays output?", "options": {"A": "input()", "B": "type()", "C": "print()", "D": "int()"}, "answer": "C", "explanation": "print() displays information on the screen."},

        # BASIC DATA TYPES (15)
        {"question": "Which data type is used for whole numbers such as 10?", "options": {"A": "str", "B": "int", "C": "float", "D": "bool"}, "answer": "B", "explanation": "int represents whole numbers."},
        {"question": "What is the data type of 3.14?", "options": {"A": "int", "B": "str", "C": "float", "D": "bool"}, "answer": "C", "explanation": "A number with a decimal point is a float."},
        {"question": "Which data type stores text?", "options": {"A": "str", "B": "int", "C": "float", "D": "bool"}, "answer": "A", "explanation": "str, short for string, stores text."},
        {"question": "Which data type represents True or False?", "options": {"A": "float", "B": "str", "C": "bool", "D": "int"}, "answer": "C", "explanation": "bool is the Boolean data type and has True or False values."},
        {"question": "What is the data type of 25?", "options": {"A": "float", "B": "int", "C": "str", "D": "bool"}, "answer": "B", "explanation": "25 is a whole number, so its type is int."},
        {"question": "What is the data type of \"Hello\"?", "options": {"A": "int", "B": "float", "C": "str", "D": "bool"}, "answer": "C", "explanation": "Text inside quotation marks is a string (str)."},
        {"question": "What is the result of type(7)?", "options": {"A": "str", "B": "int", "C": "float", "D": "bool"}, "answer": "B", "explanation": "type() reports the data type; 7 is an integer."},
        {"question": "Which value is a Boolean?", "options": {"A": "\"True\"", "B": "100", "C": "True", "D": "2.5"}, "answer": "C", "explanation": "True without quotation marks is a Boolean value."},
        {"question": "Which function converts a value to an integer when possible?", "options": {"A": "str()", "B": "int()", "C": "float()", "D": "type()"}, "answer": "B", "explanation": "int() converts a compatible value to an integer."},
        {"question": "What does str(25) produce?", "options": {"A": "25 as text", "B": "25.0", "C": "True", "D": "An error in every case"}, "answer": "A", "explanation": "str() converts the number 25 into the string \"25\"."},
        {"question": "Which function can convert 5 to 5.0?", "options": {"A": "bool()", "B": "str()", "C": "float()", "D": "type()"}, "answer": "C", "explanation": "float() converts a compatible number to a floating-point value."},
        {"question": "Which of these is a string?", "options": {"A": "42", "B": "False", "C": "\"42\"", "D": "4.2"}, "answer": "C", "explanation": "Quotation marks make 42 text rather than a number."},
        {"question": "What is the type of 8.0?", "options": {"A": "int", "B": "float", "C": "str", "D": "bool"}, "answer": "B", "explanation": "A number written with a decimal point is a float."},
        {"question": "What is the result of bool(0)?", "options": {"A": "True", "B": "False", "C": "0.0", "D": "\"0\""}, "answer": "B", "explanation": "The number zero converts to False with bool()."},
        {"question": "Which data type would you use to store a person's name?", "options": {"A": "int", "B": "float", "C": "str", "D": "bool"}, "answer": "C", "explanation": "A person's name is text, so str is appropriate."},

        # CONDITIONAL STATEMENTS (12)
        {"question": "Which keyword begins a conditional statement?", "options": {"A": "if", "B": "for", "C": "def", "D": "print"}, "answer": "A", "explanation": "if checks whether a condition is True."},
        {"question": "Which keyword is used when the first if condition is False and another condition should be checked?", "options": {"A": "else", "B": "elif", "C": "while", "D": "return"}, "answer": "B", "explanation": "elif means else if and checks another condition."},
        {"question": "Which keyword runs when the if and all elif conditions are False?", "options": {"A": "def", "B": "elif", "C": "else", "D": "pass"}, "answer": "C", "explanation": "The else block handles cases not matched by earlier conditions."},
        {"question": "Which operator checks whether two values are equal?", "options": {"A": "=", "B": "==", "C": "!=", "D": ">="}, "answer": "B", "explanation": "== compares two values for equality; = assigns a value."},
        {"question": "What does the != operator mean?", "options": {"A": "Equal to", "B": "Greater than", "C": "Not equal to", "D": "Less than"}, "answer": "C", "explanation": "!= checks whether two values are different."},
        {"question": "What is the result of 5 > 3?", "options": {"A": "True", "B": "False", "C": "5", "D": "3"}, "answer": "A", "explanation": "Five is greater than three, so the expression is True."},
        {"question": "Which operator means logical AND?", "options": {"A": "or", "B": "not", "C": "and", "D": "&&"}, "answer": "C", "explanation": "and is True only when both conditions are True."},
        {"question": "Which operator means at least one condition can be True?", "options": {"A": "and", "B": "or", "C": "not", "D": "is"}, "answer": "B", "explanation": "or is True when at least one condition is True."},
        {"question": "What does the not operator do?", "options": {"A": "Repeats a condition", "B": "Reverses a Boolean value", "C": "Adds two numbers", "D": "Defines a function"}, "answer": "B", "explanation": "not changes True to False and False to True."},
        {"question": "What is printed? x = 4; if x > 2: print(\"Yes\")", "options": {"A": "No", "B": "4", "C": "Yes", "D": "Nothing"}, "answer": "C", "explanation": "Since 4 is greater than 2, the if block runs."},
        {"question": "What is indentation used for in an if statement?", "options": {"A": "To show which code belongs to the block", "B": "To rename variables", "C": "To create numbers", "D": "To end Python"}, "answer": "A", "explanation": "Indentation defines the body of an if, elif, or else block."},
        {"question": "Which symbol means less than or equal to?", "options": {"A": "=>", "B": "=<", "C": "<=", "D": "=="}, "answer": "C", "explanation": "<= checks whether a value is smaller than or equal to another."},

        # PYTHON FUNDAMENTALS (8)
        {"question": "Which function is used to receive input from a user?", "options": {"A": "print()", "B": "input()", "C": "type()", "D": "range()"}, "answer": "B", "explanation": "input() reads text entered by the user."},
        {"question": "Which character starts a single-line comment in Python?", "options": {"A": "//", "B": "/*", "C": "#", "D": "--"}, "answer": "C", "explanation": "A hash symbol (#) begins a single-line comment."},
        {"question": "Which of these is a valid Python variable name?", "options": {"A": "2name", "B": "first_name", "C": "first-name", "D": "class"}, "answer": "B", "explanation": "Variable names can contain underscores and cannot begin with a digit or use reserved keywords."},
        {"question": "What is the output of print(2 + 3)?", "options": {"A": "23", "B": "5", "C": "2 + 3", "D": "Error"}, "answer": "B", "explanation": "The + operator adds the two numbers, producing 5."},
        {"question": "Which operator is used for multiplication?", "options": {"A": "+", "B": "/", "C": "*", "D": "%"}, "answer": "C", "explanation": "The asterisk (*) is Python's multiplication operator."},
        {"question": "What is the usual file extension for a Python file?", "options": {"A": ".txt", "B": ".html", "C": ".py", "D": ".java"}, "answer": "C", "explanation": "Python source files commonly use the .py extension."},
        {"question": "What does the = operator do in a statement such as age = 15?", "options": {"A": "Compares two values", "B": "Assigns a value to a variable", "C": "Checks a condition", "D": "Prints a value"}, "answer": "B", "explanation": "The = operator assigns the value on the right to the variable on the left."},
        {"question": "Which statement can stop a loop immediately?", "options": {"A": "break", "B": "continue", "C": "def", "D": "input"}, "answer": "A", "explanation": "break exits the nearest enclosing loop."}
    ]

def get_player_answer():
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ("A", "B", "C", "D"):
            return answer
        print("Invalid choice! Please enter A, B, C or D.")

def display_results(player_name, score, total):
    percentage = round((score / total) * 100, 1) if total else 0
    print("\n" + "=" * 40)
    print("              QUIZ RESULTS")
    print("=" * 40)
    print(f"Player: {player_name}")
    print(f"Correct answers: {score}/{total}")
    print(f"Incorrect answers: {total - score}")
    print(f"Percentage: {percentage}%")
    if percentage >= 80:
        print("Excellent work! You have done very well.")
    elif percentage >= 60:
        print("Good job! Keep practising.")
    elif percentage >= 40:
        print("Nice effort! There is still room to improve.")
    else:
        print("Keep learning. Every attempt helps you improve.")
    print("=" * 40)

def run_quiz(player_name):
    questions = get_questions()
    random.shuffle(questions)
    score = 0
    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}/{len(questions)}")
        print(question["question"])
        for option, text in question["options"].items():
            print(f"{option}. {text}")
        answer = get_player_answer()
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Not quite. The correct answer is {question['answer']}.")
        print("Explanation:", question["explanation"])
    display_results(player_name, score, len(questions))

def main():
    display_header()
    print("Welcome to the Python Quiz Game!")
    player_name = input("Enter your name: ").strip() or "Player"
    print(f"\nWelcome, {player_name}!")
    print("Get ready to test your Python knowledge!")
    while True:
        run_quiz(player_name)
        again = input("\nWould you like to play again? (Y/N): ").strip().upper()
        if again != "Y":
            print("Thanks for playing. Keep learning Python!")
            break

if __name__ == "__main__":
    main()
