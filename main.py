class BaseComponent:
    def __init__(self, percent_fat: float, percent_sugar: float, percent_snf: float, percent_stabilizer, quantity: float):
        """
        The base class for an ice cream component
        :param perfect_fat: The per
        """
        self.percent_fat = percent_fat
        self.percent_snf = percent_snf
        self.percent_stabilizer = percent_stabilizer
        self.percent_sugar = percent_sugar

        self.quantity = quantity


class Mix:
    def __init__(self, total_mass) -> None:
        
        self.total_mass

