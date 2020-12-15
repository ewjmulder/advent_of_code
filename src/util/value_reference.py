from typing import TypeVar, Generic
from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class ValueReference(Generic[T]):
    value: T
