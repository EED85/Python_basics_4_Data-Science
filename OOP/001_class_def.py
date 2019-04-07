
#%% [markdown]

# # Define a simple class with class attributes
class Pizza(object):
    def __init__(self, size, toppings, price, rating):
        self.size = size
        self.toppings = toppings
        self.price = price
        self.rating = rating


#%% [markdown]
myPizza = Pizza(size= "L",toppings = "Olive",price = 15,rating = 5)

print(myPizza.price)