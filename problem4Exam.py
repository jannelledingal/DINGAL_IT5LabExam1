def isPalindrome(valStr):
    
    return valStr == valStr[::-1]

def toBinaryIfNumber(value):
    
    if value.isdigit():
        return bin(int(value))[2:]  
    return None


user_input = input("Enter a value: ")


input_palindrome = isPalindrome(user_input)
print("Input is a palindrome:", input_palindrome)


binary_value = toBinaryIfNumber(user_input)
if binary_value:
    print("Binary equivalent:", binary_value)
    binary_palindrome = isPalindrome(binary_value)
    print("Binary is a palindrome:", binary_palindrome)
else:
    print("(No binary conversion since input is text)")
