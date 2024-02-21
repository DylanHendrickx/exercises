
class CircularBuffer:
    def __init__(self, n):
        self.__n = n
        self.__buffer = []

    def add(self, item):
        if len(self.__buffer) < self.__n:
            self.__buffer.append(item)
        elif len(self.__buffer) == self.__n:
            del self.__buffer[0]
            self.__buffer.append(item)
    
    def __len__(self):
        return len(self.__buffer)
    
    def __getitem__(self, index):
        return self.__buffer[index]