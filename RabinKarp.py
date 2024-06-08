class NaiveStringMatcher:
    def __init__(self, text, keyWord):
        self.text = text
        self.keyWord = keyWord

    def search(self):
        position = []
        for i in range(len(self.text) - len(self.keyWord) + 1):
            j = 0
            while j < len(self.keyWord) and (self.keyWord[j] == self.text[i + j] or self.keyWord[j] == '*'):
                j += 1
            if j == len(self.keyWord):
                position.append(str(i))
        return position

#def main():
    #text = "abracadabra"
    #keyWord = "a*a"
    #matcher = NaiveStringMatcher(text, keyWord)
    #result = matcher.search()
    #print("Palavra encontrada nas posições:", result)

                
class RabinkarpStringMatcher:
    def __init__(self, text, keyWords):
        self.__text = text
        self.__keyWords = keyWords
        self.__hashedKeyWords = self.__hashSetWords__()

    def __hashSetWords__(self):
        hashed_words = []
        for keyword in self.__keyWords:
            hashed_words.append(self.__hash__(keyword))
        return hashed_words
    
    def __hash__(self, string):
        primo = 101
        hashValue = 0
        for char in string:
            hashValue = (hashValue * primo + ord(char)) % primo
        return hashValue

    def search(self):
        for keyWord in self.__keyWords:
            keyWordLength = len(keyWord)
            text_length = len(self.__text)
            
            for i in range(text_length - keyWordLength + 1):
                pattern = ""
                for j in range(keyWordLength):
                    pattern += self.__text[i + j]

                patternHashed = self.__hash__(pattern)

                if patternHashed in self.__hashedKeyWords and pattern == keyWord:
                    print("Palavra encontrada na posição:", i, ":", keyWord)

def main():
    text = "No coração de uma cidade vibrante, onde as luzes da metrópole dançam ao ritmo do progresso, surge uma sinfonia de diversidade e inovação. Entre arranha-céus imponentes e vielas pitorescas, a vida urbana floresce em todas as suas formas. Cada esquina conta uma história única, entrelaçando passados distintos e futuros promissores."
    keyWords = ["uma", "cidade", "vida", "passados"]
    rabin = RabinkarpStringMatcher(text, keyWords)
    rabin.search()

main()