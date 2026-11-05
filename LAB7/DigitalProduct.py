from Product import Product

class DigitalProduct(Product):
    def __init__(self, id, name, price, stock, download_size):
        super().__init__(id, name, price, stock)
        self._download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

#test

digital_product = DigitalProduct(
    id = "P001",
    name = "OS",
    price = 100.0,
    stock = 10,
    download_size = 250
)
digital_product.display_information()