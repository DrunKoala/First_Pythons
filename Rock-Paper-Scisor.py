import random
while True:
    n = input(
        "\n\033[35mTas\033[0m-\033[35mKagit\033[0m-\033[35mMakas\033[0m? ")

    a = ["Tas", "Kagit", "Makas"]

    b = random.choice(a)

    if n == b:
        print(
            f" \nBerabere\n\033[34mSen=\033[0m (\033[37m{n}\033[0m) sectin  \033[33mAI=\033[0m (\033[37m{b}\033[0m) secti")
    elif (n == "Tas" and b == "Makas") or \
         (n == "Kagit" and b == "Tas") or \
         (n == "Makas" and b == "Kagit"):
        print(
            f"\n\033[32mSen kazandin\033[0m   \n\033[34mSen=\033[0m (\033[37m{n}\033[0m)  \033[33mAI=\033[0m (\033[37m{b}\033[0m)")
    else:
        print(
            f"\n\033[31mSen kaybetdin\033[0m  \n\033[34mSen=\033[0m (\033[37m{n}\033[0m)  \033[33mAI=\033[0m (\033[37m{b}\033[0m)")
