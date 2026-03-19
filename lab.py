#swap two numbers
"""
a = input("enter first number:")
b = input("enter the second value:")

temp = a
a = b
b = temp

print("a =", a, "b =", b)
"""

#sum of n natural number
"""

n = int(input("Enter a positive integer: "))


sum_n = n * (n + 1) // 2


print(f"The sum of first {n} natural numbers is: {sum_n}")
"""

#wap to print truth table for bitwise operator

# Truth table for bitwise operators AND, OR, XOR
"""
print("A B | A&B A|B A^B")
print("-------------------")

for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} {b} |  {a & b}   {a | b}   {a ^ b}")

"""
#wap to print left shift and right shift of the number
"""
num = int(input("Enter a number: "))
shift = int(input("Enter how many positions to shift: "))


left_shift = num << shift   
right_shift = num >> shift 


print(f"Original number: {num}")
print(f"Left shift ({num} << {shift}) = {left_shift}")
print(f"Right shift ({num} >> {shift}) = {right_shift}")
"""

#using membership operator find whether a given number is in sequence(10,20,56,78,89)
"""
sequence = (10, 20, 56, 78, 89)


num = int(input("Enter a number: "))

if num in sequence:
    print(f"{num} is present in the sequence {sequence}")
else:
    print(f"{num} is NOT present in the sequence {sequence}")
"""

                                                            ## experiment-----2 ##


#Check whether the given number is divisible by 3 and 5 both

"""
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")
    """

#Check whether a given number is multiple of five or not.

"""num = int(input("Enter a number: "))

if num % 5 == 0:
    print(f"{num} is a multiple of 5.")
else:
    print(f"{num} is not a multiple of 5.")
"""

#Find the greatest among the two numbers. If numbers are equal than print “numbers are equal”.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
else:
    print("Numbers are equal.")
    """

#Find the greatest among three numbers assuming no two values are same.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest.")
else:
    print(f"{num3} is the greatest.")
"""

#Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
"""
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and distinct.")
    print(f"Root1 = {root1}, Root2 = {root2}")
elif D == 0:
    root = -b / (2*a)
    print("Roots are real and equal.")
    print(f"Root = {root}")
else:
    realPart = -b / (2*a)
    imagPart = math.sqrt(-D) / (2*a)
    print("Roots are imaginary (complex).")
    print(f"Root1 = {realPart} + {imagPart}i")
    print(f"Root2 = {realPart} - {imagPart}i")
    """

#Find whether a given year is a leap year or not.
"""
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    """

#Write a program which takes any date as input and display next date of the calendar
#I/P: day=20 month=9 year=2005
#O/P: day=21 month=9 year 2005
"""
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))


is_leap = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

if is_leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


days_in_month = [31, 29 if is_leap else 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]


if day < days_in_month[month - 1]:
    next_day = day + 1
    next_month = month
    next_year = year
else:
    next_day = 1
    if month == 12:  
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

print(f"Next date is: day={next_day} month={next_month} year={next_year}")
"""
#Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
"""
def get_grade(cgpa):
    if 0 <= cgpa <= 3.4:
        return "F"
    elif 3.5 <= cgpa <= 5.0:
        return "C+"
    elif 5.1 <= cgpa <= 6.0:
        return "B"
    elif 6.1 <= cgpa <= 7.0:
        return "B+"
    elif 7.1 <= cgpa <= 8.0:
        return "A"
    elif 8.1 <= cgpa <= 9.0:
        return "A+"
    elif 9.1 <= cgpa <= 10.0:
        return "O (Outstanding)"
    else:
        return "Invalid CGPA"

name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
sapid = input("Enter SAPID: ")
sem = input("Enter semester: ")
course = input("Enter course: ")

subjects = ["Maths", "Python", "Chemistry", "English", "Physics"]
marks = []

for subject in subjects:
    m = int(input(f"Enter marks for {subject}: "))
    marks.append(m)

total_marks = sum(marks)
percentage = total_marks / (len(subjects) * 100) * 100
cgpa = percentage / 10
grade = get_grade(cgpa)

print("\n------ Grade Sheet ------")
print(f"Name: {name}")
print(f"Roll Number: {roll_number} SAPID: {sapid}")
print(f"Sem: {sem} Course: {course}")
print("Subject name: Marks")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]}")
print(f"Percentage: {percentage:.2f}%")
print(f"CGPA: {cgpa:.1f}")
print(f"Grade: {grade}")
"""
                                                              ## classwork ##

#1take two numbers from users, print the sum, product and check whether the product is even or odd
"""
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

sum = num1 + num2

product = num1 * num2

print("sum is: " , sum)
if(sum%2==0):
    print("sum is even")
else:
    print("sum is odd")
print("product is:" , product)

if(product%2==0):
    print(" product is even")
else:
    print("product is odd")
    

"""
#2take string input from user and remove leading abd trailing space and turn to uppercase without using .upper



