from circles_classes.circles import Circles


class Circle2(Circles):

    def __hash__(self):
        return hash((id(self)))
