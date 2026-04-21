

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ValueObject[TValue](ABC):
    value: TValue

    @classmethod
    @abstractmethod
    def default(cls) -> Self:
        pass

    @classmethod
    @abstractmethod
    def parse(cls, s: str) -> Self:
        pass


@dataclass(frozen=True)
class VideoTitle(ValueObject[str]):
    def __post_init__(self):
        if not isinstance(self.value, str):
            raise ValueError(f'The title must be an instance of str class, but was <{type(self.value)}> type.')

    @classmethod
    def parse(cls, s: str) -> Self:
        if not isinstance(s, str):
            raise ValueError(f'The s must be an instance of a str class, but was <{type(s)}> type.')
        return cls(s)

    @classmethod
    def default(cls) -> Self:
        return cls('')



@dataclass(frozen=True)  
class VideoCTR(ValueObject[float]):
    def __post_init__(self):
        if not isinstance(self.value, float):
            raise ValueError(f'The ctr must be an instance of float class, but was <{type(self.value)}> type.')
        if not 0 <= self.value <= 100:
            raise ValueError(f'The ctr must be a positive real number in range [0, 100], but was <ctr={self.value}>.')

    @classmethod
    def parse(cls, s: str) -> Self:
        if not isinstance(s, str):
            raise ValueError(f'The s must be an instance of a str class, but was <{type(s)}> type.')
        return cls(float(s))

    @classmethod
    def default(cls) -> Self:
        return cls(0.0000001)


@dataclass(frozen=True) 
class VideoRetentionRate(ValueObject[int]):
    def __post_init__(self):
        if not isinstance(self.value, int):
            raise ValueError(f'The retention rate must be an instance of integer class, but was <{type(self.value)}> type.')
        if not 0 <= self.value <= 100:
            raise ValueError(f'The retention rate must be in range [0, 100], but was <retention rate={self.value}>.')

    @classmethod
    def parse(cls, s: str) -> Self:
        if not isinstance(s, str):
            raise ValueError(f'The s must be an instance of a str class, but was <{type(s)}> type.')
        return cls(int(s))

    @classmethod
    def default(cls) -> Self:
        return cls(0)

        

@dataclass(frozen=True)  
class Count(ValueObject[int]):
    def __post_init__(self):
        if not isinstance(self.value, int):
            raise ValueError(f'The count must be an instance of an integer class, but was <{type(self.value)}> type.')
        if self.value < 0:
            raise ValueError(f'The count must be a non negative integer number, but was <views={self.value}>.')

    @classmethod
    def parse(cls, s: str) -> Self:
        if not isinstance(s, str):
            raise ValueError(f'The s must be an instance of a str class, but was <{type(s)}> type.')
        return cls(int(s))

    @classmethod
    def default(cls) -> Self:
        return cls(0)

        

@dataclass(frozen=True)  
class VideoWatchTime(ValueObject[float]):
    def __post_init__(self):
        if not isinstance(self.value, float):
            raise ValueError(f'The watch time must be an instance of a float class, but was <{type(self.value)}> type.')
        if self.value < 0:
            raise ValueError(f'The watch time must be a non negative real number, but was <average watch time={self.value}>.')

    @classmethod
    def parse(cls, s: str) -> Self:
        if not isinstance(s, str):
            raise ValueError(f'The s must be an instance of a str class, but was <{type(s)}> type.')
        return cls(float(s))

    @classmethod
    def default(cls) -> Self:
        return cls(0.0000001)


