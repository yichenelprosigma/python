import math
# #una función con cuatro parámetros 

# def polinomio(numeroa,numerob,numeroc,x):
#     ecuación=numeroa*x**2+numerob*x+numeroc
#     print(ecuación)
    
# polinomio(2,3.7,-0.5,100)

#modificación
def polinomio(numeroa,numerob,numeroc):
    if math.sqrt(numerob**2-4*numeroa*numeroc) <0:
        print("No se puede hacer esta ecuación")
    else:
        #se puede mejorar 
        ecuación1=(-numerob+math.sqrt(numerob**2-4*numeroa*numeroc))/2*numeroa
        ecuación2=(-numerob-math.sqrt(numerob**2-4*numeroa*numeroc))/2*numeroa
        print(int(ecuación1))
        print(int(ecuación2))
        #print(f"{numero:.0f}"
        #print(f"{numero:.0f}"
        
polinomio(1,1,1)