from Supplier import Supplier
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

class ProductFactory:
    @staticmethod
    def create (
        product_medium:str, 
        product_id:str, 
        name:str, 
        price:float, 
        stock:int,
        supplier:Supplier,
        weight: float | None = None,
        download_size: float | None = None,
        ) -> Product:
        if product_medium == "physical":
            if weight is None:
                raise ValueError("Physical products require weight.")
            return PhysicalProduct(product_id, name, price, stock, supplier, weight)

        if product_medium == "digital":
            if download_size is None:
                raise ValueError("Digital products require download_size.")
            return DigitalProduct(
                product_id, name, price, stock, supplier, download_size
            )

        raise ValueError(f"Unknown product type: {product_medium}")