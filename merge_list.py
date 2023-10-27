# Merge two sorted linked lists and return it as a new sorted list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1, l2):
    # Create a dummy node as the head of the merged list.
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # If one of the lists has remaining elements, append them to the merged list.
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    return dummy.next

# Helper function to print a linked list.
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create two sorted linked lists.
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge the sorted linked lists.
merged_list = merge_sorted_lists(list1, list2)

# Print the merged list.
print_linked_list(merged_list)
