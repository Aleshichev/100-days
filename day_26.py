numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [num**2 for num in numbers]

#Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:

print(result)


with open("file1.txt") as f:
    new_f = f.readlines()

with open("file2.txt") as f2:
    new_f2 = f2.readlines()

result = [int(num) for num in new_f if num in new_f2]


# Write your code above 👆

print(result)
