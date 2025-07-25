from models.assessment import Assessment


class Restaurant:
    restaurants = []

    def __init__(self, name, cuisine_type, assessment):
        self.name = name
        self.cuisine_type = cuisine_type
        self._status = True
        self._assessment = []
        self.add_restaurant()

    def __str__(self):
        return f"Restaurant Name: {self.name}, Cuisine Type: {self.cuisine_type}, Status: {self.status}"

    def add_restaurant(self):
        Restaurant.restaurants.append(self)

    @classmethod
    def list_of_restaurants(cls):
        print(
            f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}"
        )
        for restaurant in cls.restaurants:
            print(
                f"{restaurant.name.ljust(25)} - {restaurant.cuisine_type.ljust(25)} - {restaurant.is_open.ljust(25)}"
            )

    @property
    def is_open(self):
        return "Open" if self._status else "Closed"

    def turn_status(self):
        self._status = not self._status
        print(f"{self.name} is now {'open' if self._status else 'closed'}.")

    def make_assessment(self, client, rate):
        assessment = Assessment(client, rate)
        self._assessment.append(assessment)

    def show_assessment(self, assessments):
        if not self._assessment:
            return "The restaurant has no reviews"
        for assessment in _assessments:
            print(assessment)
