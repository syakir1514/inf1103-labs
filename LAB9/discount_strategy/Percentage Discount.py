from LAB9.discount_strategy.DiscountStrategy import DiscountStrategy

class PercentageDiscount (DiscountStrategy):
    def __init__(self, percentage: float):
        self._percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self._percentage / 100)
