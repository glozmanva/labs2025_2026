from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @classmethod
    def get_name(cls):
        return cls.__name__