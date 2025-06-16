"""
Author : Joshua Li
Student Number: 755277
Revision Date : 6/13/2025
Program : Credit Card Expiry and Validation Report
Description : Reads credit card data from a file, sorts by expiry date, validates card numbers using 
              the Luhn algorithm, and outputs status to both the screen and an output file.

VARIABLE DICTIONARY :
    arr (list) - Stores all lines read from the input file (excluding the header)
    FullName (list) - Stores full names (first and last) of all cardholders
    CCTypes (list) - Stores the type of each credit card (e.g., VISA, Mastercard)
    CCNumbers (list) - Stores the credit card numbers as strings
    Expiry_Dates (list) - Stores expiry dates in the format YYYYMM as integers
    output_file_name (str) - Name of the output file where the report is written
    output_file (file object) - File handle used to write the output report
    first_line (str) - Header line from the input file (removed before processing)
    f (file object) - File handle used to read from the input file
    line (str) - Temporarily stores each line read from the input file
    EndOfFile (bool) - Boolean flag to check for end-of-file during reading
    x (str) - Temporarily stores each credit card entry from the input list during processing
    GivenName (str) - First name of a cardholder (extracted from input line)
    Surname (str) - Last name of a cardholder (extracted from input line)
    CCType (str) - Type of the credit card (extracted from input line)
    CCNumber (str) - Credit card number (extracted from input line)
    Exp_Mo (str) - Expiry month of the card, possibly padded to 2 digits
    Exp_Yr (str) - Expiry year of the card
    Name (str) - Concatenated full name of the cardholder
    Expiry_Date (str/int) - Concatenated and converted YYYYMM expiry date
    Expired_Text (str) - Stores either "EXPIRED" or "RENEW IMMEDIATELY" depending on date
    validity (str) - Stores "VALID" or "INVALID" based on result of Luhn validation
"""

arr = []
# Stores all lines read from the input file (excluding the header)
FullName = []
# Stores full names of all cardholders
CCTypes = []
# Stores the type of each credit card (e.g., VISA, Mastercard)
CCNumbers = []
# Stores the credit card numbers as strings
Expiry_Dates = []
# Stores expiry dates in the format YYYYMM as integers

"""
Function to reverse a given string.
Parameters:
    s (str): The input string to be reversed.
    reversed_str (str): Stores the reversed version of the input string, built character by character.
    char (str): The current character from the input string during iteration.
"""

def reverse_string(s):
  # Defines function
    reversed_str = ""
    # Stores the reversed version of the input string
    for char in s:
        reversed_str = char + reversed_str
        # Builds reversed string by prepending each character
    return reversed_str
    # Returns the final reversed string
  
"""
Function to validate a number using the Luhn algorithm.
Parameters:
    N (str): A string of digits representing the number to validate.
    total (int): Accumulates the total sum used to determine if the number is valid.
    digit (int): The numeric value of the current digit being processed.
    doubled (int): The result of doubling every second digit from the right (with adjustment if > 9).
"""

def validate(N):
  # Defines function
    N = reverse_string(N)
    # Reverse number for processing
    total = 0
    # Accumulates the total sum used to determine validity
    for i in range(len(N)):
        digit = int(N[i])
        # Convert character to integer
        if i % 2 == 1:
            doubled = digit * 2
            # Double every second digit
            if doubled > 9:
                doubled -= 9
                # Subtract 9 if doubled value is greater than 9
            total += doubled
            # Add adjusted value
        else:
            total += digit
            # Add non-doubled digit
    return total % 10 == 0
    # Returns True if the total is divisible by 10

"""
Function to perform merge sort on multiple parallel arrays.
Parameters:
    arr (list): Primary array used for sorting
    arr2 (list): Parallel array to be reordered based on arr's sorting 
    arr3 (list): Parallel array to be reordered based on arr's sorting 
    arr4 (list): Parallel array to be reordered based on arr's sorting 
    l (int): Left index of the subarray to sort.
    r (int): Right index of the subarray to sort.
    m (int): Middle index used to divide the array into two halves for recursive sorting.
"""

def mergeSort(arr, arr2, arr3, arr4, l, r):
  # Defines function
    if l < r:
        m = l + (r - l) // 2
        # Calculate the middle index
        mergeSort(arr, arr2, arr3, arr4, l, m)
        # Recursively sort left half
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        # Recursively sort right half
        merge(arr, arr2, arr3, arr4, l, m, r)
        # Merge sorted halves

