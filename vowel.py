def rem_vowel(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result = [letter for letter in string if letter not in vowels]
    result = ''.join(result)
    print(result)
  
string = input("Enter the name:")
rem_vowel(string)
