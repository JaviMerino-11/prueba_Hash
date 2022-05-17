class Circle1(object):
    def __init__(self, coord_x, coord_y, radio):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.radio = radio

    def hash(self):
        return hash((self.coord_x, self.coord_y, self.radio))


class Circle2(object):
    def __init__(self, coord_x, coord_y, radio):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.radio = radio
        self.id_x = id(self.coord_x)
        self.id_y = id(self.coord_y)
        self.id_radio = id(self.radio)

    def hash_id(self):
        return hash((self.id_x, self.id_y, self.id_radio))


def main():
    instance_1_circ_1 = Circle1(1, 2, 3)
    instance_2_circ_1 = Circle1(1, 2, 3)

    instance_1_circ_2 = Circle2(1, 2, 3)
    instance_2_circ_2 = Circle2(1, 2, 3)

    set_instances = {instance_1_circ_1.hash(), instance_2_circ_1.hash(), instance_1_circ_2.hash_id(),
                     instance_2_circ_2.hash_id()}
    print(set_instances)

    if instance_1_circ_1.hash() == instance_2_circ_1.hash():
        print(
            'Los hash sobre los contenidos de dos instancias de la misma clase son iguales y es %i' % instance_1_circ_1.hash())
    else:
        print('Los hash sobre los contenidos de dos instancias de la misma clase NO son iguales')

    if instance_1_circ_2.hash_id() == instance_2_circ_2.hash_id():
        print(
            'Los hash sobre el ID de dos instancias de la misma clase son iguales y es %i' % instance_1_circ_2.hash_id())
    else:
        print('Los hash sobre el ID de dos instancias de la misma clase NO son iguales')


if __name__ == '__main__':
    main()
