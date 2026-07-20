#creating the class Node.
class Node:
#add data that name,rollnumber,marks.
  def __init__(self,name,roll_number,marks):
    self.name=name
    self.marks=marks
    self.roll_number=roll_number
    self.next=None
#creating the class studentslinkedlist.
class studentslinkedlist:
  #creating the head inside the function.
  def __init__(self):
    self.head=None
    #add new student in record.
  def add_students(self,name,roll_number,marks):
    newnode=Node(name,roll_number,marks)
    if self.head is None:
      self.head=newnode
      return
    new_node=self.head
    for I in new_node:
            
    
