import math

def disc(a, b, c):
    """This function is used to resolve equation of degree 2
    """
    print("*"*10)
    delta = b**2 - 4*a*c
    print(delta)
    
    if delta > 0 :
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print(f"There are two real solutions, x1 = {x1} and x2 = {x2}.")

    if delta == 0 : 
        x0 = -b / (2*a)
        print(f"There is one real solution, x0 = {x0}.")
    
    if delta < 0 :
        print(f"There are two complex solutions.\nx1 = {-b} + i*sqrt({delta}) / (2*{a}) \nx2 = {-b} - i*sqrt({delta}) / (2*{a}).")

    print("Scipt successfully completed\n***********")

if __name__ == '__main__' :
    disc(20, 4, 1)