class Restaurant:
    def __init__(self, name, cuisine_type, status):
        self.name = name
        self.cuisine_type = cuisine_type
        self.status = status

    def __str__(self):
        return f"Restaurant Name: {self.name}, Cuisine Type: {self.cuisine_type}, Status: {self.status}"


coco_bambu = Restaurant("Coco Bambu", "Italian", "Open")

print(coco_bambu)
