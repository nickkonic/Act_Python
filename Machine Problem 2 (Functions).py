string = input("Enter a string: ")

def palindrome(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    else:
        return False

if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
