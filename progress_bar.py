from time import sleep
import math


def create_bar():
    print(f"\rProgress: [----------]", end='')

def update_bar(total, current, info = ""):
    progress = math.ceil(10*(current/total))
    print(f"\rProgress: ["+ "="*progress + "-"* (10-progress) +f"] {current}/{total}  {info}", end='')


if __name__ == '__main__':
    create_bar()

    for i in range(18):
        update_bar(17, i, )
        sleep(1)
    print("")

