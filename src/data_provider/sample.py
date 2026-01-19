import random

def getRandomUniqueUniform(startRange, endRange, count):
    result = random.sample(range(startRange, endRange + 1),k = count)
    return result
