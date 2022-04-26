rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_image = [rock, scissors, paper]
usser = int(input("Input the name (0 - rock or 1 - scissors or 2 - paper): "))
if   0 > usser or usser >= 3:
    print("Try again. Only 0,1,2")
else:
    print("YOU:""\n", game_image[usser])

    answer_pc = random.randint(0,2)
    print("PC:""\n", game_image[answer_pc])

    if answer_pc == int(usser):
      print('draw')
    elif (answer_pc == 0 and usser == 2) or (answer_pc == 1 and usser == 0) or (answer_pc == 2 and usser == 1):
      print("you win")
    else:
      print("pc - win")





