class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    """Helper function to print your list"""
    current = head
    while current != None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def create_list(values):
    """Helper function to create a list from a list of values"""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


# If there is a cycle, then a 'current' that is moving faster than another will eventually lap the slower current
def findCycle(head):
    if head.next == None:
        return False
    else:
        current = head
        fast_current = head
        while fast_current.next != None and fast_current.next.next != None:
            fast_current = fast_current.next
            if fast_current == current:
                return True
            fast_current = fast_current.next
            current = current.next
        return False
    

head = create_list([1,2,3,4,5,6,7,8,9,])
head.next.next.next.next.next.next.next.next = head
print(findCycle(head))

