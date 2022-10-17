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
image=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(image[user_choice])

import random
c_choice=int(random.randint(0,2))
print(f"computer chose {c_choice}")
print(image[c_choice])


if user_choice==c_choice:
  print("none win!! DRAW")
elif user_choice>c_choice:
  print("YOU WIN, HURRAY!!!...")
elif user_choice<c_choice:
  print("YOU LOOSE, better luck next time..")





