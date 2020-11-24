import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_people = len(names)
randomInteger = random.randint(0, num_people - 1)
payer = names[randomInteger]

# payer = random.choice(names)

print(payer + " is going to buy the meal today!")