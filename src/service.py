from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def areas(self):
        pass

    @abstractmethod
    def concreto(self):
        pass

    @abstractmethod
    def mortero(self):
        pass

    @abstractmethod
    def elemento(self):
        pass
