class Circles(object):
    def __init__(self, coord_x, coord_y, radio, name):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.radio = radio
        self.name = name

    def __repr__(self):
        return self.name
