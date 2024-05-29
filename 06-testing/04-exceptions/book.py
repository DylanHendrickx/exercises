class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def isbn(self):
        return self.__isbn  
    
    @title.setter
    def title(self, value):
        if value == "":
            return RuntimeError
        self.__title = value

    @isbn.setter
    def isbn(self, value):
        array = []
        for x in value:
            if x == " " or x == "-":
                break
            if x == 0 or x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7 or x == 8 or x == 9:
                array.append(x)
            
        if len(array) > 13:
            return RuntimeError
        
        for x in array:
            if x == 2 or x == 4 or x == 6 or x == 8:
                x *= 3

        total = sum(array)
        if total % 10 != 0:
            return RuntimeError
        return True