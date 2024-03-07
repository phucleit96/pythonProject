# # with open("weather_data.csv", mode="r") as f:
# #     list = f.readlines()
# #     print(list)
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #     temperature = []
# #     for rows in data:
# #         if rows[0] == "day":
# #             pass
# #         else:
# #             temp = int(rows[1])
# #             temperature.append(temp)
# #     print(temperature)
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)
# sum = 0
# for temp in temp_list:
#     sum += temp
#
# # average_temp = "{:.2f}".format(float(sum/len(temp_list)))
# # print(f"The average temp is {average_temp}")
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # # Get data in columns:
# # print(data["condition"])
# # print(data.condition)
# # Get data in rows:
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp*9/5 + 32
# print(monday_temp_f)
#
# #Create a dataframe from scratch:
# data_example = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data_ex = pandas.DataFrame(data_example)
# print(data_ex)
# data_ex.to_csv("../test/new_data.csv")
import csv

import pandas as pd
# df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df = pd.read_csv("weather_data.csv")
# distinct_count = df["Primary Fur Color"].value_counts()
# print(distinct_count)
#
#
# new_data = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [x for x in distinct_count]
# }
# new_df = pd.DataFrame(new_data)
# print(new_df)
# new_df.to_csv("squirrel_count.csv")
a = df[df.day == "Sunday"]["condition"]
print(a)


