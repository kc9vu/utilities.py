# utilities

> 为 Python 中常用的操作提供快捷函数

将目录设为 `PYTHONPATH` 即可使用

## **quota.py**

- _@_ do\_with\_semaphore(*sema*)

  通过信号量 `asyncio.Semaphore` 控制协程的并发数量

  ```python
  import asyncio
  
  @do_with_semaphore(asyncio.Semaphore(3))
  async def do_something(*args, **kwargs):
      ...
  ```

## **fileop.py**

- read_json(*file*, _\*\*kwargs_)

  以 JSON 格式读取文件

- read_msgpack(*file*, _\*\*kwargs_)

  以 MSGPACK 格式读取文件

- read_toml(*file*, _\*\*kwargs_)

  以 TOML 格式读取文件

- write_json(_obj_, _file_, _default=None_, _option=None_, _\*\*kwargs_)

  以 JSON 格式写入文件, 返回写入的字节数.  
  使用的是 `orjson.dumps`, 可以传入 _default_ 与 _option_ 以定制

- write_msgpack(_obj_, _file_, _\*\*kwargs_)

  以 JSON 格式读取文件
