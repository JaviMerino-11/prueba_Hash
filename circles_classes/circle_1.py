from circles_classes.circles import Circles


class Circle1(Circles):

    def __hash__(self):
        return hash((self.coord_x, self.coord_y, self.radio))
