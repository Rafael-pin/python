from model.Triangle import Triangle

triangle = Triangle(0,0)

while not triangle.verify_if_catetos_are_empty():
    try:
        triangle.catetos[0] = float(input('Type the first cateto: '))
        triangle.catetos[1] = float(input('Type the second cateto: '))
        print('The hypotenuse is: {}!'.format(triangle.calculate_hypotenuse()))
    except ValueError:
        print("Only numbers are accept")
