from LAB9.discount_strategy.DiscountStrategy import DiscountStrategy

class NoDiscount (DiscountStrategy):
    def apply(self, total:float) -> float:
        return total
