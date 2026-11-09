

class Supplier():
    def __init__(self, supplier_id, supplier_name, supplier_email):
        self._id = supplier_id
        self._name = supplier_name
        self._email = supplier_email

    def display_information(self):
        print (f'''
===Supplier Information===
Supplier ID: {self._id}
Supplier Name: {self._name}
Supplier Email Contact: {self._email}
==========================
        ''')

def test():
    Razer = Supplier('001', 'Razer', 'business@razer.com')
    Razer.display_information()
