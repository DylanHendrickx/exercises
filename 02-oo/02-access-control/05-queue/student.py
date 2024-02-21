
class Queue:
    def __init__(self):
        self.__queue_list = []

    def add(self, item):
        self.__queue_list.append(item)

    def next(self):
        item = self.__queue_list[0]
        del self.__queue_list[0]
        return item
    
    def is_empty(self):
        if len(self.__queue_list) == 0:
            return True
        return False