import tomllib
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import msgpack
import orjson


@contextmanager
def _open(file, **kwargs):
    if not isinstance(file, Path):
        try:
            file = Path(file)
        except TypeError:
            raise TypeError(f"必须是一个可转为 Path 对象的类型, 传入不合法 {file:r}")
    file, _file = file.resolve(), file
    with open(file, **kwargs) as buffer:
        yield buffer


def read_json(file, **kwargs) -> Any:
    """以 JSON 格式读取文件, 返回读取的结果"""
    kwargs["mode"] = "rb"
    with _open(file, **kwargs) as ins:
        return orjson.loads(ins.read())


def write_json(obj: Any, file, *, default=None, option=None, **kwargs) -> int:
    """以 JSON 格式写入到文件中, 返回写入的字节数\n
    `option` 可选多个序列化选项（数字相加／按位或）:\n
    以 2 个空格缩进 (1), 允许非字符串键 (4), 忽略时间的毫秒 (8), 自动排序键 (32)
    """
    kwargs["mode"] = "wb"
    with _open(file, **kwargs) as outs:
        return outs.write(orjson.dumps(obj, default=default, option=option | 64))


def read_msgpack(file, **kwargs) -> Any:
    """以 MSGPACK 格式读取文件, 返回读取的结果"""
    kwargs['mode'] = 'rb'
    with _open(file, **kwargs) as ins:
        return msgpack.load(ins)


def write_msgpack(obj: Any, file, **kwargs) -> None:
    """以 MSGPACK 格式写入文件"""
    kwargs['mode'] = 'wb'
    with _open(file, **kwargs) as outs:
        msgpack.dump(obj, outs)


def read_toml(file, **kwargs) -> Any:
    """以 TOML 格式读取文件, 返回读取的结果"""
    kwargs['mode'] = 'rb'
    with _open(file, **kwargs) as ins:
        return tomllib.load(ins)
