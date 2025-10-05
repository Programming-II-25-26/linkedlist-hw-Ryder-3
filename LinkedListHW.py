#Starter Ccode below including helper functions 
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

def reverse_list(head):
    if head.next == None:
        return head
    else:
        current = head
        log_1 = head
        log_2 = head

        while current.next != None:
            current = current.next
            if log_1 == log_2:
                log_1.next = None
                log_1 = current
            else:
                log_1.next = log_2
                log_2 = log_1
                log_1 = current
        log_1.next = log_2
        head = current
        return head

values = [0]
head = create_list(values)
print_list(head)
head = reverse_list(head)
print_list(head)
