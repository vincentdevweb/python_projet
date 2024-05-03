from abc import ABC, abstractmethod
from typing import Generic, Iterable, Optional, TypeVar

T = TypeVar("T")

class GenericDao(Generic[T],ABC):
    
    @abstractmethod
    def save(self, t: T) -> T:
        pass
    
    @abstractmethod
    def update(self, t: T) -> T:
        pass
    
    @abstractmethod
    def delete(self, t: T) -> None:
        pass
    
    @abstractmethod
    def find_all(self) -> Iterable[T]:
        pass
    
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[T]:
        pass