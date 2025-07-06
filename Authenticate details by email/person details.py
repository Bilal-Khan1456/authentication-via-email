
# users_data = [
#     {"name": "Ali", "email": "ali@example.com", "password": "alice123", "age": 25},
#     {"name": "Babar", "email": "babar@example.com", "password": "babar123", "age": 30},
#     {"name": "Hamza", "email": "hamza@example.com", "password": "hamza123", "age": 22},
#     {"name": "Dawood", "email": "dawood@example.com", "password": "dawood123", "age": 28},
#     {"name": "Bilal", "email": "bilal@example.com", "password": "bilal123", "age": 24},
#     {"name": "Faheem", "email": "faheem@example.com", "password": "faheem123", "age": 35},
#     {"name": "Jawad", "email": "jawad@example.com", "password": "jawad123", "age": 26},
#     {"name": "Ismail", "email": "ismail@example.com", "password": "ismail123", "age": 27},
#     {"name": "Moiz", "email": "moiz@example.com", "password": "moiz123", "age": 29},
#     {"name": "Fahad", "email": "fahad@example.com", "password": "fahad123", "age": 31}
# ]


# def find_user_by_email(data, email):
#     for user in data:
#         if user["email"] == email:
#             return user
#     return None

# def authenticate_user(data):
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
    
#     user = find_user_by_email(data, email)
#     if user:
#         if user["password"] == password:
#             print("\n User authenticated successfully!\n")
#             print("User Details:")
#             print(f"Name : {user['name']}")
#             print(f"Email: {user['email']}")
#             print(f"Age  : {user['age']}")
#         else:
#             print("\n Password is incorrect.")
#     else:
#         print("\n User not found.")


# authenticate_user(users_data)


# # use functions but not use loops here



# users_data = [
#     {"name": "Ali", "email": "ali@example.com", "password": "alice123", "age": 25},
#     {"name": "Babar", "email": "babar@example.com", "password": "babar123", "age": 30},
#     {"name": "Hamza", "email": "hamza@example.com", "password": "hamza123", "age": 22},
#     {"name": "Dawood", "email": "dawood@example.com", "password": "dawood123", "age": 28},
#     {"name": "Bilal", "email": "bilal@example.com", "password": "bilal123", "age": 24},
#     {"name": "Faheem", "email": "faheem@example.com", "password": "faheem123", "age": 35},
#     {"name": "Jawad", "email": "jawad@example.com", "password": "jawad123", "age": 26},
#     {"name": "Ismail", "email": "ismail@example.com", "password": "ismail123", "age": 27},
#     {"name": "Moiz", "email": "moiz@example.com", "password": "moiz123", "age": 29},
#     {"name": "Fahad", "email": "fahad@example.com", "password": "fahad123", "age": 31}
# ]


# def find_user_by_email(data, email):
#     if data[0]["email"] == email:
#         print(data[0])
#         return data[0]
        
#     elif data[1]["email"] == email:
#         return data[1]
#     elif data[2]["email"] == email:
#         return data[2]
#     elif data[3]["email"] == email:
#         return data[3]
#     elif data[4]["email"] == email:
#         return data[4]
#     elif data[5]["email"] == email:
#         return data[5]
#     elif data[6]["email"] == email:
#         return data[6]
#     elif data[7]["email"] == email:
#         return data[7]
#     elif data[8]["email"] == email:
#         return data[8]
#     elif data[9]["email"] == email:
#         return data[9]
#     else:
#         return None

# def authenticate_user(data):
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")

#     user = find_user_by_email(data, email)

#     if user:
#         if user["password"] == password:
#             print("\n User authenticated successfully!\n")
#             print("User Details:")
#             print(f"Name : {user['name']}")
#             print(f"Email: {user['email']}")
#             print(f"Age  : {user['age']}")
#         else:
#             print("\n Password is incorrect.")
#     else:
#         print("\n User not found.")


# authenticate_user(users_data)


# # without function

