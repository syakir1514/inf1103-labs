from discount_strategy.DiscountStrategy import DiscountStrategy

class StudentDiscount (DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.75
