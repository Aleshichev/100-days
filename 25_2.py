import pandas

data = pandas.read_csv("Squirrel.csv")    # открываем фаил через панду
grey_squirrel = data[data["Highlight Fur Color"] == "Gray"]
grey_squirrel_count = len(data[data["Highlight Fur Color"] == "Gray"])
Cinnamon_squirrel_count = len(data[data["Highlight Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Highlight Fur Color"] == "Black"])
print(Cinnamon_squirrel_count)
print(grey_squirrel_count)
print(black_squirrel_count)
# создаём словарь
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, Cinnamon_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("sq_count.csv")     # создаём фаил

print(data_dict)