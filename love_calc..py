# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_1 = name1.lower()
name_2 = name2.lower()
l = (name_1 + name_2).count('l')
o = (name_1 + name_2).count('o')
v = (name_1 + name_2).count('v')
e = (name_1 + name_2).count('e')

love = str(l+o+v+e)

t = (name_1 + name_2).count('t')
r = (name_1 + name_2).count('r')
u = (name_1 + name_2).count('u')
e = (name_1 + name_2).count('e')

true = str(t+r+u+e)
love_score = int(true + love)
if 10 > love_score or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")