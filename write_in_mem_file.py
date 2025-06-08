class CustomerAffinity:
    def __init__(self, customer_id, product):
        self.customer_id = customer_id
        self.product = product
    
cust1 = CustomerAffinity("ahg89eb29", "some_product")

# This won't work. cust1 is not serialzed.
with open("customer_affinity.txt", "w") as file:
    file.write(cust1)