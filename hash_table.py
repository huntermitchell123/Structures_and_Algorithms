# An implementation of a hash table in python :)

class HashTable:
    def __init__(self,max_size=100):
        self.MAX = max_size
        self.arr = [None for i in range(self.MAX)] # initialize array with null values

    def get_hash(self,key): # return hash of value
        h = 0
        for i in key: # add the ascii of each character, then mod by array size
            h += ord(i)
        return h % self.MAX
    
    def add(self,key,value): # puts value at hash position of key
        hash = self.get_hash(key)
        self.arr[hash] = value

    def get(self,key): # gets the value at hash position of key
        hash = self.get_hash(key)
        return self.arr[hash]

    def __setitem__(self,key,value): # overrides basic set operation and puts value at hash position of key
        hash = self.get_hash(key)
        self.arr[hash] = value

    def __getitem__(self,key): # overrides basic get operation and gets the value at hash position of key
        hash = self.get_hash(key)
        return self.arr[hash]



def main():

    hash_table = HashTable()

    # trying out adding and getting key/values 
    hash1 = hash_table.get_hash('hunter')
    print('Hash of \'hunter\':',hash1)
    hash_table.add('hunter',22)
    print('Hash table value at', hash1, ':', hash_table.get('hunter'))

    hash_table.add('mitchell',30)
    print(hash_table.get('mitchell'))

    # returns None for keys we haven't added
    print(hash_table.get('something_else'))

    # can also do it this way since we overrided
    hash_table['another_name'] = 45
    print(hash_table['another_name'])


if __name__=="__main__":
    main()