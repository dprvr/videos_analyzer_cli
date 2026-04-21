

from abc import ABC, abstractmethod


class DataExtracter[TData](ABC):
    
    @abstractmethod
    def extract_data(self) -> TData:
        pass