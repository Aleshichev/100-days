# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# x = sentence.split()
#
# result = {item:len(item) for item in x}
#
# print(result)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {word:((temp* 9/5) + 32) for (word, temp) in weather_c.items()}
#
# print(weather_f)

student_dict = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# просматриваем словари
for (key,value) in student_dict.items():
   print(key)

import pandas

st_data_frame = pandas.DataFrame(student_dict)       # таблица данных
# print(st_data_frame)
# for (key,value) in st_data_frame.items():
#     print(value)

# iterrows - обрабатывает каждую строку
for (index, row) in st_data_frame.iterrows():
    if row.students == "Angela":
        print(row.score)     # объект панды
