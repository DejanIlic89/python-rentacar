# Brandovi: audi, bmw, mercedes
# Modeli: Audi: A4, A5, A6. BMW: M5, M3. Mercedes: GLK, GLE..

# BONUS:
# Modeli: Audi A4 (2004)...
# Svaki model ima godinu proizvodnje
# __production_year

class Car:
    VALID_CARS = {
        "Audi": [
            {"model": "A4", "production_year": 2004},
            {"model": "A5", "production_year": 2015},
            {"model": "A6", "production_year": 2010},
        ],
        "BMW": [
            {"model": "M3", "production_year": 2008},
            {"model": "M5", "production_year": 2006},
        ],
        "Mercedes": [
            {"model": "GLK", "production_year": 2015},
            {"model": "GLE", "production_year": 2016},
        ],
    }

    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__production_year = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("Brand cannot be None")
        # valid_models = []
        # for car in Car.VALID_CARS[self.__brand]:
        #     valid_models.append(car["model"])
        valid_models = [car["model"] for car in Car.VALID_CARS[self.__brand]]
        if model not in valid_models:
            raise ValueError("Invalid model value")
        self.__model = model

        for car_model in Car.VALID_CARS[self.__brand]:
            if car_model["model"] == model:
                self.__production_year = car_model["production_year"]

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand not in Car.VALID_CARS:
            raise ValueError("Invalid brand value")
        self.__brand = brand

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, year):
        if self.__model is None:
            raise ValueError("Production year cannot be set")
        if self.__model is not None and self.__production_year is not None:
            raise ValueError("Production year cannot be set twice")
        self.__production_year = year
