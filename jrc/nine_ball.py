import random
#This is a nine ball solution program

regular_weight = int(input("Tell me the weight of the regular ball: "))
odd_weight = int(input("Tell me the weight for the odd ball: "))

balls = [regular_weight] * 9
odd_index = random.randint(0,8)
balls[odd_index] = odd_weight


print(balls)
print(odd_index)
