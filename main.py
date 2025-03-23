# x = 5
# y = 4
# print(x + y)
#
# my_list = [10, 20, 30, 40, 50, 60]
#
# if __name__ == "__main__":
#     print("Loop Executing")
#     for num in my_list:
#         print(num)
#     print("Loop Completed")
import time


def my_func1():
    print("Function 1 Executing")
    time.sleep(5)
    print("Function 1 Completed")
    return 5

def my_func2():
    print("Function 2 Executing")
    time.sleep(5)
    print("Function 2 Completed")
    return 10

if __name__ == "__main__":
    x = my_func1()
    y = my_func2()
    print(f"After completed my_func1 result x = {x}")
    print(f"After completed my_func2 result y = {y}")