import math
class Triangle:
    catetos = [0,0]

    def __init__(self, cateto_a, cateto_b):
        self.catetos[0] = cateto_a
        self.catetos[1] = cateto_b

    def verify_if_catetos_are_empty(self):
        if self.catetos[0] != 0 and self.catetos[1] != 0:
            return True
        return False
    
    def calculate_hypotenuse(self):
        return math.hypot(self.catetos[0], self.catetos[1])
