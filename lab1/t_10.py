import sys
import math

_, a, b, c = sys.argv
a = int(a)
b = int(b)
c = int(c)

def quadratic_solver():
    d = b**2-4*a*c
    if d < 0:
        return('no solutions')
    elif d == 0:
        x = -b/2*a
        return(f'solutions: {x}')
    else:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        return(f'solutions: {x1}, {x2}')

def main():
    print(quadratic_solver())    

if __name__ == '__main__':
    main()