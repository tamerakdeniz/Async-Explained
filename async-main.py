import asyncio

async def my_func1():
    print("Function 1 Executing")
    await asyncio.sleep(5)
    print("Function 1 Completed")
    return 5

async def my_func2():
    print("Function 2 Executing")
    await asyncio.sleep(5)
    print("Function 2 Completed")
    return 10

async def main():

    task1 = asyncio.create_task(my_func1())
    task2 = asyncio.create_task(my_func2())

    x = await task1
    y = await task2

    print(f"After completed my_func1 result x = {x}")
    print(f"After completed my_func2 result y = {y}")

if __name__ == "__main__":
    asyncio.run(main())