#3take variable name as input print whether it is a valid python identifier
"""
var_name = input("Enter a variable name: ")

if var_name.isidentifier():
    print(f"'{var_name}' is a valid Python identifier.")
else:
    print(f"'{var_name}' is NOT a valid Python identifier.")
    """
#4create list and an integer wap that passes both to a function modifies the list inside the function and integer inside the function

#5wap that takes marks as input and print distinction if marks>=75 ,1 if marks>=60,pass if marks>=40 and fails others
"""
marks = int(input("Enter marks: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("1st Division")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
"""
#6wap to print
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
"""
n = 5  

for i in range(1, n+1):       
    for j in range(1, i+1):   
        print(j, end=" ")
    print()

    """

                                                            ## experiment-----3 ##

 # Find a factorial of given number.
"""
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

"""


#Find whether the given number is Armstrong number.
"""
def is_armstrong(num):
   
    digits = str(num)
    power = len(digits)
    
    total = sum(int(digit) ** power for digit in digits)
    
    return total == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
"""

#Print Fibonacci series up to given term.
"""
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci series up to {num_terms} terms:")
print(fibonacci_series(num_terms))
"""

#Write a program to find if given number is prime number or not.
"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
"""

#Check whether given number is palindrome or not.
"""
def is_palindrome(num):
    
    str_num = str(num)
  
    return str_num == str_num[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
    
"""
#Write a program to print sum of digits.
"""
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10   
        total += digit     
        num //= 10         
    return total

num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum_of_digits(num)}")
"""

#Count and print all numbers divisible by 5 or 7 between 1 to 100.
"""
def divisible_by_5_or_7():
    numbers = []
    for i in range(1, 101):
        if i % 5 == 0 or i % 7 == 0:
            numbers.append(i)
    return numbers

nums = divisible_by_5_or_7()
print("Numbers divisible by 5 or 7 between 1 and 100:")
print(nums)
print(f"Total count = {len(nums)}")
"""

#Convert all lower cases to upper case in a string.
"""
def to_uppercase(string):
    return string.upper()

text = input("Enter a string: ")
print("Uppercase string:", to_uppercase(text))
"""

#Print the table for a given number:
"""5 * 1 = 5
5 * 2 = 10……….."""
"""
def print_table(num):
    for i in range(1, 11):  
        print(f"{num} * {i} = {num * i}")

num = int(input("Enter a number: "))
print_table(num)
"""

#Write a program to print the following pattern
"""
123454321
1234 *4321
123 * * 321
12 * * * 21
1 * * * * 1
"""
"""
n = 5
for i in range(1, n + 1):
    
    for j in range(1, n - i + 2):
        print(j, end="")

    for j in range(1, i):
        print("**", end="") 

    for j in range(n - i + 1, 0, -1):

        if i == 1 and j == n:
            continue
        print(j, end="")

    print()
"""
#Write a program to print the sum of the following series
"""
1+ ½ + 1/3 + ¼ +….+1/n
"""
"""
n = int(input("Enter the value of n: "))
sum_series = 0.0

for i in range(1, n + 1):
    sum_series += 1 / i

print("Sum of the series up to 1/{} is: {:.6f}".format(n, sum_series))
"""

                                                                 ## experiment-----4 ##

#Write a program to count and display the number of capital letters in a given string

"""
def count_capitals(text):
    count = 0
    for char in text:
        if char.isupper(): 
            count += 1
    return count

string = input("Enter a string: ")
capital_count = count_capitals(string)

print("Number of capital letters:", capital_count)
"""

#Count total number of vowels in a given string.
"""
def count_vowels(text):
    vowels = "aeiouAEIOU" 
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
vowel_count = count_vowels(string)

print("Total number of vowels:", vowel_count)
"""

#Input a sentence and print words in separate lines.
"""
sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    print(word)
"""

#WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
"""
Sample Input
ABCDCDC
CDC
Sample Output
2
"""
"""
def count_substring(string, sub):
    count = 0
    sub_len = len(sub)
    
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == sub:
            count += 1
    return count

string = input("Enter the main string: ")
sub = input("Enter the substring: ")

result = count_substring(string, sub)
print("Number of occurrences:", result)
"""

#Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
"""
Sample Input
ABaBCbGc
Sample Output
2A
3B
2C
1G
"""
"""
def count_alphabets(text):
    text = text.upper()
    
    freq = {}
    
    for char in text:
        if char.isalpha(): 
            freq[char] = freq.get(char, 0) + 1
  
    for key in sorted(freq.keys()):
        print(f"{freq[key]}{key}")

