import uuid
import tkinter as tk
from tkinter import messagebox
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
    
    def get_all_contacts(self):
        return self.contacts.to_list()
    
    def search_contact(self,key,attribute = "first_name"):
        contact_list = self.contacts.to_list()

        #sorting the list using merge sort before applying binary search 

        sorted_list = MergeSort.merge_sort(
            contact_list,
            key = lambda c: getattr(c, attribute)
        )

        return BinarySearch.search(
            sorted_list,
            key,
            attribute = attribute
        )
    
    def remove_contact(self, contact_id):
        current = self.contacts.head
        prev = None

        while current:
            if current.get_data().contact_id == contact_id:
                if prev: # will remove from the middle
                    prev.set_next(current.get_next())
                else: # will remove the head
                    self.contacts.head = current.get_next()
                return True
            
            prev = current
            current = current.get_next()
        return False
    
    def update_contact(self, contact_id, **kwargs):
        current = self.contacts.head

        while current:
            contact = current.get_data()
            if contact.contact_id == contact_id:
                for key, value in kwargs.items():
                    if hasattr(contact,key):
                        setattr(contact,key,value)
                return contact
            current = current.get_next()
        return None
    





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
    

class ContactApp:
    def __init__(self,root,manager):
        self.root = root
        self.root.title("Contact Book")
        self.manager = manager

        #inputs for adding contacts
        tk.Label(root, text = "First Name").grid(row=0,column=0)
        tk.Label(root, text = "Last Name").grid(row=1, column=0)
        tk.Label(root, text = "Phone").grid(row=2, column=0)
        tk.Label(root, text  = "Email").grid(row = 3, column = 0)
        tk.Label(root, text = "Address").grid(row = 4,column = 0)


        self.entry_first = tk.Entry(root)
        self.entry_last = tk.Entry(root)
        self.entry_phone = tk.Entry(root)
        self.entry_email = tk.Entry(root)
        self.entry_address = tk.Entry(root)

        self.entry_first.grid(row = 0, column = 1)
        self.entry_last.grid(row = 1, column = 1)
        self.entry_phone.grid(row = 2, column = 1)
        self.entry_email.grid(row = 3, column = 1)
        self.entry_address.grid(row = 4, column = 1)

        tk.Button(root, text = "Add Contact", command = self.add_contact).grid(row=5,column=0,pady=5)
        tk.Button(root, text = "show all contacts", command = self.show_contacts).grid(row=5,column=1)
        tk.Button(root, text = "Search Contact", command = self.search_contact).grid(row=6, column =0)
        tk.Button(root, text = "Delete Contact", command = self.delete_contact).grid(row = 6, column = 1)

        self.output = tk.Text(root, height =15, width=50)
        self.output.grid(row=7,column = 0, columnspan = 2, pady = 10)



    def add_contact(self):
        first = self.entry_first.get()
        last = self.entry_last.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if not first:
            messagebox.showerror("Error", "first name is required")
            return
        
        new_contact = self.manager.add_contact(first, last, phone, email, address)
        messagebox.showinfo("Success", "Contact Added")
        self.clear_entries()

    def show_contacts(self):
        self.output.delete("1.0",tk.END)
        contacts = self.manager.contacts.to_list()

        if not contacts:
            self.output.insert(tk.END, "no contacts found.\n")
            return
        
        for c in contacts:
            self.output.insert(tk.END, f"{c}\n")

    def search_contact(self):
        name = self.entry_first.get()
        if not name:
            messagebox.showerror("Error, enter first name to search")
            return
        
        contacts_list = self.manager.contacts.to_list()
        sorted_contacts = MergeSort.merge_sort(contacts_list,key=lambda c: c.first_name)
        result = BinarySearch.search(sorted_contacts, name, "first_name")

        self.output.delete("1.0",tk.END)
        if result:
            self.output.insert(tk.END,f"FOUND: {result}\n")
        else:
            self.output.insert(tk.END,f"CONTACT NOT FOUND.\n")

    
    def delete_contact(self):
        name = self.entry_first.get()
        if not name:
            messagebox.showerror("Error", "Enter FirstName to delete")
            return
        current = self.manager.contacts.head
        prev = None
        

        while current:
            if current.data.first_name == name:
                if prev:
                    prev.next_node = current.next_node
                else:
                    self.manager.contacts.head = current.next_node
                    messagebox.showinfo("Deleted",f"Deleted{name}")
                    return
            prev = current
            current = current.next_node

    
    def clear_entries(self):
        self.entry_first.delete(0, tk.END)
        self.entry_last.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    manager = ContactManager()
    app = ContactApp(root, manager)
    root.mainloop()


        





        
    

    



       