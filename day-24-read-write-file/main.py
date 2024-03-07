# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
# with open("my_file.txt", mode="a") as file: # open file in read-only mode as r, w = write
#     # contents = file.read() # a stand for append --> add on
#     # print(contents)
#     # no need to worry about close file
#     file.write("\nNew text: Duc Le")

with open("../../Desktop/non", mode="r") as f:
    contents = f.read()
    print(contents)