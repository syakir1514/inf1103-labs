from abc import ABC


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total:float) -> float:
        pass