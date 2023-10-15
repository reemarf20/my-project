fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Lets add 'Orange' to the list
fruits.append("orange")

#Lets check if an item is there in the list
user_input = input("Enter the name of a fruit: ")

if user_input in fruits:
    print("Yes, " + user_input + " is in the list.")
else:
    print("No, " + user_input + " is not in the list.")
