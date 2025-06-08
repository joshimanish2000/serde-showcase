import pickle

class CustomerAffinity:
    def __init__(self, customer_id, product):
        self.customer_id = customer_id
        self.product = product
    
cust1 = CustomerAffinity("ahg89eb29", "some_product")

# This will work. Pickle serialization.
with open("customer_affinity.txt", "wb") as file:
    file.write(pickle.dumps(cust1))