string = input("Enter a string: ")
count_alphabets(string)
"""

#Program to count number of unique words in a given sentence using sets.
"""
def count_unique_words(sentence):

    words = sentence.split()
    
    unique_words = set(words)
    
    print("Unique words:")
    for word in unique_words:
        print(word)
   
    print("Total number of unique words:", len(unique_words))

sentence = input("Enter a sentence: ")
count_unique_words(sentence)
"""

#Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
"""a)Fruits which are in both sets s1 and s2
b)Fruits only in s1 but not in s2
c)Count of all fruits from s1 and s2
"""
"""
n = int(input("Enter number of fruits in each set: "))

print("\nEnter fruits for Set s1:")
s1 = set()
for i in range(n):
    fruit = input(f"Fruit {i+1}: ").strip()
    s1.add(fruit)

print("\nEnter fruits for Set s2:")
s2 = set()
for i in range(n):
    fruit = input(f"Fruit {i+1}: ").strip()
    s2.add(fruit)

common_fruits = s1.intersection(s2)

only_in_s1 = s1.difference(s2)

all_fruits_count = len(s1.union(s2))

print("\nResults:")
print("a) Fruits in both sets:", common_fruits if common_fruits else "None")
print("b) Fruits only in s1:", only_in_s1 if only_in_s1 else "None")
print("c) Count of all unique fruits from s1 and s2:", all_fruits_count)
"""

#Take two sets and apply various set operations on them :
"""S1 = {Red ,yellow, orange , blue }
S2 = {violet, blue , purple}"""
"""
S1 = {"Red", "Yellow", "Orange", "Blue"}
S2 = {"Violet", "Blue", "Purple"}

union_set = S1.union(S2)

intersection_set = S1.intersection(S2)


diff_s1_s2 = S1.difference(S2)  
diff_s2_s1 = S2.difference(S1)   

symmetric_diff = S1.symmetric_difference(S2)


print("S1 =", S1)
print("S2 =", S2)
print("\nUnion (S1 ∪ S2):", union_set)
print("Intersection (S1 ∩ S2):", intersection_set)
print("Difference (S1 - S2):", diff_s1_s2)
print("Difference (S2 - S1):", diff_s2_s1)
print("Symmetric Difference (S1 △ S2):", symmetric_diff)
"""


                                                            ## experiment------5 ##

#Scan n values in range 0-3 and print the number of times each value has occurred.
"""
n = int(input("How many numbers? "))
count = [0, 0, 0, 0]   

for i in range(n):
    x = int(input(f"Enter number {i+1} (0-3): "))
    if 0 <= x <= 3:
        count[x] += 1
    else:
        print("Warning: Value should be 0-3 (ignored)")

print("\nResult:")
print("0 appears", count[0], "times")
print("1 appears", count[1], "times")
print("2 appears", count[2], "times")
print("3 appears", count[3], "times")
"""

#Create a tuple to store n numeric values and find average of all values.
"""
n = int(input("Enter how many values you want: "))

values_list = []

print("Enter", n, "numeric values:")
for i in range(n):
    num = float(input())   
    values_list.append(num)

values_tuple = tuple(values_list)

if n>0:
     average = sum(values_tuple) / len(values_tuple)

     print("Tuple is:", values_tuple)
     print("Average is:", average)

else:
    print("no values added")
   """

#WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.
"""Sample Input
N = 5
Scores= 2 3 6 6 5
Sample output
5
Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
"""
"""
n = int(input("Enter number of students: "))
scores = []

print("Enter", n, "scores:")
for i in range(n):
    s = int(input())
    scores.append(s)

max_score = max(scores)

while max_score in scores:
    scores.remove(max_score)

if len(scores) > 0:
    runner_up = max(scores)
    print("Runner-up score:", runner_up)
else:
    print("No runner-up exists")
"""

#Create a dictionary of n persons where key is name and value is city.
"""
a) Display all names
b) Display all city names
c) Display student name and city of all students.
d) Count number of students in each city.
"""
"""
n = int(input("Enter number of persons: "))
students = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    students[name] = city

print("\nAll names:")
for name in students.keys():
    print(name)

print("\nAll cities:")
for city in students.values():
    print(city)

print("\nName and city of all students:")
for name, city in students.items():
    print(name, "->", city)

city_count = {}
for city in students.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print("\nNumber of students in each city:")
for city, count in city_count.items():
    print(city, ":", count)
