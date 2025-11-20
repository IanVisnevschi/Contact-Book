import uuid
# Class that will define the persons in the contact book.
class Contact:
    def __init__(self,contact_id,first_name,last_name,phone_number,email,address):
        self.contact_id = contact_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone_number}, {self.email}, {self.address}"
    
    #convert the data into a dictionary so it can go in a file
    def to_dict(self) -> dict:
        return{
            "contact_id": self.contact_id,
            "first name": self.first_name,
            "last name": self.last_name,
            "phone number": self.phone_number,
            "email": self.email,
            "address": self.address


        }
    # re create the data from the dictionary/file
    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            contact_id = data.get("contact_id",str(uuid.uuid4())),
            first_name = data["first name"],
            last_name = data.get("last name",""),
            phone_number = data.get("phone number",""),
            email = data.get("email",""),
            address = data.get("address","")


        )
#node class
class Node:
    def __init__(self,data = None, next_node=None):
        self.data=data
        self.next_node = next_node

    def __repr__(self):
        return f"Node({self.data!r})"
    
    def get_data(self):
        return self.data
    
    def set_data(self,value):
        self.data = value

    def get_next(self):
        return self.next_node
    
    def set_next(self,next_node):
        self.next_node = next_node


#linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.get_next(): #moves through the list
            current = current.get_next() 

        current.set_next(new_node) # new nodes goes at the end
    # puts all the data into a python list
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.get_data())
            current = current.get_next()
        return result
    #prints all the information for testing 
    def print_linkedlist(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()
    
#queue class
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
        
    def peek(self):
        if self.is_empty():
            return None 
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0 
    
    def size(self):    #returns size of queue
        return len(self.items)
    
    def __repr__(self):
        return f"Queue({self.items})"
    

class ContactManager:
    def __init__(self):
        self.contacts = LinkedList()
        self.pending_actions = Queue()

    def add_contact(self,first_name,last_name,phone,email,address):
        new_contact = Contact(
            contact_id = str(uuid.uuid4()),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone,
            email = email,
            address = address

        )

        self.contacts.insert_end(new_contact)
        return new_contact
    



class MergeSort:
    
    @staticmethod
    def merge_sort(data_list,key = lambda x: x):
       #base case, if a list has 0 or 1 items it is already sorted so program will just return the list.
        if len(data_list)<=1:
            return data_list
        
        mid = len(data_list)//2
        left_half = MergeSort.merge_sort(data_list[:mid],key)
        right_half = MergeSort.merge_sort(data_list[mid:],key)

        return MergeSort.merge(left_half,right_half,key)
    
    @staticmethod
    
    def merge(left,right,key):
        merged=[]
        i=0
        j=0

        while i <len(left) and  j < len(right):
            if key(left[i])<=key(right[j]):
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    
class BinarySearch:
    
    @staticmethod
    def search(contacts_list,key, attribute = "first_name"):
        low = 0
        high = len(contacts_list)-1
       
        while low <=high:       #loop will keep going while there is a valid list range to search
            mid = (low+high)//2
            contact = contacts_list[mid]
            
            value = getattr(contact, attribute)     #extracts the attribute value to compare

            if value == key:
                return contact
            
            if value< key:
                low = mid+1
            else:
                high = mid-1
        # item not found
        return None



       