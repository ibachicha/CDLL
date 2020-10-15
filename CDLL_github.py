# Course: CS261 - Data Structures
# Student Name: Isaac Bachicha
# Assignment: Assignment 3, Part 3
# Description: Implements a Deque and Bag ADT interfaces with a circular doubly linked list data.


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None: #good
        """
        This method adds a new node at the beginning of the list (right after the front sentinel).
        """
        new_node = DLNode(value)

        #if the list is empty, set 4 pointers to add node into list to complete circle
        if self.sentinel.next == self.sentinel:
            new_node.next = self.sentinel # link from new_node to the next sentinel
            new_node.prev = self.sentinel # " " " to the previous sentinel
            self.sentinel.next = new_node # link from the sentinel to the next forward new_node for complete circle
            self.sentinel.prev = new_node # " " " to the previous new_node for complete circle

        #else, add node to front of list with 4 pointers to complete circle
        else:
            new_node.next = self.sentinel.next
            #print(new_node.next.value)
            new_node.prev = self.sentinel
            #print(new_node.prev.value)
            # self.sentinel.prev = new_node
            self.sentinel.next = new_node
            #print(self.sentinel.next.value)
            # self.sentinel.prev.next = new_node
            self.sentinel.next.next.prev = new_node
            #print(self.sentinel.next.next.prev.value)

        return


    def add_back(self, value: object) -> None: #good
        """
        This method adds a new node at the end of the list (right before the back sentinel).
        """

        new_node = DLNode(value)

        if self.sentinel.next == self.sentinel:  # if the list is empty

            new_node.next = self.sentinel  # point from new node to sentinel.next
            #print(new_node.next.value)
            new_node.prev = self.sentinel  # point from new node to sentinel.prev
            #print(new_node.prev.value
            self.sentinel.next = new_node  # point from sentinel.next to new node
            self.sentinel.prev = new_node  # point from sentinel.next to new node
        else:

            new_node.next = self.sentinel  # point from new node to the sentinel
            new_node.prev = self.sentinel.prev  # point from new node to prev of las node
            self.sentinel.prev = new_node  # move from sentinel to new node
            self.sentinel.prev.prev.next = new_node  # move from prev prev of last node to what is now the last node

        return

    def insert_at_index(self, index: int, value: object) -> None: #good
        """
        Method adds a new value at the specified index position in the linked list
        """
        new_node = DLNode(value)

        if index < 0 or index > self.length():
            raise CDLLException

        if index == 0: #if the index is at zero, add it to the front
            self.add_front(value)
            return
        if index == self.length(): #if the index is in the last position, add it to the back
            self.add_back(value)
            return


        count = 0
        current = self.sentinel.next
        previous = self.sentinel

        while current != self.sentinel:
            if count == index: #if count is index, set up four links to the sentinel

                new_node.next = current  # move the new_node to the sentinel after
                new_node.prev = previous  # move the new_node to the sentinel before
                previous.next = new_node  # move from the sentinel before to the new_node
                current.prev = new_node  # move from the sentinel after to the new_node
                return
            count += 1 #increment counter if position not reached
            previous = current #previous novet to next position
            current = current.next #current moves up next next position

        return


    def remove_front(self) -> None: #good
        """
        removes the first node from the list. If the list is empty, the method raises a
        custom “SLLException”.
        """

        if self.length() == 0: #if list is empty
            raise CDLLException

        self.sentinel.next.next.prev = self.sentinel #link sentinel to front so it's none value
        #print(self.sentinel.next.next.prev.value)
        self.sentinel.next = self.sentinel.next.next #link start to the next next position, which is 2nd
        #print(self.sentinel.next.value)
        return


    def remove_back(self) -> None:
        """
        removes the lsat node from the list. If the list is empty, the method raises a
        custom “SLLException”.
        """
        if self.length() == 0: #if list is empty
            raise CDLLException

        self.sentinel.prev.prev.next = self.sentinel #link sentinel to back
        #print(self.sentinel.prev.prev.next.value)
        self.sentinel.prev = self.sentinel.prev.prev #link last to the prev prev position
        #print(self.sentinel.prev.value)

        return


    def remove_at_index(self, index: int) -> None:
        """
        Removes a node given its index position
        """

        if index < 0 or index > self.length() - 1:
            raise CDLLException

        if index == 0: #if the index is 0, remove the front
            self.remove_front()
            return
        if index == self.length(): #if the index is in the last position, remove back
            self.remove_back()
            return

        current = self.sentinel.next
        previous = self.sentinel
        count = 0

        while current != self.sentinel:
            if count == index:  # if count == current index position
                previous.next = current.next  # point prev to current.next
                previous.next.prev = previous  # point  prev of previous.next to prev
                return

            count += 1 #else increment count and increment position..same as insert_at_index
            previous = current
            current = current.next


    def get_front(self) -> object: #good
        """
        Returns value from the first node in the list without removing it.
        """
        if self.length() == 0: #if list is empty, raise exception
            raise CDLLException
        return self.sentinel.next.value #return the value after sentinel


    def get_back(self) -> object:
        """
        Gets back position without removing it
        """

        if self.length() == 0:
            raise CDLLException
        return self.sentinel.prev.value #return the value previous to sentinel


    def remove(self, value: object) -> bool: #not good
        """
        traverses the list from the beginning to the end and removes the first node in
        the list that matches the provided “value” object. Method returns True if some node was
        actually removed from the list. Otherwise it returns False.
        """

        if self.length() == 0:  # if the list is empty
            return False

        current_node = self.sentinel.next

        if current_node.value == value: #if the node is the first node
            self.remove_front()
            return True

        while current_node.next != self.sentinel and current_node.next.value != value:
            current_node = current_node.next #iterate through the list

        if (current_node.next.value == value):  # If the node to be removed was found
            #print(current_node.next.value)
            current_node.next = current_node.next.next #skip node to remove
            current_node.next.prev = current_node #previous of current becomes sentinel.next

            return True

        return False #if node was found, return false


    def count(self, value: object) -> int: #good
        """
        Counts the number of elements in the list that match the provided “value"
        """
        count = 0
        current = self.sentinel
        length1 = self.length()

        while length1 > 0: # wile the list length is > 0, traverse list
            current = current.next
            length1 -= 1 #decrement length of list
            #print("THIS IS TEMP :", length1)
            if current.value == value: #if it equal the count, add to count + 1
                count += 1
                #print("secondl:", length1)
                #print("CURRENTVAL :", current.value, end='\n')
        return count


    def slice(self, start_index: int, size: int) -> object: #maybe good
        """
        returns a new LinkedList object that contains the requested number of nodes
        from the original list starting with the node located at the requested start index
        """
        if start_index < 0 or start_index + size > self.length():
            raise CDLLException


        new_list = CircularList() #create a new sliced list to return
        current_node = self.sentinel.next

        count = 0
        while count < start_index: #loop to find the start_index poisition
            count += 1
            current_node = current_node.next
        for i in range(0, size):  #set the size of the slice range
            new_list.add_back(current_node.value)  #add_back the current_node to the new circular list
            current_node = current_node.next #find mext node to increment to size
        return new_list


    def is_sorted(self) -> int: #maybegood
        """
        This method returns an integer that describes whether the linked list is sorted. Method
        should return 1 if the list is sorted in strictly ascending order. It should return 2 if the list is
        sorted in strictly descending order. Otherwise the method should return 0.
        """

        ascendingNode = 1 #return 1 if ascending
        descendingNode = 2  #return 2 if descending

        current_nodeAsc = self.sentinel.next #check ascending sort
        while current_nodeAsc.next.next != self.sentinel: #check next to head
            if current_nodeAsc.value >= current_nodeAsc.next.value: #check to see if in ascending order. val > next.val
                ascendingNode = 0  #return 0 if not greater
            current_nodeAsc = current_nodeAsc.next #check next node


        current_nodeDes = self.sentinel.next #check descending sort
        while current_nodeDes.next.next != self.sentinel: #check next position to head
            if current_nodeDes.value <= current_nodeDes.next.value: #if descending order, current < current.next
                descendingNode = 0   #return 0 if not less than
            current_nodeDes = current_nodeDes.next #check next node

        if ascendingNode < descendingNode: #check to see which value is greater and return it
            return descendingNode
        else:
            return ascendingNode


    def swap_pairs(self, index1: int, index2: int) -> None: #maybegood
        """
                This method swaps pairs of two nodes located at different indices.
                Swapping must be done by changing node pointers. You are not allowed to just swap values
                of the two nodes.
                """
        if index1 < 0 or index1 >= self.length() or index2 < 0 or index2 >= self.length():
            raise CDLLException

        new_node = self.sentinel.next
        count = 0
        while new_node != self.sentinel:  # check index 1 to swap paire
            # print("This is NN :", new_node.value)
            if count < index1:  # if less than the index, check next node
                # print("COUNT :", count)
                # print("INDEX :", index1)
                count += 1
                new_node = new_node.next
            else:
                break

        new_node2 = self.sentinel.next  # check for index 2 same as before
        count2 = 0
        while new_node2 != self.sentinel:
            if count2 < index2:
                # print("COUNT2 :", count2)
                # print("INDEX2 :", index2)
                count2 += 1
                new_node2 = new_node2.next
            else:
                break

        if new_node.next == new_node2:  # check when nodes are next to each other
            new_node.prev.next = new_node2  # point prev of next to new_node2
            new_node2.next.prev = new_node  # point next of prev to new_node
            new_node.next = new_node2.next  # point node_new to new_node2.next
            new_node.prev = new_node2  # point prev new_node to new_node2
            new_node2.next = new_node  # point next new_node2 to new_node 1st
            new_node2.prev = new_node2.prev.prev  # point prev of new_node2 to the node before prev
            return
        if new_node2.next == new_node:  # check next nodes to swap
            new_node2.prev.next = new_node
            new_node.next.prev = new_node2  # same as before
            new_node2.next = new_node.next  # same as before
            new_node.next = new_node2  # same as before
            new_node.prev = new_node.prev.prev  # same as before
            return

        temp_next = new_node.next  # if nodes arent together, they are spaced by one.
        # print(temp.next.value)
        temp_prev = new_node.prev
        # print(temp.prev.value)

        new_node.prev.next = new_node2
        # print(new_node.prev.next.value)
        new_node.next.prev = new_node2
        # print(new_node.next.prev.value)
        new_node2.prev.next = new_node  # prev of next to the new_node
        new_node2.next.prev = new_node  # point next of prev to new_node
        new_node.next = new_node2.next  # point new_node next second new_node next
        new_node.prev = new_node2.prev  # point new node prev to new_node2 prev
        new_node2.next = temp_next  # last, point new_node2.next to new_node.next
        new_node2.prev = temp_prev  # last, point new_node2.prev to new_node.prev

        return

    def reverse(self) -> None: #good but not passing gradescope?
        """
        Reverses the order of the nodes in the list. The reversal is done “in
        place” without creating any copies of existing nodes or an entire existing list
        """
        if self.length() == 0: # or self.length() == 1: #if empty or one element, return
            return

        if self.length() == 1:
            self.add_front()
            return

        temp = None
        current_node = self.sentinel.next

        while current_node != self.sentinel:
            temp = current_node.prev    #point temp to the previous node
            current_node.prev = current_node.next #point "backwards" to what is next in front
            current_node.next = temp #current points forward to what is now temp
            current_node = current_node.prev #point current to new prev, which is really current next

        if temp is not None:
            self.sentinel.next = temp.prev #go to next position if not None


    def sort(self) -> None: # good

        """
        This method sorts the content of the list in non-descending order. It's done
        “in place” without creating any copies of existing nodes or an entire existing list.
        """

        # Check if list is empty or only has one element
        if self.length() == 0 or self.length() == 1:
            return

        #if self.length() == 1:
            #self.add_front()
            #return

        else:
            is_sorted = False

            while not is_sorted:
                is_sorted = True

                node1 = self.sentinel.next
                node2 = self.sentinel.next.next

                while node2 != self.sentinel:
                    if node1.value > node2.value:
                        is_sorted = False
                        #swap using bubble sort
                        node_before_n1 = node1.prev  # create link to node before n1 that can be used later
                                                  # bc we alter n1.prev later on
                        node1.prev.next = node2
                        node2.next.prev = node1
                        node1.next = node2.next  # point to next of n2
                        node1.prev = node2  # point to prev of n1
                        node2.next = node1
                        node2.prev = node_before_n1  # point to link before n1

                        node2 = node1.next  # n1 is already where it should be, move n2 to next position

                    else:
                        node1 = node2
                        node2 = node2.next  # to next position if not


    def length(self) -> int: #good
        """
        Find length of CDLL
        """

        new_node = self.sentinel

        count = 0
        while new_node.next != self.sentinel: #create loop: sentinel is back again for circular
            new_node = new_node.next #increment to next node for count until sentinel is reached
            count = count + 1

        return count


    def is_empty(self) -> bool: #good
        """
        Returns True is list is empty, False otherwise
        """

        if self.length() == 0:
            return True
        return False


