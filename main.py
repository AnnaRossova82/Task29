BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]
        if capacity < 1:
            raise ValueError
        self._pairs = capacity * [None]

    def __len__(self):
        return len(self.values)

    def _index(self, key):
        return hash(key) % len(self)

    def __setitem__(self, key, value):
        self.values[self._index(key)] = value
        index = self._index(key)
        if self.values[index] is BLANK:
            self.values[self._index(key)] = value
        else:
            while index < len(self) and self.values[index] is not BLANK:
                index += 1
            else:
                IndexError("No more space left")

    def __getitem__(self, key):
        value = self.values[self._index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value

    def __delitem__(self, key):
        self.values[self._index(key)] = BLANK

    def __contains__(self, key):
         try:
             self[key]
         except KeyError:
             return False
         else:
             return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        index = hash(key) % len(self)
        self.values[index] = BLANK

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

if __name__ == "__main__":
    ht=HashTable(7)
    print(len(ht))
    ht['b']=777
    ht['c']=9
    print(ht.values)
    print(ht['b'])