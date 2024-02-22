import pyinputplus as pyip
import random

while True:
    min = 1
    max = 100
    count = 0
    random_number = random.randint(min,max)
    print(random_number)
    print("==========猜數字遊戲==========")
    while True:
        keyin = pyip.inputInt(f"請猜數字範圍{min}~{max}:")
        count += 1
        print(keyin)
        if keyin == random_number:
            print(f"賓果!猜對了,答案是:{random_number}")
            print(f"您猜了{count}次")
            break
        elif keyin > random_number:
            print(f"{keyin} 請猜小一點")
            max = keyin - 1
        else:
            print(f"{keyin} 請猜大一點")
            min = keyin + 1
        print(f"您已經猜了{count}次")
        print("=====================")

    is_continue = pyip.inputYesNo("請問還要繼續嗎? (y/n):")
    if is_continue != "yes":
        break
print("遊戲結束")