from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish

coco_bambu = Restaurant("Coco Bambu", "Italian")
abbraccio = Restaurant("Abbraccio", "Mediterranean")
barbacoa = Restaurant("Barbacoa", "Steak house")

coco_bambu.make_assessment("João", 9.8)
abbraccio.make_assessment("Maria", 5.6)
barbacoa.make_assessment("José", 7.2)

juice = Drink("Orange Juice", 5.00)
pizza = Dish(
    "Pizza Margherita",
    30.00,
    "Traditional pizza with tomato sauce, mozzarella cheese, and fresh basil.",
)

coco_bambu.add_drink(pizza)
abbraccio.add_dish(juice)


def main():
    Restaurant.list_of_restaurants()


if __name__ == "__main__":
    main()
