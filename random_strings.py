import random

base_string = input("Your string: ")

i = 1
while i <= 5:
    # result = random.choice(base_string) + random.choice(base_string) + random.choice(base_string) \
    #     + random.choice(base_string) + random.choice(base_string)

    # result = random.choices(base_string, k=5)
    # print("".join(result))

    # result = list(base_string)
    # random.shuffle(result)
    # print("".join(result))

    result = random.sample(base_string, k=len(base_string))
    print("".join(result))

    i += 1
