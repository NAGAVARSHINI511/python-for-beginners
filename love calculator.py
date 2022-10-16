print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
l_name1=name1.lower()
l_name2=name2.lower()

t_t=l_name1.count('t')+l_name1.count('u')+l_name1.count('r')+l_name1.count('e')+l_name2.count('t')+l_name2.count('u')+l_name2.count('r')+l_name2.count('e')

t_l=l_name1.count('l')+l_name1.count('0')+l_name1.count('v')+l_name1.count('e')+l_name2.count('l')+l_name2.count('0')+l_name2.count('v')+l_name2.count('e')

x =int(str(t_t)+str(t_l))

if(x<10 or x>90):
    print(f"Your score is {x}, you go together like coke and mentos.")
elif(x>40 and x<50):
    print(f"Your score is {x}, you are alright together.")
else:
    print(f"Your score is {x}.")