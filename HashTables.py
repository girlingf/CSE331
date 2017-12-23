class HashItem:
    """
    Type of item stored in the hash table, contains a key and a value
    """
    def __init__(self, key, value):
        """
        Initialize the HashItem
        :param key: Key of HashItem
        :param value: Value of HashItem
        """
        self.key = key
        self.value = value

    def __eq__(self, other):
        """
        Compares two HashItems
        :param other: Other HashItem
        :return: True if keys and values are the same
        """
        if isinstance(other, HashItem) and self.key == other.key and self.value == other.value:
            return True

        return False

    def __repr__(self):
        """
        String representation of HashItem
        :return: key and value as string
        """
        return self.key + ":" + str(self.value)


class HashTable:
    """
    Hash table class, utilizes list of lists of hash items, uses separate chaining
    """

    def __init__(self, tableSize = 7):
        """
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.tableSize = tableSize
        self.numItems = 0
        self.table = [[] for i in range(self.tableSize)]

    def __eq__(self, other):
        """
        defines what makes a hash table equal to another hash table
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.tableSize != other.tableSize:
            return False
        for i in range(self.tableSize):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]" + str(item) + '\n'
            bin_no += 1
        return represent

    def hash_function(self, x):
        """
        Simple function that converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0
        # hash code
        for ch in x:
            hashed_value = 37 * hashed_value + ord(ch)
        # compression function
        return hashed_value % self.tableSize

    def insert(self, key, value):
        """
        Insert HashItem into HashTable based on key, value arguments
        @pre: takes in a key and value
        @post: inserts the key value pair into the hash table
        This function inserts a key value pair in the hash table and increases the size if needed
        """
        if key != "":
            find = self.search(key)

            if find == 0:

                item = HashItem(key, value)
                hash_num = self.hash_function(key)
                self.table[hash_num] = [item] + self.table[hash_num]
                self.numItems += 1

            else:
                find.value = value

        load = self.numItems / self.tableSize

        if load > 1:
            self.double()

    def search(self, key):
        """
        Returns the HashItem in the table based on the key
        @pre: takes in a key
        @post: returns a HashItem if found, otherwise returns False
        This function searches for an input key and returns the item if it is found
        """
        index = self.hash_function(key)
        bucket = self.table[index]

        for item in bucket:
            if item.key == key:
                return item

        return False

    def get(self, key):
        """
        Returns value of HashItem
        @pre: takes in a key
        @post: returns the value of the corresponding HashItem
        This function performs similar to search, and returns the value of the given key
        """
        if self.search(key) == 0:
            return False

        else:
            index = self.hash_function(key)
            bucket = self.table[index]
            for item in bucket:
                if item.key == key:
                    return item.value

    def delete(self, key):
        """
        Deletes a HashItem from the HashTable given the key
        Returns true if successful, false if not
        @pre: takes in a key
        @post: returns True or False, based on if the deletion was successful
        This function uses search to see if the input key is in the hash table, and delete that HashItem if it is there
        """
        if self.search(key):
            index = self.hash_function(key)
            bucket = self.table[index]
            for item in bucket:
                if item.key == key:
                    bucket.remove(item)
                    self.numItems -= 1

                    load = self.numItems / self.tableSize

                    if load < (1/4):
                        self.half()

                    return True

        else:
            return False

    def double(self):
        """
        Doubles the size of the HashTable
        Rehashes all the values
        @pre: takes no inputs
        @post: doubles the size of the HashTable
        This function doubles the size of the HashTable and rehashes the items within it
        """
        self.tableSize = self.tableSize * 2
        self.rehash()

    def half(self):
        """
        Halves the size of the HashTable
        Rehashes all the values
        @pre: takes no inputs
        @post: halves the size of the HashTable
        This function halves the size of the HashTable and rehashes the items within it
        """
        self.tableSize = self.tableSize // 2
        self.rehash()

    def rehash(self):
        """
        Creates a new table with new size
        Hashes all the values from the old table to the new table
        @pre: takes no inputs
        @post: redistributes the items in the HashTable
        This function creates a new HashTable and redistributes the old items within it
        """
        new = HashTable(self.tableSize)
        self.numItems = 0
        elements = []
        for item in self.table:
            elements.extend(item)

        for item in elements:
            new.insert(item.key, item.value)
            self.numItems += 1

        self.table = new.table


class HashTableDouble:
    """
    Hash table class, uses double hashing
    """

    def __init__(self, tableSize = 7):
        """
        Initializes the table
        :param tableSize: Size of hash table
        """
        self.tableSize = tableSize
        self.numItems = 0
        self.table = ["" for i in range(self.tableSize)]

    def __repr__(self):
        """
        Represents the table as a string
        :return: string representation of a hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "][" + str(item) + "]" + '\n'
            bin_no += 1
        return represent

    def __eq__(self, other):
        """
        defines what makes a hash table equal to another hash table
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.tableSize != other.tableSize:
            return False
        for i in range(self.tableSize):
            if self.table[i] != other.table[i]:
                return False
        return True

    def hash_function(self, x):
        """
        Simple function that converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0
        for ch in x:
            hashed_value += 37 * hashed_value + ord(ch)
        return hashed_value % self.tableSize

    def insert(self, key, value):
        """
        Insert HashItem into hash table based on key, value arguments
        Returns True if successful, False if not
        @pre: takes a key and value as inputs
        @post: inserts the key value pair into the hash table
        This function inserts a key value pair in the hash table and increases the size if needed
        """
        if key != "":
            find = self.search(key)
            if find == 0:
                item = HashItem(key, value)
                hash_num = self.hash_function(key)

                if self.table[hash_num] == "":
                    self.table[hash_num] = item
                    self.numItems += 1

                else:
                    step = self.step_function(hash_num)
                    self.table[(step + hash_num) % self.tableSize] = item
                    self.numItems += 1

            else:
                find.value = value

            load = self.numItems / self.tableSize

            if load > 0.5:
                self.double()

            return True

        return False

    def double(self):
        """
        Doubles the size of the HashTable
        Rehashes all the values
        @pre: takes no inputs
        @post: the size of the HashTable is doubled
        This function doubles the size of the HashTable and rehashes the items
        """
        self.tableSize = self.tableSize * 2
        self.rehash()

    def half(self):
        """
        Halves the size of the HashTable
        Rehashes all the values
        @pre: takes no inputs
        @post: the size of the HashTable is halved
        This function halves the size of the HashTable and rehashes the items
        """
        self.tableSize = self.tableSize // 2
        self.rehash()

    def rehash(self):
        """
        Creates a new table with new size
        Hashes all the values from the old table to the new table
        @pre: takes no inputs
        @post: redistributes the items in the HashTable
        This function creates a new HashTable and redistributes the old items within it
        """
        new = HashTableDouble(self.tableSize)
        self.numItems = 0

        for item in self.table:
            if item:
                new.insert(item.key, item.value)
                self.numItems += 1

        self.table = new.table

    def step_function(self, key):
        """
        Step size must be relatively prime to table size for maximum efficiency
        Cannot be zero
        :param key: Key to hash
        :return: step number for double hashing
        """
        number = 7 - (key % 7)
        while True:
            if self.relatively_prime(number, self.tableSize):
                return number
            number = number - 1

    def relatively_prime(self, a, b):
        """
        Returns true if a is relatively prime to b
        :param a: First number
        :param b: Second number
        :return: True if a is relatively prime to b
        """
        while b != 0:
            t = a
            a = b
            b = t % b
        return a == 1

    def search(self, key):
        """
        Returns the HashItem in the table based on the key, if it exists
        Otherwise, returns False
        @pre: takes a key as an input
        @post: returns a HashItem if found, otherwise returns False
        This function searches for an input key and returns the item if it is found
        """
        index = self.hash_function(key)  #bucket index number
        bucket = self.table[index]

        if bucket != "":
            if bucket.key == key:
                return bucket

        return False

    def delete(self, key):
        """
        Deletes a HashItem from the HashTable given the key
        Returns true if successful, false if not
        @pre: takes a key as an input
        @post: returns True or False, based on if the deletion was successful
        This function uses search to see if the input key is in the hash table, and delete that HashItem if it is there
        """
        if self.search(key):
            index = self.hash_function(key)
            bucket = self.table[index]
            if bucket != "":
                if bucket.key == key:
                    self.table[index] = ""
                    self.numItems -= 1

                    load = self.numItems / self.tableSize

                    if load < (1/4):
                        self.half()

                    return True

        else:
            return False

    def get(self, key):
        """
        Returns value of HashItem
        Returns False if it's not in the HashTable
        @pre: takes a key as an input
        @post: returns the value of the corresponding HashItem
        This function performs similar to search, and returns the value of the given key
        """
        if self.search(key) == 0:
            return False

        else:
            index = self.hash_function(key)  # List of HashItem objects
            bucket = self.table[index]  # HashItem object

            if bucket != "":
                if bucket.key == key:

                    return bucket.value
