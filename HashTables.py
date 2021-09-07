class HashTables:
    def __init__(self, size):
         self.data_map = [None] * size

    def __hash(self, key):
        my_hash=0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        
        if self.data_map[index] is not None:
            val = []
            for val in self.data_map[index]:
                if val[0] == key:
                    return val[1]
            del val

        return None
        
    def keys(self):
        key_list=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                        key_list.append(self.data_map[i][j][0])
        
        return key_list


    def printHashTable(self):
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)

    

if __name__ == "__main__":
    my_ht=HashTables(1000)
    
    my_ht.set('bolts',1400)
    my_ht.set('screws',2400)
    my_ht.set('phillip',1400)
    my_ht.set('lotbs',50)
    my_ht.set('ltbos',70)
    my_ht.set('lbost',90)
    my_ht.set('bostl',80)
    #print(my_ht.get('bostl'))
    #my_ht.printHashTable()
    print(my_ht.keys())
