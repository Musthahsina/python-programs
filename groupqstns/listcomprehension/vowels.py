# remove vowels
string='Hello world'
vowels=['a','e','i','o','u','A','E','I','O','U']
nonvowels = [i for i in string if i not in vowels]
nonvowels=''.join(nonvowels)
print(nonvowels)