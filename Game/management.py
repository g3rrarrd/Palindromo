class management:

    def __init__(self):
        self.__word__= []

    def set_word(self, word):
        for letter in word:
            self.__word__.append(letter.lower())
        

    def validator(self, word):
        self.set_word(word)
        long = len(self.__word__)
        for i in range(long//2):
            if(self.__word__[i] != self.__word__[long - 1]):
                return False
            long -=1
        return True