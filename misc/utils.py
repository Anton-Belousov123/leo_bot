from random import randint


async def get_random_name():
    s = ''
    for i in range(16):
        s = s + str(randint(0, 9))
    return s
