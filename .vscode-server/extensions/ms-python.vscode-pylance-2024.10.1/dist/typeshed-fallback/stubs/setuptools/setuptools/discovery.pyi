import itertools
from _typeshed import Incomplete, StrPath
from collections.abc import Iterable, Iterator, Mapping
from typing import ClassVar
from typing_extensions import TypeAlias

from . import Distribution

StrIter: TypeAlias = Iterator[str]
chain_iter = itertools.chain.from_iterable

class _Filter:
    def __init__(self, *patterns: str) -> None: ...
    def __call__(self, item: str) -> bool: ...
    def __contains__(self, item: str) -> bool: ...

class _Finder:
    ALWAYS_EXCLUDE: ClassVar[tuple[str, ...]]
    DEFAULT_EXCLUDE: ClassVar[tuple[str, ...]]
    @classmethod
    def find(cls, where: StrPath = ".", exclude: Iterable[str] = (), include: Iterable[str] = ("*",)) -> list[str]: ...

class PackageFinder(_Finder):
    ALWAYS_EXCLUDE: ClassVar[tuple[str, ...]]

class PEP420PackageFinder(PackageFinder): ...
class ModuleFinder(_Finder): ...

class FlatLayoutPackageFinder(PEP420PackageFinder):
    DEFAULT_EXCLUDE: ClassVar[tuple[str, ...]]

class FlatLayoutModuleFinder(ModuleFinder):
    DEFAULT_EXCLUDE: ClassVar[tuple[str, ...]]

class ConfigDiscovery:
    dist: Incomplete
    def __init__(self, distribution: Distribution) -> None: ...
    def __call__(self, force: bool = False, name: bool = True, ignore_ext_modules: bool = False) -> None: ...
    def analyse_name(self) -> None: ...

def remove_nested_packages(packages: list[str]) -> list[str]: ...
def remove_stubs(packages: list[str]) -> list[str]: ...
def find_parent_package(packages: list[str], package_dir: Mapping[str, str], root_dir: StrPath) -> str | None: ...
def find_package_path(name: str, package_dir: Mapping[str, str], root_dir: StrPath) -> str: ...
def construct_package_dir(packages: list[str], package_path: StrPath) -> dict[str, str]: ...
