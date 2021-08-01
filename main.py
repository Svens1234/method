# immutable, неизменяемые
first_name = 'Jake'

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)

# Concatenable
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

greeting = 'Hello'
greeting = greeting + ' Python!'
print(greeting)

# Multiplication
yummy = 'Yum '
print(yummy * 3)
print(yummy.upper())
print(yummy.lower())

long_string = 'This is long string'
print(long_string.split())

print(long_string.split('s'))
