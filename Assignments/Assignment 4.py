f = open("wordle.dat")
EndOfFile = False
arr = []
dateNum = []
words = []
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

try:
    while not EndOfFile:
        line = f.readline().strip()
        EndOfFile = (line == "")
        if not EndOfFile:
            arr.append(line)
    f.close()
except OSError:
    print("OSError")
except EOFError:
    print("EOFError")
    
for x in range(len(arr)):
    [monthS, day, year, word] = arr[x].split()
    monthNum = month.index(monthS) + 1
    words.append(word)

    date = int(year) * 10000 + (monthNum * 100) + int(day)
    dateNum.append(date)

print("Welcome to the Wordle Database!")
choice = input("Enter w if you are looking for a word, or d for a word on a certain date: ").upper

if choice != "D" or "W":
    print("Please enter one of the options")

if choice == "D":
    try:
        user_year = int(input("Enter the year: "))
        user_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        user_month = month.index(user_month) + 1
        user_day = int(input("Enter the day: "))

        user_date = user_year * 10000 + (user_month * 100) + user_day

        if 20210619 <= user_date <= 20240421:
            print("The word entered on", user_date, "was", words[dateNum.index(user_date)])
        elif user_date < 20210619:
            print(user_date, "is too early. No Wordles occurred before 20210619. Enter a later date.") 
        else:
            print(user_date, "is too recent. Our records only go as late as 20240421. Please enter an earlier date.") 
    except ValueError:
        print("Invalid input! Please enter numeric values for the year and day.")

if choice == "W":
    user_word = input("What word are you looking for? ").upper()
    try:
        index = words.index(user_word)
        print("The word", user_word, "was the solution to the puzzle on", dateNum[index])
    except ValueError:
        print(user_word, "was not found in the database.")





# Open the file "wordle.dat" for reading
f = open("wordle.dat")

# Initialize variables
EndOfFile = False  # Flag to check for end-of-file
arr = []  # List to store lines from the file
dateNum = []  # List to store numerical representations of dates
words = []  # List to store Wordle words

# List of month abbreviations for conversion to numeric values
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Try block to handle file reading
try:
    while not EndOfFile:  # Loop until the end of the file is reached
        line = f.readline().strip()  # Read a line and remove leading/trailing spaces
        EndOfFile = (line == "")  # Check if the line is empty (end-of-file)
        if not EndOfFile:
            arr.append(line)  # Store the line in the array if it's not empty
    f.close()  # Close the file after reading all lines
except OSError:
    print("OSError")  # Print error message if there is an issue opening or reading the file
except EOFError:
    print("EOFError")  # Print error message if the end-of-file is encountered unexpectedly

# Process each line from the file
for x in range(len(arr)):
    [monthS, day, year, word] = arr[x].split()  # Split line into components
    monthNum = month.index(monthS) + 1  # Convert month name to numeric representation
    words.append(word)  # Store the word

    # Convert the date into an integer format YYYYMMDD for easy comparison
    date = int(year) * 10000 + (monthNum * 100) + int(day)
    dateNum.append(date)  # Store the numeric date

# Display the welcome message
print("Welcome to the Wordle Database!")

# Get user choice for searching by word or date
choice = input("Enter w if you are looking for a word, or d for a word on a certain date: ").upper  # Convert to uppercase

# Validate user input
if choice != "D" or "W":
    print("Please enter one of the options")  # Prompt user to enter valid input

# If user chooses to search by date
if choice == "D":
    try:
        user_year = int(input("Enter the year: "))  # Get the year from the user
        user_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")  # Get the month
        user_month = month.index(user_month) + 1  # Convert month abbreviation to number
        user_day = int(input("Enter the day: "))  # Get the day

        # Convert input date to numeric format YYYYMMDD
        user_date = user_year * 10000 + (user_month * 100) + user_day

        # Check if the date is within the valid range
        if 20210619 <= user_date <= 20240421:
            print("The word entered on", user_date, "was", words[dateNum.index(user_date)])  # Display the word for the date
        elif user_date < 20210619:
            print(user_date, "is too early. No Wordles occurred before 20210619. Enter a later date.")  # Handle too early date
        else:
            print(user_date, "is too recent. Our records only go as late as 20240421. Please enter an earlier date.")  # Handle too recent date
    except ValueError:
        print("Invalid input! Please enter numeric values for the year and day.")  # Handle invalid input

# If user chooses to search by word
if choice == "W":
    user_word = input("What word are you looking for? ").upper()  # Get the word input from the user and convert to uppercase
    try:
        index = words.index(user_word)  # Find the word in the list
        print("The word", user_word, "was the solution to the puzzle on", dateNum[index])  # Display the corresponding date
    except ValueError:
        print(user_word, "was not found in the database.")  # Handle case where word is not found
