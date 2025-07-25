class Restaurant:
    def __init__(self, name, cuisine_type, status):
        self.name = name
        self.cuisine_type = cuisine_type
        self.status = status

    def __str__(self):
        return f"Restaurant Name: {self.name}, Cuisine Type: {self.cuisine_type}, Status: {self.status}"

    def list_of_restaurants(self):
        for restaurant in Restaurant.restaurants:
            print(
                f"{restaurant.name} - {restaurant.cuisine_type} - {restaurant.status}"
            )


coco_bambu = Restaurant("Coco Bambu", "Italian", "Open")
abbraccio = Restaurant("Abbraccio", "Mediterranean", "closed")

restaurants = [coco_bambu, abbraccio]
restaurants.list_of_restaurants()

print(coco_bambu)
