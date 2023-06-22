import asyncio

async def my_async_function():
    for i in 'hello':
        print(i)
    print(2)
    print(3)
    print(4)
    print("Асинхронная операция завершена")

asyncio.run(my_async_function())