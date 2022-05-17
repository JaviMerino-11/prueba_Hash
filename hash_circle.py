from circles_classes.circle_1 import Circle1
from circles_classes.circle_2 import Circle2


def main():
    instance_1_circ_1 = Circle1(1, 2, 3, 'circulo1_1')
    instance_2_circ_1 = Circle1(1, 2, 3, 'circulo2_1')

    instance_1_circ_2 = Circle2(1, 2, 3, 'circulo1_2')
    instance_2_circ_2 = Circle2(1, 2, 3, 'circulo2_2')

    set_instances = {instance_1_circ_1, instance_2_circ_1, instance_1_circ_2, instance_2_circ_2}
    # print(instance_1_circ_1, instance_2_circ_1, instance_1_circ_2, instance_2_circ_2)
    print(set_instances)


if __name__ == '__main__':
    main()
