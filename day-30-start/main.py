# FileNotFound
# with open("a_file.txt") as file:
#     file.read()
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     value = a_dictionary["ngu"]
#     print(value)
# except FileNotFoundError:
#     # print("There was an error!")
#     file = open("a_file.txt", "w")
#     file.write("Solved Find Not Found Error")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed!")
#     raise TypeError("This is an error that I made up")
# Key Error
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent"]
# print(value)

# Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# Type Error:
# text = "abc"
# print(text + 5)
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")
bmi = weight / height ** 2
print(bmi)