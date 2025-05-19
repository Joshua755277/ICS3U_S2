"""
Author : Joshua Li
Student number: 755277
Course code: ICS3U
Revision date : May 19, 2025
Program : Wordle Database Search
Description : A program that accesses a Wordle solution file, allowing users to 
              look up solutions by date or determine when a specific word was featured.

VARIABLE DICTIONARY :
  arr (list) = Stores lines read from the Wordle solution file
  dateNum (list) = Stores all dates in integer YYYYMMDD format
  words (list) = Stores all the words from the file
  month (list) = Contains month abbreviations used to convert month names to numbers
  f (file) = Used to open and read the wordle.dat file
  EndOfFile (bool) = Flags whether the end of the file has been reached
  line (str) = Temporarily stores a line read from the file before processing
  monthS (str) = Stores the month abbreviation extracted from a line of the file
  day (str) = Stores the day extracted from a line of the file
  year (str) = Stores the year extracted from a line of the file
  word (str) = Stores the Wordle solution word extracted from a line of the file
  monthNum (int) = Stores the numerical representation of a month
  date (int) = Stores a date converted into YYYYMMDD format
  choice (str) = Stores the user input for selecting either word or date search
  user_year (int) = Stores the year input by the user when searching by date
  user_month (int) = Stores the month input by the user when searching by date
  user_day (int) = Stores the day input by the user when searching by date
  user_date (int) = Stores the date input by the user when searching for a date
  user_word (str) = Stores the word entered by the user when searching for a word
"""

# Creates array to store lines from the file
arr = []  
# Creates array to store numerical representations of dates
dateNum = []  
# Creates array to store Wordle words
words = []  

# List of month abbreviations for conversion to numerical value
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Tries to read file and catches error
try:
    # Open the file "wordle.dat" for reading
    f = open("wordle.dat", "r")
    # Flag to check for end-of-file
    EndOfFile = False  
    # Loop until the end of the file is reached
    while not EndOfFile:
        # Reads a line and remove leading/trailing spaces
        line = f.readline().strip()  
        # Check if the next line is empty
        EndOfFile = (line == "")  
        if not EndOfFile:
            # Store the line in the array if it's not empty
            arr.append(line)  
    # Close the file after reading all lines
    f.close()  
except OSError:
    # Print error message if there is an issue opening or reading the file
    print("OSError")  
except EOFError:
    # Print error message if the end of file is unexpectedly reached
    print("EOFError")  

# Cycles through each line from the file
for x in range(len(arr)):
    # Splits each line into monthS, day, year, and word
    [monthS, day, year, word] = arr[x].split()  
    # Converts month name to numerical value
    monthNum = month.index(monthS) + 1  
    # Stores the word in words array
    words.append(word) 

    # Convert the date into an integer format YYYYMMDD
    date = int(year) * 10000 + (monthNum * 100) + int(day)
    # Stores the numerical date in dateNum array
    dateNum.append(date)  

# Prints welcome message
print("Welcome to the Wordle Database!")

# Get user choice for searching by word or date and also converets to uppercase
choice = input("Enter w if you are looking for a word, or d for a word on a certain date: ").upper()

# Makes sure user input is valid
if choice != "D" and choice != "W":
    # Asks for user input
    print("Please enter one of the options")  

# If user chooses to search by date
if choice == "D":
    # Makes sure user input is valid
    try:
        # Gets the year from the user
        user_year = int(input("Enter the year: ")) 
        # Gets the month from the user
        user_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ") 
        # Converts month abbreviation to number
        user_month = month.index(user_month.capitalize()) + 1  
        # Get the day
        user_day = int(input("Enter the day: ")) 

        # Convert input date to numeric format YYYYMMDD
        user_date = user_year * 10000 + (user_month * 100) + user_day

        # Check if the date is within the valid range
        if 20210619 <= user_date <= 20240421:
            # Display the word for the date entered by the user
            print("The word entered on", user_date, "was", words[dateNum.index(user_date)])  
        elif user_date < 20210619:
            # Runs if user inputs a date too late
            print(user_date, "is too early. No Wordles occurred before 20210619. Enter a later date.")  
        else:
            # Runs if user inputs a date too early
            print(user_date, "is too recent. Our records only go as late as 20240421. Please enter an earlier date.") 
    except ValueError:
        # Handles invalid input
        print("Invalid input. Please enter numeric values for the year and day.")  

# If user chooses to search by word
if choice == "W":
    # Get the word input from the user and convert to uppercase
    user_word = input("What word are you looking for? ").upper()  
    try:
        # Display the corresponding date
        print("The word", user_word, "was the solution to the puzzle on", dateNum[words.index(user_word)])  
    except ValueError:
        # Handle case where word is not found
        print(user_word, "was not found in the database.")  
