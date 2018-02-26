firstName = input("Enter your first name:")
lastName = input("Enter your last name:")
reversedFirstName = ""
reversedLastName = ""
for char in reversed(firstName):
    reversedFirstName+=char
for char in reversed(lastName):
    reversedLastName+=char
print(reversedFirstName+" "+reversedLastName)
