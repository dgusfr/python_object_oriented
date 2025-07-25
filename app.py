from models.restaurant import Restaurant

coco_bambu = Restaurant("Coco Bambu", "Italian")
abbraccio = Restaurant("Abbraccio", "Mediterranean")
barbacoa = Restaurant("Barbacoa", "Steak house")

abbraccio.make_assessment("João", 9.8)


def main():
    Restaurant.list_of_restaurants()


if __name__ == "__main__":
    main()
