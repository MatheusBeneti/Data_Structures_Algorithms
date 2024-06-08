import random

def generateArray():
    return [random.randint(0, 100) for _ in range(100)]
    #return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 19, 19, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def sequencialSearch(array, target):
    NumberOfChecks = 0
    for i in range(len(array)):
        NumberOfChecks += 1
        if array[i] == target:
            return i, NumberOfChecks
        
def sequencialSearchAll(array, target):
    NumberOfChecks = 0
    positions = []
    for i in range(len(array)):
        NumberOfChecks += 1 
        if array[i] == target:
            positions.append(i)
    return positions, NumberOfChecks

def binarySearch(array, target):
    Beginning = 0
    End = len(array) - 1
    NumberOfChecks = 0

    OrderedArray = array
    OrderedArray.sort()


    while True:
        Middle = (Beginning + End) // 2 

        NumberOfChecks += 1
        if OrderedArray[Middle] == target:
            return Middle, NumberOfChecks  
        elif OrderedArray[Middle] < target: 
            Beginning = Middle + 1 #Move o inicio para o meio + 1
        else:
            End = Middle - 1 #Move o fim para o meio - 1

def binarySearchAll(array, target):
    positions = []
    
    orderedArray = array
    orderedArray.sort()
    
    Beginning = 0
    End = len(array) - 1
    numberOfChecks = 0

    while Beginning <= End:
        Middle = (Beginning + End) // 2

        numberOfChecks += 1
        if orderedArray[Middle] == target:
            left_index = right_index = Middle
            positions.append(Middle)

            numberOfChecks += 1
            while left_index > 0 and orderedArray[left_index - 1] == target:
                left_index -= 1
                positions.append(left_index)
                numberOfChecks += 1

            numberOfChecks += 1
            while right_index < len(orderedArray) - 1 and orderedArray[right_index + 1] == target:
                right_index += 1
                positions.append(right_index)
                numberOfChecks += 1

            return positions, numberOfChecks

        numberOfChecks += 1
        if orderedArray[Middle] < target:
            Beginning = Middle + 1
        else:
            End = Middle - 1

    return positions, numberOfChecks
  
def main():

    array = generateArray()
    print("\nArray gerado:", array, "\n")

    while(True):
        target = int(input("Digite o valor a ser buscado: "))
        print("\n----------------------------------------------------------------")

        print("Busca sequencial. Achar um valor específico\n")
        position, NumberOfChecks = sequencialSearch(array, target)        
        print("Posição do valor buscado:", position)
        print("Número de comparações:", NumberOfChecks)
        print("----------------------------------------------------------------")

        position = []
        NumberOfChecks = 0

        print("Busca sequencial. Achar todas as ocorrencias de um valor específico\n")
        position, NumberOfChecks = sequencialSearchAll(array, target)
        print("Posição do valor buscado:", position)
        print("Número de comparações:", NumberOfChecks)
        print("----------------------------------------------------------------")

        position = []
        NumberOfChecks = 0

        print("Busca binária. Achar um valor específico\n")
        position, NumberOfChecks = binarySearch(array, target)
        print("Posição do valor buscado:", position)
        print("Número de comparações:", NumberOfChecks)
        print("----------------------------------------------------------------")

        position = []
        NumberOfChecks = 0

        print("Busca binária. Achar todas as ocorrencias de um valor específico\n")
        position, NumberOfChecks = binarySearchAll(array, target)
        print("Posição do valor buscado:", position)
        print("Número de comparações:", NumberOfChecks)
        print("----------------------------------------------------------------")

main()