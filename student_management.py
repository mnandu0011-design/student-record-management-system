#creating the class for store marks,name and roll number using the linkedlist.
class Node:
  def __init__(self,name,roll_number,marks):
    self.name=name
    self.marks=marks
    self.roll_number=roll_number
    self.next=None
