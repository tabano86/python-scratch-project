import enum


class FieldName(enum.Enum):
    name = "name"
    rating = "rating"
    brand = "brand"


class Whisky:
    name: str
    rating: int
    country: str
    category: str
    price: float
    abv: int
    age: int
    brand: str

    def __init__(self, name, rating, country, category, price, abv, age, brand) -> None:
        self.name = name
        self.rating = rating
        self.country = country
        self.category = category
        self.price = price
        self.abv = abv
        self.age = age
        self.brand = brand