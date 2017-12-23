class Stack:
    def __init__(self, capacity=2):
        """
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack.

        @pre: a capacity of the Stack, if no input is provided it will default to 2

        @post: initializes a Stack object

        This is the Stack constructor. It creates an object based on the capacity input or default value
        """
        self._capacity = capacity
        self._data = [0] * self._capacity
        self._size = 0

    def __str__(self):
        """
        Prints the elements in the stack from bottom of the stack to top,
        followed by the capacity.

        @pre: None

        @post: Returns the Stack object information in a string format

        This method returns the Stack object information in the following order: Bottom of stack to the top,
        and capacity
        """

        if self._size > 0:

            lst = [str(self._data[item]) for item in range(self._size)]
            str1 = str(lst) + " Capacity: " + str(self._capacity)

            return str1

        else:
            return "Empty Stack"

    def parse_input(self, instructions):
        """
        Parse the input given from the stream.

        @pre: An input, called instructions. It is expected to be push, pop, top, or replace

        @post: Based on the input, it calls the push, pop, top, or replace method

        This method takes in instructions and based on the word, calls one of a few methods based on the Stack object
        """

        input_ = instructions
        input_list = input_.strip().split()

        if input_list[0] == 'push':
            self.push(input_list[1])

        elif input_list[0] == 'pop':
            self.pop()

        elif input_list[0] == 'top':
            self.top()

        elif input_list[0] == 'replace':
            self.replace(input_list[1], input_list[2])

        else:
            pass

    def get_size(self):
        """
        Returns the number of items currently in the stack

        @pre: None

        @post: Returns the current size of the Stack object

        This method returns the current number of objects in the Stack
        """

        return self._size

    def is_empty(self):
        """
        Returns True if the stack is empty

        @pre: None

        @post: Returns True or False based on if the size of the Stack object is zero

        This method checks if the Stack object is empty
        """

        return self._size == 0

    def push(self, addition):
        """
        Adds an item to the top of the stack

        @pre: An input, called addition. This is what is added to the top of the Stack object

        @post: No return, the addition is added to the top of the Stack object

        This method adds the addition to the top of the Stack object, and calls the grow method if the Stack is full
        """

        if self._size < self._capacity:

            self._data[self._size] = addition
            self._size += 1

        else:
            self.grow()
            self.push(addition)

    def pop(self):
        """
        Removes and returns the top item from the stack
        Does nothing if stack is empty
        Reduces stack size if number of items is half capacity

        @pre: None

        @post: The top of the Stack object is removed and returned

        This method removes the top of the Stack object and returns it. If the size of the Stack object is half or less
        or the capacity, the shrink method is called
        """

        if not self.is_empty():

            half_cap = self._capacity // 2
            item = self._data[self._size-1]
            self._data[self._size-1] = 0
            self._size -= 1

            if self._size <= half_cap:
                if half_cap != 0:

                    self.shrink()

            return item

        else:
            pass

    def top(self):
        """
        Returns, but does not remove, the top item from the stack.
        Does nothing if stack is empty

        @pre: None

        @post: The top of the Stack object is returned

        This method returns the top of the Stack object, but does not remove it
        """

        if self.is_empty():
            pass

        else:
            return self._data[0]

    def grow(self):
        """
        Resize the stack to be 2 times its previous size.

        @pre: None

        @post: No return. The capacity of the Stack object is doubled

        This method doubles the capacity of the Stack object and does not do anything with the data within it
        """

        old = self._data
        self._capacity = 2 * self._capacity
        self._data = [0] * self._capacity

        for i in range(self._size):

            self._data[i] = old[i]

    def shrink(self):
        """
        Resize the stack to be half its current size.

        @pre: None

        @post: No return. The capacity of the Stack object is halved

        This method halves the capacity of the Stack object and does not do anything with the data within it
        """

        old = self._data
        self._capacity = self._capacity // 2
        self._data = [0] * self._capacity

        if len(old) >= 1:
            for i in range(self._size):

                self._data[i] = old[i]

    def replace(self, old_val, new_val):
        """
        For each old_ch in the stack, replace it
        with the new_ch.

        @pre: Two inputs, old_val and new_val.
            old_val: The value that is being replaced in the Stack object
            new_val: The value that ie replacing the old value in the Stack object

        @post: This method has no return. It just replaces the old_val with new_val in every occurrence within the
        Stack object

        This method changes all of the old_val into new_val and keeps the rest of the Stack object in the same order
        """

        temp_data = Stack(self._capacity)

        while not self.is_empty():
            check = self.pop()

            if check == old_val:
                check = new_val

            temp_data.push(check)

        while not temp_data.is_empty():
            self.push(temp_data.pop())
