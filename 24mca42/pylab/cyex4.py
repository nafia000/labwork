from palindrome import is_palindrome
def longest(s):
        n=len(s)
        longest=" "
        for i in range(n):
                for j in range(i,n):
                        substring=s[i:j+1]
                        if is_palindrome(substring) and len(substring)>len(longest):
                                longest=substring
        return longest
input_string=input("Enter a string : ")
print("longest palindromic substring : ",longest(input_string)) 

 

