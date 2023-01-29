from typing import Awaitable, Callable, ParamSpec, TypeVar
from async_lru import alru_cache

P = ParamSpec("P")
T = TypeVar("T", bound=Awaitable)


def alru_cache_typed(
    fn: Callable[P, T] = None,
    *,
    maxsize: int = 128,
    typed: bool = False,
    cache_exceptions: bool = True
) -> Callable[P, T]:
    return alru_cache(
        fn=fn,
        maxsize=maxsize,
        typed=typed,
        cache_exceptions=cache_exceptions
    )
