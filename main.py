import random
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

user_input=int(input("Select\n0 for Rock \n1 for Paper\n2 for Scissors\n:"))
computer_input=random.randint(0,2)
print(computer_input)

RPS_list=[rock,paper,scissors]

print(f"Your Input:{RPS_list[user_input]}")
print(f"Computer Input:{RPS_list[computer_input]}")

rule_book=[["Tie","Computer Wins","User Wins"],
          ["User Wins","Tie","Computer Wins"],
           ["Computer Wins","User Wins","Tie"]]

print(rule_book[user_input][computer_input])