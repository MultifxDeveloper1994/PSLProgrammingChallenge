
# el orden de ejecucion de este metodo es O(N) donde N es el numero de digitos del numero
# que es el peor caso cuando el numero si esta ordenado
def isSorted(number):
    stringNumber = str(number)
    for i in range(len(stringNumber) - 1 ):
       if (int(stringNumber[i]) > int(stringNumber[1+i])):
           return False   
    return True

## Cuando el numero ya esta ordenado el orden es O(N), dado que es el tiempo de ejecución del metodo O(N)
## El orden de ejecución de este metodo es O(N**2) en el peor de los casos, donde N es la longitud del numero.
## PEro dado que la restricción de digitos es de 18, no se evidencia demasiada demora, en comparación a si se hiciera
## por fuerza bruta donde el orden del algoritmo seria O(N*K) donde N seria el numero y K el numero de digitos
## que posee el numero 
def foundMaxSorted(num):
    if(isSorted(num)):
        return num    
    
    for i in range( 1 , len (str(num))+ 1):
        numero = num - (num % (10**i)) - 1
        if (isSorted(numero)):
            return numero        
    return 0

if __name__ == "__main__":
    inputFile = open("entrada.txt", "r")
    outputFile = open("salida.txt", "w")
    lines = inputFile.readlines()
    casos = int(lines[0])
    for i in range(1 , casos + 1 ):
        numero = int(lines[i])
        outputFile.write("Caso " + str(i) + ": N="  + str(numero) + ", O=" + str(foundMaxSorted(numero)) + "\n")

    inputFile.close()
    outputFile.close()


    
