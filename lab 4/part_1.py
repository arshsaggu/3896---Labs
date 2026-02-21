class LLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None


    def __repr__(self):
        return f"LLN({str(self.contents)})"


    def insertAfter(self, new_content):
        new_node = LLN(new_content)
        if self.next is not None:
            new_node.next = self.next
        self.next = new_node
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


    def findAfter(self, needle):
        current = self.next
        while current is not None:
            if current.contents == needle:
                return current
            current = current.next
        raise KeyError(needle)
                

def main():
    print("\n** testing init and repr **")
    first = LLN("alice")
    print("first should have a repr() (or a str()) so that it can be printed:", first)

    print("\n** insertAfter **")
    second = first.insertAfter("bob")
    print("we did first.insertAfter(bob), so now second s hould exist too, and contain bob:", second)

    print("\n** more insertAfter **")
    third = second.insertAfter("carol")
    print("we did second.insertAfter(carol), so now third should exist too, and contain carol:", third)

    print("\n** toList **")
    print("I'd like to be able to print them out in a normal Python list")
    print("Everything (as a list) starting from second (should be 2 things):", second.toList())
    print("Everything (as a list) starting from first (should be 3 things):", first.toList())
    print("Let me prove that it returns a list.  What's the type?  It's:", type(first.toList()))

    print("\n** more checking of longer LinkedLists **")
    fourth = third.insertAfter("dave")
    print("we just added 'dave' after the third node")
    print("the whole linked list (as a list):", first.toList())
    print("starting at third:", third.toList())
    print("starting at fourth:", fourth.toList())

    print("\n** findLast **")
    print("this should get dave (who is last): ", first.findLast())
    print("this should also get dave (who is last): ", fourth.findLast())

    print("\n** inserting works in the middle **")
    two_point_cat = second.insertAfter("cat")
    print("I added a cat after bob, it should appear before carol:", first.toList())

    two_point_dog = second.insertAfter("dog")
    print("I added a dog after bob, it should appear before the cat:", first.toList())

    print("\n** findAfter **")
    print("I can find bob after alice:", first.findAfter("bob"))
    print("But if I try to find alice after bob, I get an exception")
    try:
        print(second.findAfter("alice"))
    except KeyError as ke:
        print("KEY ERROR", ke)
    print("Similarly I cannot find cat AFTER cat, I get an exception")
    try:
        print(two_point_cat.findAfter("cat"))
    except KeyError as ke:
        print("KEY ERROR", ke)
    print("But the dave is after the cat, that's fine:", two_point_cat.findAfter("dave"))


if __name__ == "__main__":
    main()