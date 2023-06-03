import random
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names1=(len(names))
names2=random.randint(0, names1 -1)

names_end=names [names2] + "is going to buy the meal today!"
print(names_end)
