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
    while new_node:
      new_node=new_node.next
    new_node.next=newnode
  #display the students ex:name of the student,roll number,how many marks got student.
  def display(self):
    temp=self.head
    while temp:
      print(f"name of the student {self.name}")
      print(f"student roll number {self.roll_number}")
      print(f"student marks {self.marks}")
      temp=temp.next
      

  
            
    
