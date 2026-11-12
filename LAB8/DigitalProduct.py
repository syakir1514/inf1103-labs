from Product import Product

class DigitalProduct(Product):
    def __init__(self, id, name, price, stock, supplier, download_size:float):
        super().__init__(id, name, price, stock, supplier)
        self._medium = "digital"
        self._download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self._download_size} MB")
        super().display_supplier()

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

#test
def test():
    digital_product = DigitalProduct(
        id = "P001",
        name = "OS",
        price = 100.0,
        stock = 10,
        download_size = 250
    )
    digital_product.display_information()