if __name__ == '__main__':
    print('\n# add_front example 1')
    list = CircularList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = CircularList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)


    print('\n# insert_at_index example 1')
    list = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# remove_front example 1')
    list = CircularList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = CircularList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = CircularList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = CircularList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = CircularList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = CircularList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = CircularList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = CircularList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '1'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200]
    )
    for case in test_cases:
        list = CircularList(case)
        print('Result:', list.is_sorted(), list)


    print('\n# is_empty example 1')
    list = CircularList()
    print(list.is_empty(), list)
    list.add_back(100)
    print(list.is_empty(), list)
    list.remove_at_index(0)
    print(list.is_empty(), list)


    print('\n# length example 1')
    list = CircularList()
    print(list.length())
    for i in range(800):
        list.add_front(i)
    print(list.length())
    for i in range(799, 300, -1):
        list.remove_at_index(i)
    print(list.length())

    print('\n# swap_pairs example 1')
    list = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5), (4, 2), (3, 3))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            list.swap_pairs(i, j)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        list = CircularList(case)
        list.reverse()
        print(list)


    print('\n# reverse example 2')
    list = CircularList()
    print(list)
    list.reverse()
    print(list)
    list.add_back(2)
    list.add_back(3)
    list.add_front(1)
    list.reverse()
    print(list)


    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        list = CircularList(case)
        print(list)
        list.sort()
        print(list)
