from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def format(self):
        pass
