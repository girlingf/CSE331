class CircularQueue(object):
    def __init__(self, capacity=2):
        """
        Initialize the queue to be empty with a fixed capacity
        :param capacity: Initial size of the queue

        @pre: a capacity of the circular queue, if no input is provided it will default to 2

        @post: initializes a CircularQueue object

        This is the CircularQueue constructor. It creates an object based on the capacity input or default value
        """
        self._capacity = capacity
        self._size = 0
        self._list = [None] * self._capacity
        self._sum = 0
        self._read = 0
        self._write = 0

    def __str__(self):
        """
        Return a string representation of RunningQueue
        :return: string

        @pre: None

        @post: returns the CircularQueue object information in a string format

        This method returns the CircularQueue object information in the following order: numbers from read to draw,
        sum of the numbers, and current capacity
        """

        if self._size > 0:
            str1 = ""

            if self._write > self._read:
                for i in self._list[self._read:self._write]:
                    i = str(i)
                    str1 = str1 + i + " "

            else:
                for j in self._list[self._read:]:
                    j = str(j)
                    str1 = str1 + j + " "

                for k in self._list[:self._write]:
                    k = str(k)
                    str1 = str1 + k + " "

            str1 = str1.replace("None", "")
            str1 = str1.strip()
            str1 = str1 + " Sum:" + str(self._sum) + " Capacity:" + str(self._capacity)

            return str1

        else:
            return "Queue is Empty"

    def parse_command(self, command):
        """
        Parse command given from the input stream
        :param command: command from input stream
        :return: None

        @pre: An input, called command. It is expected to be an 'a' or 'r'

        @post: Based on the input, either enqueue or dequeue. No return

        This method takes in a command and based on the letter, enqueue or dequeues from the CircularQueue
        """

        input_ = command
        input_list = input_.strip().split()

        if input_list[0] == 'a':
            self.enqueue(input_list[1])

        elif input_list[0] == 'r':
            self.dequeue()
        else:
            pass

    def enqueue(self, number):
        """
        Add a number to the end of the queue
        :param number: number to add
        :return: None

        @pre: a number to enqueue to the CircularQueue

        @post: The number is attached to the end of the CircularQueue. No return

        This method attaches the number to the end of the CircularQueue and increases its variables
        """

        if self._size == self._capacity:
            self.resize()

        self._list[self._write % self._capacity] = number
        self._size += 1
        self._sum = self._sum + int(number)
        self._write = (self._write + 1) % len(self._list)

    def dequeue(self):
        """
        Remove an element from the front of the queue
        Do nothing if the queue is empty
        :return: None

        @pre: None

        @post: Removes the first element from the CircularQueue. No return

        This method removes the first element from the CircularQueue and changes its variables accordingly
        """

        if self._size < 1:
            pass

        else:
            self._sum = self._sum - int(self._list[self._read])
            self._list[self._read] = None
            self._read = (self._read + 1) % len(self._list)
            self._size -= 1

    def resize(self):
        """
        Resize the queue to be two times its previous size
        :return: None

        @pre: None

        @post: Doubles the capacity of the CircularQueue and changes the read and write pointers accordingly

        This method is called when the CircularQueue is full. It doubles the capacity and copies the old values over
        in the correct order, changing the read and write pointers to match the new capacity
        """

        old = self._list
        self._write = self._capacity
        self._capacity = self._capacity * 2
        self._list = [None] * self._capacity
        count = self._read

        for i in range(self._size):
            self._list[i] = old[count]
            count = (count + 1) % len(old)

        self._read = 0

    def get_sum(self):
        """
        Get the sum of the numbers currently in the queue
        :return: sum of the queue

        @pre: None

        @post: Returns the sum of the numbers in the CircularQueue

        This method returns the sum of the numbers in the CircularQueue that is tracked when using enqueue or dequeue
        """

        return self._sum

