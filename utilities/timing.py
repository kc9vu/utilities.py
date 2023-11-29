import time
from contextlib import contextmanager


def _human_like(num: float) -> str:
    days, seconds = divmod(num, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    if days:
        if days > 1000:
            return f"{num:,.1f} seconds"
        return f"{days:.0f} days {hours + round(minutes / 60):.0f} hours"
    if hours:
        return f"{hours:.0f} hours {minutes + round(seconds):.0f} minutes"
    if minutes:
        return f"{minutes:.0f} minutes {seconds:.1f} seconds"
    if seconds > 1:
        return f"{num:.1f} seconds"
    else:
        return f"{num * 1000:.3f} milliseconds"


@contextmanager
def time_cost(message: str = ''):
    """计算耗时并输出易读的时间"""
    begin_at = time.perf_counter()
    yield
    cost = time.perf_counter() - begin_at

    print('[TIMING]', end=' ')
    if message:
        print(message, end=': ')
    print(f'Cost {_human_like(cost)}')
