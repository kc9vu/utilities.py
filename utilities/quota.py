import asyncio

type Semaphore = asyncio.Semaphore


class do_with_semaphore:
    def __init__(self, sema: Semaphore):
        self.sema = sema

    def __call__(self, func):
        async def wrapper(*args, **kwargs):
            async with self.sema:
                result = await func(*args, **kwargs)
                return result

        return wrapper


if __name__ == "__main__":
    import random

    @do_with_semaphore(asyncio.Semaphore(3))
    async def test(n):
        print(f"Task {n} start...")
        await asyncio.sleep(0.4 + random.random() * 0.3)
        print(f"Task {n} done.")

    async def run():
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(test(n)) for n in range(1, 8)]
        return tasks

    asyncio.run(run())
