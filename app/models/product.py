from dataclasses import dataclass

@dataclass
class Category:
    category_name : str 

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    amount: int
    category: Category  # what type goes here?

    def __post_init__(self):
        # enforce the validity rules we agreed on
        # what should happen if a rule is violated?
        if self.amount <0:
            raise ValueError("the amount should be zero or positive")
        if self.price <0 :
            raise ValueError("the price should be zero or positive")
        if self.name.strip() == "":
            raise ValueError("name can't be empty")


