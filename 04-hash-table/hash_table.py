class HashTable:
    
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        value = 0
        for i in range(0, len(string)):
            value += ord(string[i])
        return value

    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value
        
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
        
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        else:
            return None