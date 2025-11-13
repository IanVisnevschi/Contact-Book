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
    
