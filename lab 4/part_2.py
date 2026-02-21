class DLLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None
        self.prev = None


    def __repr__(self):
        pass


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
        

    def toList(self):
        pass

    def findLast(self):
        pass

    def findFirst(self):
        pass

    def findAfter(self, needle):
        pass

    def findBefore(self, needle):
        pass


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