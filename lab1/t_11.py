import argparse
import math
import cmath

parser = argparse.ArgumentParser(description='quadratic solver')
parser.add_argument(
    'av',
    type=float,
    default=0,
    help='a'
)
parser.add_argument(
    'bv',
    type=float,
    default=0,
    help='b'
)
parser.add_argument(
    'cv',
    type=float,
    default=0,
    help='c'
)
parser.add_argument(
    '-c',
    '--complex',
    type=bool,
    default=False,
    help='condition for complex solution'
)


var_ns = parser.parse_args()
a = var_ns.av
b = var_ns.bv
c = var_ns.cv
complex = var_ns.complex

def quadratic_solver():
    d = b**2-4*a*c
    if complex == False:
        if d < 0:
            return('no solutions')
        elif d == 0:
            x = -b/2*a
            return(f'solutions: {x}')
        else:
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            return(f'solutions: {x1}, {x2}')
    else:
        x1 = (-b+cmath.sqrt(d))/(2*a)
        x2 = (-b-cmath.sqrt(d))/(2*a)
        return(f'solutions: {x1}, {x2}')

def main():
    print(quadratic_solver())    

if __name__ == '__main__':
    main()