# users_data = [
#     {"name": "Ali", "email": "ali@example.com", "password": "alice123", "age": 25},
#     {"name": "Babar", "email": "babar@example.com", "password": "babar123", "age": 30},
#     {"name": "Hamza", "email": "hamza@example.com", "password": "hamza123", "age": 22},
#     {"name": "Dawood", "email": "dawood@example.com", "password": "dawood123", "age": 28},
#     {"name": "Bilal", "email": "bilal@example.com", "password": "bilal123", "age": 24},
#     {"name": "Faheem", "email": "faheem@example.com", "password": "faheem123", "age": 35},
#     {"name": "Jawad", "email": "jawad@example.com", "password": "jawad123", "age": 26},
#     {"name": "Ismail", "email": "ismail@example.com", "password": "ismail123", "age": 27},
#     {"name": "Moiz", "email": "moiz@example.com", "password": "moiz123", "age": 29},
#     {"name": "Fahad", "email": "fahad@example.com", "password": "fahad123", "age": 31}
# ]

# # Take input from user
# email_input = input("Enter your email: ")
# password_input = input("Enter your password: ")

# # Initialize a flag to track if user is found
# user_found = False

# # Loop through the data to search for the user
# for user in users_data:
#     if user["email"] == email_input:
#         user_found = True
#         if user["password"] == password_input:
#             print("\nUser authenticated successfully!\n")
#             print("User Details:")
#             print(f"Name : {user['name']}")
#             print(f"Email: {user['email']}")
#             print(f"Age  : {user['age']}")
#         else:
#             print("\nPassword is incorrect.")
#         break

# # If no user found after loop
# if not user_found:
#     print("\nUser not found.")
# # without loops
# # Store 10 user's data in a list of dictionaries
# users_data = [
#     {"name": "Ali", "email": "ali@example.com", "password": "alice123", "age": 25},
#     {"name": "Babar", "email": "babar@example.com", "password": "babar123", "age": 30},
#     {"name": "Hamza", "email": "hamza@example.com", "password": "hamza123", "age": 22},
#     {"name": "Dawood", "email": "dawood@example.com", "password": "dawood123", "age": 28},
#     {"name": "Bilal", "email": "bilal@example.com", "password": "bilal123", "age": 24},
#     {"name": "Faheem", "email": "faheem@example.com", "password": "faheem123", "age": 35},
#     {"name": "Jawad", "email": "jawad@example.com", "password": "jawad123", "age": 26},
#     {"name": "Ismail", "email": "ismail@example.com", "password": "ismail123", "age": 27},
#     {"name": "Moiz", "email": "moiz@example.com", "password": "moiz123", "age": 29},
#     {"name": "Fahad", "email": "fahad@example.com", "password": "fahad123", "age": 31}
# ]

# # Take input
# email = input("Enter your email: ")
# password = input("Enter your password: ")

# # Manually checking each user without loops
# if users_data[0]["email"] == email:
#     user = users_data[0]
# elif users_data[1]["email"] == email:
#     user = users_data[1]
# elif users_data[2]["email"] == email:
#     user = users_data[2]
# elif users_data[3]["email"] == email:
#     user = users_data[3]
# elif users_data[4]["email"] == email:
#     user = users_data[4]
# elif users_data[5]["email"] == email:
#     user = users_data[5]
# elif users_data[6]["email"] == email:
#     user = users_data[6]
# elif users_data[7]["email"] == email:
#     user = users_data[7]
# elif users_data[8]["email"] == email:
#     user = users_data[8]
# elif users_data[9]["email"] == email:
#     user = users_data[9]
# else:
#     user = None

# # Authentication logic
# if user:
#     if user["password"] == password:
#         print("\nUser authenticated successfully!\n")
#         print("User Details:")
#         print(f"Name : {user['name']}")
#         print(f"Email: {user['email']}")
#         print(f"Age  : {user['age']}")
#     else:
#         print("\nPassword is incorrect.")
# else:
#     print("\nUser not found.")
try:
    def area(length,width):
        
        sum=length*width
        return sum

    def volume(length,width,height):
        
        sum=length*width*height
        return sum

    print("Application for calculate Area and Volume")
    userinput=int(input("Enter 1 for Area. And 2 for Volume: "))
    if userinput == 1:
        print("---Area---")
        userinLength=float(input("Please input Length:"))
        userinWidth=float(input("Please input Width:"))
        
        print(f"Area of {userinLength} and {userinWidth} = {area(userinLength,userinWidth)}.")

    elif userinput == 2 :
        print("---Volume---")
        
        userinLength=float(input("Please input Length:"))
        userinWidth=float(input("Please input Width:"))
        userinHeight=float(input("Please input Height:"))
        print(f"Area of {userinLength}, {userinHeight} and {userinWidth} = {volume(userinLength,userinWidth,userinHeight)}.")
    else:
        print("Invalid Input...")
except ValueError:
    print("Invalid input! Try again...")