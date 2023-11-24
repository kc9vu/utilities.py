import asyncio
from functools import wraps

type Semaphore = asyncio.Semaphore


class do_with_semaphore:
    def __init__(self, sema: Semaphore, /):
        self.sema = sema

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with self.sema:
                result = await func(*args, **kwargs)
                return result

        return wrapper
