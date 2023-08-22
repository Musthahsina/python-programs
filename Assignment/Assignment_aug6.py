# """1.Ask the user to enter the names of three people they want to invite to a party and store them in a list. Aft
# er they have entered all three names, ask them if they want to add another. If they do, allow them to add
# more names until they answer “no”. When they answer “no”, display how many people they have invited t
# o the party."""

# invitees = []

# for i in range(3):
#     name = input("Enter the name of a person you want to invite: ")
#     invitees.append(name)

# while True:
#     more = input("Do you want to add another person? (yes/no): ").lower()
#     if more == "yes":
#         name = input("Enter the name of a person you want to invite: ")
#         invitees.append(name)
#     elif more == "no":
#         break
#     else:
#         print("Please enter 'yes' or 'no'.")

# num_invited = len(invitees)
# print("You have invited", num_invited, "people to the party.")


# """2.Change the above question so that once the user has completed their list of names, display the full list a
# nd ask them to type in one of the names on the list. Display the position of that
# name in the list. Ask the user if they still want that person to come to the party. If they answer “no”, delete
# that entry from the list and display the list again."""

# invitees = []

# for i in range(3):
#     name = input("Enter the name of a person you want to invite: ")
#     invitees.append(name)

# print("List of invitees:",invitees)

# choose_name = input("Choose a name from the invitees list:")

# position = invitees.index(choose_name) + 1
# print(f"{choose_name} is at position {position} in the list.")

# decide = input(f"Do you still want {choose_name} to come to the party? (yes/no): ").lower()

# if decide=="no":
#     invitees.remove(choose_name)
#     print(choose_name,"has been removed from the list")
#     print("Updated list of invitees:", invitees)


"""
3.Using the below list ask the user which row they would like displayed and display just that row. Ask the
m to enter a new value and add it to the end of the row and display the row again. list=[[2,5,8],[3,7,4],[1,6,
9],[4,2,0]]

"""

# list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

# row_num = int(input("Enter the row number you want to display: "))
# print("Row:", list[row_num - 1])
# new_value = int(input("Enter a new value to add at the end of the row: "))
# list[row_num - 1].append(new_value)
# print("Updated Row:", list[row_num - 1])


"""
4.Ask the user to enter the name, age and Id for four people. Ask for the name of one of the people in the
list and display their age and Id.
"""

# persons = []
# for i in range(4):
#     name = input("Enter the name of a person: ")
#     age = int(input("Enter their age: "))
#     id = input("Enter their ID: ")
#     persons.append({"Name": name, "Age": age, "Id": id})

# find_name = input("Enter the name of a person from the list: ")

# for person in persons:
#     if person["Name"] == find_name:
#         print("Age:", person["Age"])
#         print("ID:", person["Id"])
#         break
# else:
#     print("Person not found in the list")

"""
5.Adapt the above program to display the names and ages of all the people in the list but do not show 
their Id.

"""

# persons = []
# for i in range(4):
#     name = input("Enter the name of a person: ")
#     age = int(input("Enter their age: "))
#     id = input("Enter their ID: ")
#     persons.append({"Name": name, "Age": age, "Id": id})


# print("\nNames and Ages of all people:")
# for person in persons:
#     print("Name:", person["Name"])
#     print("Age:", person["Age"])

"""
6.a. Create a dictionary representing a library catalog with book titles as
keys and values as dictionaries c ontaining information like author, publication year, and genre.
b. Add a new book to the catalog and update the author of an existing book.
c. Write a function to count how many books in the catalog were published before a given year.

"""

#a

library_catalog = {
    "Hamlet": {"author": " William Shakespeare", "year": 1603, "genre": "tragedy"},
    "Pride and Prejudice": {"author": "Jane Austen", "year": 1813, "genre": "romance"},
    "The Lord of the Rings": {"author": "J.R.R. Tolkien", "year": 1968, "genre": "fantasy"}
    }

#b

new_book = {"Othello":{
    "author": "William Shakspeare",
    "year": 1603,
    "genre": "tragedy"}
    }

library_catalog.update(new_book) 

existing_book = "Hamlet"
library_catalog[existing_book]["author"] = "Shakspeare"

print(library_catalog,"\n")


#c

def count_books_before_year(catalog, year):
    count = 0
    for book in catalog.values():
        if book["year"] < year:
            count += 1
    return count

year_to_check = 1960
count = count_books_before_year(library_catalog, year_to_check)
print(f"Number of books published before {year_to_check}: {count}")

