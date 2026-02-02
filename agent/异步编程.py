import time
import asyncio

async def make_coffee_async(customer:str) -> str:
    print(f"开始执行任务{customer}")
    asyncio.sleep(1)
    return f"{customer}的任务"


async def main_async():
    start_time = time.time()

    # 创建任务清单
    tasks = [
        make_coffee_async("顾客A"),
        make_coffee_async("顾客B"),
    ]

    result = await asyncio.gather(*tasks)
    print(result)
    end_time = time.time()

    print(f"异步方式总耗时：{end_time - start_time}秒")


if __name__ == '__main__':
    asyncio.run(main_async())



