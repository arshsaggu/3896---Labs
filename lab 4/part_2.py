class DLLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None
        self.prev = None


    def __repr__(self):
        return f"LLN({str(self.contents)})"


    def insertAfter(self, contents):
        new_node = DLLN(contents)
        new_node.prev = self
        new_node.next = self.next
        if new_node.next is not None:
            new_node.next.prev = new_node
        self.next = new_node
        return new_node


    def insertBefore(self, contents):
        new_node = DLLN(contents)
        new_node.prev = self.prev
        new_node.next = self
        if new_node.prev is not None:
            new_node.prev.next = new_node
        self.prev = new_node
        return new_node
        

    def toList(self):
        linkedlistlist = []
        current = self
        while current is not None:
            linkedlistlist.append(current.contents)
            current = current.next
        return linkedlistlist


    def findLast(self):
        current = self
        while current.next is not None:
            current = current.next
        return current
    

    def findFirst(self):
        current = self
        while current.prev is not None:
            current = current.prev
        return current
    

    def findAfter(self, needle):
        current = self
        current = self.next
        while current is not None:
            if current.contents == needle:
                return current
            current = current.next
        raise KeyError(needle)
                

    def findBefore(self, needle):
        current = self
        current = self.prev
        while current is not None:
            if current.contents == needle:
                return current
            current = current.prev
        raise KeyError(needle)


def main():
    one = DLLN("one")
    two = one.insertAfter('two')
    print("should be one two:", one.toList())

    five = one.findLast().insertAfter('five')
    print("should be one two five:", one.toList())

    three = two.insertAfter('three')
    print("should be one two three five:", one.toList())

    zero = one.insertBefore('zero')
    print("should be zero one two three five:", one.findFirst().toList())

    four = one.findAfter('five').insertBefore('four')
    print("should be zero one two three four five:", one.findFirst().toList())

    the_two = one.findFirst().findAfter('two')
    print("should successfully find two:", the_two)

    the_two = one.findLast().findBefore('two')
    print("should successfully find two:", the_two)


    print("should fail to find two:")
    try:
        print(two.findBefore('two'), "this should not print")
    except KeyError as ke:
        print("KEY ERROR", ke)


if __name__ == "__main__":
    main()