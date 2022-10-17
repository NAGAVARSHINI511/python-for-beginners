import random	
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
random_num=random.randint(0,1)

if random_num==1:
  print("Heads")
else:
  print("Tails")