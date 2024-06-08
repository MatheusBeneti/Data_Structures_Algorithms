class Node:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.leftNode = None
        self.rightNode = None
        
    def addNode(self, node):
        if node.frequency < self.frequency:
            if self.leftNode is None:
                self.leftNode = node
            else:
                self.leftNode.addNode(node)

class TreeList:
    def __init__(self):
        self.treeList = []

    def add(self, node):
        self.treeList.append(node)
        self.treeList = sorted(self.treeList, key=lambda node: node.frequency)
    
        
    def getTree(self):
        return self.treeList[0]
            
    def createTree(self):
        while(len(self.treeList) > 1):
            newNode = Node(self.treeList[0].letter + self.treeList[1].letter, self.treeList[0].frequency + self.treeList[1].frequency)
            newNode.leftNode = self.treeList[0]
            newNode.rightNode = self.treeList[1]
            
            self.treeList.pop(0)
            self.treeList.pop(0)

            self.add(newNode)

class Compress:
    def __init__(self, text):
        self.text = text
        self.treeList = TreeList()
        self.__createNodes()
        self.__createCompressionTable()
        self.binaryText = self.__createBinaryText()

    def __createNodes(self):
        self.__frequency = self.__countFrequency(self.text)

        for letter in self.__frequency:
            self.treeList.add(Node(letter, self.__frequency[letter]))
        
        self.treeList.createTree()

    def __countFrequency(self, text):
        lettersList = {}

        for letter in text:
            if letter in lettersList:
                lettersList[letter] += 1
            else:
                lettersList[letter] = 1

        return lettersList
    
    def __createCompressionTable(self):
        rootTree = self.treeList.getTree()

        self.__compressionTable = {}

        self.__assignHuffmanCodes(rootTree, '')

    def __assignHuffmanCodes(self, node, code):
        if node is not None:
            # Adiciona no dicionário apenas os nós folhas (Simbolos indivíduais da tabela de compressão)
            if(len(node.letter) == 1):
                self.__compressionTable[node.letter] = code

            # Visite o filho esquerdo recursivamente
            self.__assignHuffmanCodes(node.leftNode,  code + '0')
            # Visite o filho direito recursivamente
            self.__assignHuffmanCodes(node.rightNode,  code + '1')
        
    def __createBinaryText(self):
        binary_text = ''
        for letter in self.text:
            binary_text += self.__compressionTable[letter]

        return binary_text
    
    def getBinaryText(self):
        return self.binaryText
    
    def getLettersCode(self):
        return self.__compressionTable
    
class Decompress:
    def __init__(self, compressed_text, letters_code):
        self.compressed_text = compressed_text
        self.letters_code = letters_code
        self.decoded_text = self.decompress()

    def decompress(self):
        decoded_text = ""
        current_code = ""
        for bit in self.compressed_text:
            current_code += bit
            for letter, code in self.letters_code.items():
                if code == current_code:
                    decoded_text += letter
                    current_code = ""
                    break
        return decoded_text

    def __repr__(self):
        return self.decoded_text

text = "abracadabra"
print("Texto original: ", text)

compress = Compress(text)
binaryText = compress.getBinaryText()
lettersCode = compress.getLettersCode()

print("O texto em binário: ", binaryText)
print("O codigo das letras ", lettersCode)

decompressedText = Decompress(binaryText, lettersCode)

print("O texto descomprimido: ", decompressedText)
