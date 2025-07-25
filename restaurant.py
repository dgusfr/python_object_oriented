class Restaurant:
    restaurants = []

    def __init__(self, name, cuisine_type, status):
        self.name = name
        self.cuisine_type = cuisine_type
        self.status = status
        self.add_restaurant()

    def __str__(self):
        return f"Restaurant Name: {self.name}, Cuisine Type: {self.cuisine_type}, Status: {self.status}"

    def add_restaurant(self):
        Restaurant.restaurants.append(self)

    @classmethod
    def list_of_restaurants(cls):
        for restaurant in cls.restaurants:
            print(
                f"{restaurant.name} - {restaurant.cuisine_type} - {restaurant.status}"
            )

    @property
    def is_open(self):
        return "Open" if self.status else "Closed"


coco_bambu = Restaurant("Coco Bambu", "Italian", "Open")
abbraccio = Restaurant("Abbraccio", "Mediterranean", "closed")

Restaurant.list_of_restaurants()
coco_bambu.is_open
abbraccio.is_open
