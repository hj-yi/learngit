from _typeshed import StrOrBytesPath
from collections.abc import Sequence
from types import CodeType
from typing import Any, final

def expr(source: str) -> STType: ...
def suite(source: str) -> STType: ...
def sequence2st(sequence: Sequence[Any]) -> STType: ...
def tuple2st(sequence: Sequence[Any]) -> STType: ...
def st2list(st: STType, line_info: bool = ..., col_info: bool = ...) -> list[Any]: ...
def st2tuple(st: STType, line_info: bool = ..., col_info: bool = ...) -> tuple[Any, ...]: ...
def compilest(st: STType, filename: StrOrBytesPath = ...) -> CodeType: ...
def isexpr(st: STType) -> bool: ...
def issuite(st: STType) -> bool: ...

class ParserError(Exception): ...

@final
class STType:
    def compile(self, filename: StrOrBytesPath = ...) -> CodeType: ...
    def isexpr(self) -> bool: ...
    def issuite(self) -> bool: ...
    def tolist(self, line_info: bool = ..., col_info: bool = ...) -> list[Any]: ...
    def totuple(self, line_info: bool = ..., col_info: bool = ...) -> tuple[Any, ...]: ...
