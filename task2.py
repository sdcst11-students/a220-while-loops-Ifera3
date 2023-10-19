#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted

"""
x = 0

while x < 2:
    x = 0
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin":
        x = x + 1
    if password == "12345":
        x = x + 1
    if x < 2:
        print("Access denied")
print("Access granted")