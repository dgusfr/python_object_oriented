class Restaurant:
    def __init__(self, name, cuisine_type, status):
        self.name = name
        self.cuisine_type = cuisine_type
        self.status = status


coco_bambu = Restaurant("Coco Bambu", "Italian", "Open")

print(coco_bambu)