"""

#Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name, year, director name, production cost, collection made (earning) & perform the following :-
"""
a)print all movie details
b)display name of movies released before 2015
c)print movies that made a profit.
d)print movies directed by a particular director.
"""
"""
n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    name = input("\nEnter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    cost = float(input("Enter production cost: "))
    earning = float(input("Enter collection made: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "earning": earning
    }

print("\nAll movie details:")
for name, details in movies.items():
    print(name, ":", details)

print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("\nMovies that made a profit:")
for name, details in movies.items():
    if details["earning"] > details["cost"]:
        print(name)

search_director = input("\nEnter director name to search: ")
print("Movies directed by", search_director, ":")
for name, details in movies.items():
    if details["director"].lower() == search_director.lower():
        print(name)
        """

#Create a contact book where users can store, search, update, and delete contacts. Use dictionary for storing contacts.
"""
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Number of", name, "is", contacts[name])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        number = input("Enter new number: ")
        contacts[name] = number
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def show_all_contacts():
    if contacts:
        print("\nAll Contacts:")
        for name, number in contacts.items():
            print(name, "->", number)
    else:
        print("No contacts available.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        show_all_contacts()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
"""

#Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks.
"""
todo = []
def add_task():
    task = input("Enter a new task: ")
    todo.append(task)
    print("Task added successfully!")

def view_tasks():
    if todo:
        print("\nYour Todo List:")
        for i, task in enumerate(todo, start=1):
            print(i, ".", task)
    else:
        print("No tasks in the list.")

def remove_task():
    view_tasks()
    if todo:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(todo):
            removed = todo.pop(num - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number.")

while True:
    print("\n--- Todo List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting Todo List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")"""


                                                         #--------logo copy---------#

"""src = "logo.png"
dst = "logo_copy.png"

with open(src, "rb") as rf, open(dst, "wb") as wf:
    header = rf.read(8)
    print(f"PNG Header: {header}")
    rf.seek(8)
    wf.write(rf.read())
    print("image copied successfully.")
"""

                                                     #------------experiment-6----------#


#1.Write a Python function to find the maximum and minimum numbers from a sequence of numbers. (Note: Do not use built-in functions.)
"""
def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum
sequence = []

n = int(input("Enter how many numbers you want: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    sequence.append(num)

max_val, min_val = find_max_min(sequence)

print("Maximum:", max_val)
print("Minimum:", min_val)
"""

#2.Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
"""
def sum_of_cubes(n):
    total = 0

    for i in range(1, n):
        total += i**3
    
    return total
num = int(input("Enter a positive integer: "))
result = sum_of_cubes(num)
print(f"Sum of cubes of numbers smaller than {num} is: {result}")
"""

#3.Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
"""
def print_numbers(n):
    if n == 0:
        return
  
    print_numbers(n - 1)
  
    print(n)

num = int(input("Enter a positive integer: "))
print_numbers(num)
"""

#4.Write a recursive function to print Fibonacci series upto n terms.
"""
def fibonacci(n, a=0, b=1, count=0):

    if count == n:
        return
    
    print(a, end=" ")
   
    fibonacci(n, b, a+b, count+1)

num = int(input("Enter how many terms you want in Fibonacci series: "))
print(f"Fibonacci series up to {num} terms:")
fibonacci(num)
"""

#5.Write a lambda function to find volume of cone.
"""
import math

volume_cone = lambda r, h: (1/3) * math.pi * (r**2) * h
 
radius = float(input("Enter radius of the cone: "))
height = float(input("Enter height of the cone: "))

print("Volume of cone:", volume_cone(radius, height))
"""

#6.Write a lambda function which gives tuple of max and min from a list.
"""Sample input: [10, 6, 8, 90, 12, 56]
Sample output: (90,6)"""

"""get_max_min = lambda lst: (max(lst), min(lst))

numbers = [10, 6, 8, 90, 12, 56]

print(get_max_min(numbers)) 
"""

#7.Write functions to explain mentioned concepts:
"""
a.Keywordargument
b.Default argument
c.Variable length argument
"""
"""
def student_info(name, age=18, *subjects):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print("Subjects enrolled:", subjects)

student_info("Deepanshi", 22, "Math", "Science")

student_info("Rahul", "English", "History")

student_info("Anita", 20, "Physics", "Chemistry", "Biology")
"""
#8.Write a program to check whether all the values in a dictionary are same or not using lambda function.
"""
all_values_same = lambda d: len(set(d.values())) == 1


data1 = {"a": 10, "b": 10, "c": 10}
data2 = {"x": 5, "y": 7, "z": 5}
data3 = {"p": "yes", "q": "yes", "r": "yes"}


print("data1:", all_values_same(data1))  
print("data2:", all_values_same(data2)) 
print("data3:", all_values_same(data3)) 
"""

#9.Write a program to create two lists and generate a dictionary with keys from list1 and values from list2.

list1 = ["a", "b", "c", "d"]
list2 = [10, 20, 30, 40]


my_dict = dict(zip(list1, list2))


print("List1:", list1)
print("List2:", list2)
print("Generated Dictionary:", my_dict)

