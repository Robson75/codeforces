import math


class GlebAndPizza:
    pass


if __name__ == "__main__":

    pizza_info = list(map(int, input().split()))
    pizza_radius = pizza_info[0]
    crust_width = pizza_info[1]
    pieces_of_sausage = int(input())
    sausages_on_crust = 0
    for sausage in range(pieces_of_sausage):
        sausage_info = list(map(int, input().split()))
        sausage_x = sausage_info[0]
        sausage_y = sausage_info[1]
        sausage_radius = sausage_info[2]
        sausage_radial_pos = math.sqrt(sausage_x * sausage_x + sausage_y * sausage_y)
        if (pizza_radius - crust_width <= sausage_radial_pos - sausage_radius
                and sausage_radial_pos + sausage_radius <= pizza_radius):
            sausages_on_crust += 1
    print(sausages_on_crust)
