# Program that calculates the number of paint Cans needed to paint a wall
# Given that 1 Can of paint can cover 5 square meter of wall.
# Given random height and width of wall, calculate how many cans of paints you'll need to buy.
# number of cans = (wall height * wall width ) / Coverage per can
# e.g height = 2, width = 4, coverage = 5
# number of cans = (2 * 4)/5 = 1.6
# but because you can't buy 0.6 of a Can of paint, the result shoul be rounded up to 2 cans.


import math #import the math module 
def paint_calc(height, width, cover): 
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)