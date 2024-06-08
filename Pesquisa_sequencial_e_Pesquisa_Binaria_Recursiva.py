import random

# Todas as buscas atualizadas para recursividade

def generateArray():
    return [random.randint(0, 100) for _ in range(100)]
    #return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 19, 19, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def sequencialSearch(array, target, index=0, NumberOfChecks=0):
    if index == len(array):
        return -1, NumberOfChecks
    if array[index] == target:
        return index, NumberOfChecks 
    return sequencialSearch(array, target, index + 1, NumberOfChecks + 1)  
            
def sequencialSearchAll(array, target, index=0, NumberOfChecks=0, positions=[]):

    if index == len(array):
        return positions, NumberOfChecks
    if array[index] == target:
        positions.append(index)
    return sequencialSearchAll(array, target, index + 1, NumberOfChecks + 1, positions)

def binarySearch(array, target, beginning=0, end=None, NumberOfChecks=0):
    if end is None:
        end = len(array) - 1

    if beginning <= end:
        middle = (beginning + end) // 2
        NumberOfChecks += 1

        if array[middle] == target:
            return middle, NumberOfChecks
        elif array[middle] < target:
            return binarySearch(array, target, middle + 1, end, NumberOfChecks)
        else:
            return binarySearch(array, target, beginning, middle - 1, NumberOfChecks)
    else:
        return -1, NumberOfChecks 

def binarySearchAll(array, target, beginning=0, end=None, positions=[], numberOfChecks=0):
    if end is None:
        end = len(array) - 1

    if beginning <= end:
        middle = (beginning + end) // 2
        numberOfChecks += 1

        if array[middle] == target:
            left_index = right_index = middle
            positions.append(middle)

            numberOfChecks += 1
            while left_index > 0 and array[left_index - 1] == target:
                left_index -= 1
                positions.append(left_index)
                numberOfChecks += 1

            numberOfChecks += 1
            while right_index < len(array) - 1 and array[right_index + 1] == target:
                right_index += 1
                positions.append(right_index)
                numberOfChecks += 1

            return positions, numberOfChecks

        elif array[middle] < target:
            return binarySearchAll(array, target, middle + 1, end, positions, numberOfChecks)
        else:
            return binarySearchAll(array, target, beginning, middle - 1, positions, numberOfChecks)
    else:
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
        position, NumberOfChecks = binarySearch(sorted(array), target)
        print("Posição do valor buscado:", position)
        print("Número de comparações:", NumberOfChecks)
        print("----------------------------------------------------------------")

        position = []
        NumberOfChecks = 0

        print("Busca binária. Achar todas as ocorrencias de um valor específico\n")
        position, NumberOfChecks = binarySearchAll(sorted(array), target)
        print("Posição do valor buscado:", position)
        print("Número de comparações:", NumberOfChecks)
        print("----------------------------------------------------------------")

main()