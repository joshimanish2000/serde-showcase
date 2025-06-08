import requests

class CustomerAffinity:
    def __init__(self, customer_hash, product):
        self.customer_hash = customer_hash
        self.product = product
    
cust1 = CustomerAffinity("ahg89eb29", "some_product")
    
# This won't work. cust1 is not serialized.
res = requests.post("http://localhost:5000/affinity", cust1)
print("Res", res.text)