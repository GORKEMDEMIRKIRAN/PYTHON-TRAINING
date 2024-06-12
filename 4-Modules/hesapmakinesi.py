


# CALCULATOR

import math


def calculator(value,number):
        if (number==1):
            return math.log(value)
        elif (number==2):
            return math.log(value)
        elif (number==3):
            return math.log(value)
        elif (number==4):
            return math.log(value)
        elif (number==5):
            return math.log(value)
            

while True:
    print("""
          1-logaritma
          2-karekök
          3-faktöriyel
          4-gamma
          5-mutlak değer
          """)
    variable=float(input("ENTER THE VALUE: "))
    value=int(input("ENTER THE PROCESS NUMBER: "))
    if (variable=="e"):
        break
    else:
        print(calculator(variable,value))
        
    
        

        