from collections.abc import Callable, Iterator, Mapping, Sequence
from enum import Enum
from typing import Any

from django.http.request import HttpRequest
from django.template.context import Context as Context
from django.template.engine import Engine
from django.template.library import Library
from django.template.loaders.base import Loader
from django.utils.safestring import SafeText

FILTER_SEPARATOR: str
FILTER_ARGUMENT_SEPARATOR: str
VARIABLE_ATTRIBUTE_SEPARATOR: str
BLOCK_TAG_START: str
BLOCK_TAG_END: str
VARIABLE_TAG_START: str
VARIABLE_TAG_END: str
COMMENT_TAG_START: str
COMMENT_TAG_END: str
TRANSLATOR_COMMENT_MARK: str
SINGLE_BRACE_START: str
SINGLE_BRACE_END: str
UNKNOWN_SOURCE: str
tag_re: Any
logger: Any

class TokenType(Enum):
    TEXT: int
    VAR: int
    BLOCK: int
    COMMENT: int

class VariableDoesNotExist(Exception):
    msg: str = ...
    params: tuple[dict[str, str] | str] = ...
    def __init__(self, msg: str, params: tuple[dict[str, str] | str] = ...) -> None: ...

class Origin:
    name: str = ...
    template_name: bytes | str | None = ...
    loader: Loader | None = ...
    def __init__(
        self,
        name: str,
        template_name: bytes | str | None = ...,
        loader: Loader | None = ...,
    ) -> None: ...
    @property
    def loader_name(self) -> str | None: ...

class Template:
    name: str | None = ...
    origin: Origin = ...
    engine: Engine = ...
    source: str = ...
    nodelist: NodeList = ...
    def __init__(
        self,
        template_string: Template | str,
        origin: Origin | None = ...,
        name: str | None = ...,
        engine: Engine | None = ...,
    ) -> None: ...
    def __iter__(self) -> None: ...
    def render(
        self,
        context: Context | dict[str, Any] | None = ...,
        request: HttpRequest | None = ...,
    ) -> SafeText: ...
    def compile_nodelist(self) -> NodeList: ...
    def get_exception_info(
        self, exception: Exception, token: Token
    ) -> dict[str, Any]: ...

def linebreak_iter(template_source: str) -> Iterator[int]: ...

class Token:
    contents: str
    token_type: TokenType
    lineno: int | None = ...
    position: tuple[int, int] | None = ...
    def __init__(
        self,
        token_type: TokenType,
        contents: str,
        position: tuple[int, int] | None = ...,
        lineno: int | None = ...,
    ) -> None: ...
    def split_contents(self) -> list[str]: ...

class Lexer:
    template_string: str = ...
    verbatim: bool | str = ...
    def __init__(self, template_string: str) -> None: ...
    def tokenize(self) -> list[Token]: ...
    def create_token(
        self,
        token_string: str,
        position: tuple[int, int] | None,
        lineno: int,
        in_tag: bool,
    ) -> Token: ...

class DebugLexer(Lexer):
    template_string: str
    verbatim: bool | str
    def tokenize(self) -> list[Token]: ...

class Parser:
    tokens: list[Token] | str = ...
    tags: dict[str, Callable[..., Any]] = ...
    filters: dict[str, Callable[..., Any]] = ...
    command_stack: list[tuple[str, Token]] = ...
    libraries: dict[str, Library] = ...
    origin: Origin | None = ...
    def __init__(
        self,
        tokens: list[Token] | str,
        libraries: dict[str, Library] | None = ...,
        builtins: list[Library] | None = ...,
        origin: Origin | None = ...,
    ) -> None: ...
    def parse(self, parse_until: tuple[str, ...] | None = ...) -> NodeList: ...
    def skip_past(self, endtag: str) -> None: ...
    def extend_nodelist(self, nodelist: NodeList, node: Node, token: Token) -> None: ...
    def error(self, token: Token, e: Exception | str) -> Exception: ...
    def invalid_block_tag(
        self,
        token: Token,
        command: str,
        parse_until: list[Any] | tuple[str] = ...,
    ) -> Any: ...
    def unclosed_block_tag(self, parse_until: tuple[str]) -> Any: ...
    def next_token(self) -> Token: ...
    def prepend_token(self, token: Token) -> None: ...
    def delete_first_token(self) -> None: ...
    def add_library(self, lib: Library) -> None: ...
    def compile_filter(self, token: str) -> FilterExpression: ...
    def find_filter(self, filter_name: str) -> Callable[..., Any]: ...

constant_string: Any
filter_raw_string: Any
filter_re: Any

class FilterExpression:
    token: str = ...
    filters: list[Any] = ...
    var: Any = ...
    def __init__(self, token: str, parser: Parser) -> None: ...
    def resolve(
        self, context: Mapping[str, Any], ignore_failures: bool = ...
    ) -> Any: ...
    @staticmethod
    def args_check(
        name: str, func: Callable[..., Any], provided: list[tuple[bool, Any]]
    ) -> bool: ...

class Variable:
    var: dict[Any, Any] | str = ...
    literal: SafeText | float | None = ...
    lookups: tuple[str] | None = ...
    translate: bool = ...
    message_context: str | None = ...
    def __init__(self, var: dict[Any, Any] | str) -> None: ...
    def resolve(
        self, context: Mapping[str, Mapping[str, Any]] | Context | int | str
    ) -> Any: ...

class Node:
    must_be_first: bool = ...
    child_nodelists: Any = ...
    origin: Origin
    token: Token = ...
    def render(self, context: Context) -> str: ...
    def render_annotated(self, context: Context) -> int | str: ...
    def __iter__(self) -> None: ...
    def get_nodes_by_type(self, nodetype: type[Node]) -> list[Node]: ...

class NodeList(list[Node]):
    contains_nontext: bool = ...
    def render(self, context: Context) -> SafeText: ...
    def get_nodes_by_type(self, nodetype: type[Node]) -> list[Node]: ...

class TextNode(Node):
    s: str = ...
    def __init__(self, s: str) -> None: ...

def render_value_in_context(value: Any, context: Context) -> str: ...

class VariableNode(Node):
    filter_expression: FilterExpression = ...
    def __init__(self, filter_expression: FilterExpression) -> None: ...

kwarg_re: Any

def token_kwargs(
    bits: Sequence[str], parser: Parser, support_legacy: bool = ...
) -> dict[str, FilterExpression]: ...