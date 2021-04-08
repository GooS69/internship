from task11 import Dessert

class JellyBean(Dessert):
    flavor = ""

    def set_flavor(self, flavor):
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor

    def is_delicious(self):
        return not (self.flavor == "black licorice")