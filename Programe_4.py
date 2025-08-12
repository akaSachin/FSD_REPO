# Program that keeps asking the user to enter a password until they enter the correct one "python123".

true_password = "python123"

while True:
    password = input("Enter the password: ")
    if password == true_password:
        print("Password is correct and Access is Granted")
        break
    else:
        print("Incorrect password!!! Please try again.")