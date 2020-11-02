# What is concatenation

first_name = "leo"
last_name = "w"
middle_name = "777"
age = 21

print(first_name, last_name)

#casting

print(str(age))
print(int(middle_name))



name = input("What is your name: ")
dob = input("What is your date of birth: ")
age = input("How old are you: ")
address = input("Where do you live: ")

print(f'Hi {name}, you were born in {dob}, you are {age} years old.')

print("Hello " + name + ", you were born on " + dob + " and so you are " + str(age) + " years old. You live in " + address)
