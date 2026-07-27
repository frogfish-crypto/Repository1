# 1. Write a function called middle with one argument that returns the middle letter of a string. If the string is even, return two letters.

# 2. Write a function called vowelPicker with one argument that returns a string made of all the vowels in the word. i.e. vowelPicker("python code") will return "ooe"

# 3. Write a function called reverse with one argument that returns the reverse of the input string.

# 4. Write a function called palindrome with one argument that returns True if the input string is a palindrome (ignoring case)

# 5. Write a function called check with two arguments (str1, str2) and checks how many instances of the second string can be found in the first string (ignoring case)

# 6. Write a function called makePalindrome with one argument that takes the first half of the input string, reverses it, and adds it to the end of the string. Any string created by this method should return True on the palindrome function.

# 7. Write a function called indexMultiple with two arguments (num, str) that returns only the indices of the string which are a multiple of num (if num is 3, the returned string should have the indices 3, 6, 9, etc.)

# 8. Write a function called indexSum with two arguments (str1, str2) that returns the sum of the indices where str2 is found in the str1 (i.e. indexSum("hello", "l") will return 5)

#1
def middle(string):
    if len(string)%2!=0:
        halfway=len(string)//2
        return(string[halfway])
    else:
        halfway=len(string)//2
        return(string[(halfway-1):(halfway+1)])
    
string="Helloworld"
middle = middle(string)
print(middle)

#2
def vowelpicker(string):
    for i in range(0, len(string)):
        if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
            print(string[i], end="")
    print("")
    
string="Helloworld"
vowelpicker(string)

#3
def reverse(string):
    return (string[::-1])

string="Helloworld"
reverse=reverse(string)
print(reverse)

#4
def palindrome(string):
    str.lower(string)
    if string[::-1]==string[::1]:
        return True
    else:
        return False
    
string="racecar"
print(palindrome(string))

#5
def check(str1, str2):
    str.lower(string)
    return str1.count(str2)

str1="Helloworld"
str2="l"
print(check(str1, str2))

#6
def makePalindrome(string):
    return string+string[::-1]

string= "Helloworld"
print(makePalindrome(string))

#7

def indexMultiple(num,str):
    for i in range(0,len(str)):
        if i!=0 and i%num==0:
            print (string[i], end="")
    print("")

num=3
str="HelLowOrlD"
indexMultiple(num,str)

#8 Write a function called indexSum with two arguments 
# (str1, str2) that returns the sum of the indices 
# where str2 is found in the str1 (i.e. indexSum("hello", "l") 
# will return 5)

def indexSum(str1, str2):
    sum=0
    for i in range (0,len(str1)):
        if str1[i]==str2:
            sum+=i
    return sum

str1="Helloworld"
str2="l"
indexSum=indexSum(str1, str2)
print(indexSum)