"""
Function to merge two sorted subarrays of multiple parallel arrays.
Parameters:
    arr (list): Primary array to be merged.
    arr2 (list): Parallel array corresponding to arr.
    arr3 (list): Parallel array corresponding to arr.
    arr4 (list): Parallel array corresponding to arr.
    l (int): Left index of the subarray.
    m (int): Middle index, dividing the two subarrays.
    r (int): Right index of the subarray.
    n1 (int): Number of elements in the left subarray.
    n2 (int): Number of elements in the right subarray.
    L, L2, L3, L4 (list): Temporary arrays holding the left halves of arr, arr2, arr3, arr4.
    R, R2, R3, R4 (list): Temporary arrays holding the right halves of arr, arr2, arr3, arr4.
    i (int): Index for traversing the left subarrays.
    j (int): Index for traversing the right subarrays.
    k (int): Index for placing merged elements back into the original arrays.
"""

def merge(arr, arr2, arr3, arr4, l, m, r):
  # Defines function
    n1 = m - l + 1
    n2 = r - m
    # Create temp arrays
    L = [0] * (n1)
    L2 = [0] * (n1)
    L3 = [0] * (n1)
    L4 = [0] * (n1)
    # Temporary arrays for left half
    R = [0] * (n2)
    R2 = [0] * (n2)
    R3 = [0] * (n2)
    R4 = [0] * (n2)
    # Temporary arrays for left right
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]
        # Copy right half into temporary arrays
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]
        # Copy right half into temporary arrays
    i = 0  
    j = 0  
    k = l  
    # Initialize index pointers
  
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            # Copy from left array if smaller
            i += 1
            # Move left index forward
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            # Copy from right array if smaller
            j += 1
            # Move right index forward
        k += 1
      # Move merged index forward
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        # Copy remaining elements from left array
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        # Copy remaining elements from right array
        j += 1
        k += 1

try:
    f = open("data.dat", "r")
    # Open input file for reading
    EndOfFile = False
    # Flag to track file end
    while not EndOfFile:
        line = f.readline().strip()
        # Read and clean next line
        EndOfFile = (line == "")
        # Check for empty line (end of file)
        if not EndOfFile:
            arr.append(line)
            # Add line to data list
    f.close()
    # Close the file
except OSError:
    print("OSError")
    # Handle file error
except EOFError:
    print("EOFError")
    # Handle end-of-file error
first_line = arr.remove(arr[0])
# Remove header line from data

for x in arr:
    GivenName, Surname, CCType, CCNumber, Exp_Mo, Exp_Yr = x.strip().split(',')
    # Split line into data fields
    Name = GivenName + ' ' + Surname
    # Concatenate first and last name
    FullName.append(Name)
    # Store full name
    CCTypes.append(CCType)
    # Store card type
    CCNumbers.append(CCNumber)
    # Store card number
  
    if len(Exp_Mo) == 1:
        Exp_Mo = '0' + Exp_Mo
        # Ensure expiry month is two digits
    Expiry_Date = Exp_Yr + Exp_Mo
    # Combine year and month
    Expiry_Dates.append(int(Expiry_Date))
    # Convert expiry date to integer and store

mergeSort(Expiry_Dates, FullName, CCNumbers, CCTypes, 0, len(Expiry_Dates) - 1)
# Sort all data by expiry date
output_file_name = "output.txt"
# Define output file name
output_file = open(output_file_name, "w")
# Open output file for writing

for i in range(len(Expiry_Dates)):
    if Expiry_Dates[i] > 202506:
        continue
        # Stop processing if expiry date is beyond January 2025
    if Expiry_Dates[i] == 202506:
        Expired_Text = "RENEW IMMEDIATELY"
        # Set renewal message for January 2025
    elif Expiry_Dates[i] < 202506:
        Expired_Text = "EXPIRED"
        # Mark cards with past expiry as expired
    validity = "VALID" if validate(CCNumbers[i]) else "INVALID"
    # Validate card number using Luhn algorithm
    print("%-37s %-15s %-20s %-10s %-25s" % (FullName[i] + ':', CCTypes[i], '#' + CCNumbers[i], Expiry_Dates[i], Expired_Text + " | " + validity))
    # Print formatted output
