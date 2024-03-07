# numbers = [1,2,3]
# new_numbers = [number*3 for number in numbers]
# print(new_numbers)
# name = "Phuc Le"
# new_list = [letter for letter in name]
# print(new_list)

student_dict = {
    "Name": ["Phuc", "Hoa", "Duc"],
    "grade": [100, 30, 20]
}
# Looping through dictionaries
for (key, value) in student_dict.items():
    if key == "Name":
        print(value)


# import pandas
# student_df = pandas.DataFrame(student_dict)
# # print(student_df)
# #
# # #Loop through a data frame
# for (key, value) in student_df.items():
#     print(type(value))
# Loop through rows of a data frame:
# for (index, row) in student_df.iterrows():
#     if row.Name == "Phuc":
#         print(row.grade)
# new_df = {row.name:row.grade for (index, row) in student_df.iterrows()}
# print(new_df)
# print(type(new_df))
