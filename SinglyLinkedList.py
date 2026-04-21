class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.first = None
        self.count = 0

    def Insert_First(self,data):
        newn = Node(data)

        newn.next = self.first
        self.first = newn
        self.count +=1

    def Insert_Last(self, data):
        newn = Node(data)

        if self.first is None:              # if node is empty
            self.first = newn

        elif self.first.next == None:       # if atleast one node
            self.first.next = newn
        
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
            temp.next = newn
        self.count +=1

    def InsertAtPos(self, data, pos):
        if pos < 1 or pos > self.count+1:
            print("Invalid Position!")
            return
        
        if pos == 1:
            self.Insert_First(data)
            return
        
        elif pos == self.count+1:
            self.Insert_Last(data)
            return
        else:
            newn = Node(data)
            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next
            
            newn.next = temp.next
            temp.next = newn
            self.count+=1

    def Delete_First(self):
        if self.first is None:
            print("Node is Empty!")
            return
        
        self.first = self.first.next
        self.count -=1

    def Delete_Last(self):
        if self.first is None:
            print("Node is Empty!")
            return
        
        if self.first.next == None:
            self.first = None

        else:
            temp = self.first
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
        self.count -=1

    def DeleteAtPos(self,pos):
        if pos < 1 or pos > self.count:
            print("Invalid Position!")
            return

        if pos == 1:
            self.Delete_First()
            return
        
        elif pos == self.count:
            self.Delete_Last()
            return
        
        else:
            temp = self.first
            for i in range(1, pos-1):
                temp = temp.next
            target = temp.next
            temp.next = target.next
            self.count -=1

    def Display(self):
        temp= self.first

        while temp:
            print(" | ",temp.data,"->",end="")
            temp = temp.next
        print("None")

    def Count(self):
        print("Total Count Node : ",self.count)

class test:
    def main():
        obj = SinglyLL()
        obj.Insert_First(input("Enter the Data : "))
        obj.Insert_First(input("Enter the Data : "))
        obj.Insert_First(input("Enter the Data : "))

        obj.Display()
        obj.Count()


        obj.Insert_Last(input("Enter the Data : "))
        obj.Insert_Last(input("Enter the Data : "))
        obj.Insert_Last(input("Enter the Data : "))

        obj.Display()
        obj.Count()

        val = int(input("Enter the Data : "))
        pos = int(input("Enter the position : "))
        obj.InsertAtPos(val, pos)

        obj.Display()
        obj.Count()

        obj.Delete_First()

        obj.Display()
        obj.Count()

        obj.Delete_Last()

        obj.Display()
        obj.Count()

        deletPos = int(input("Enter the position : "))
        obj.DeleteAtPos(deletPos)

        obj.Display()
        obj.Count()

    main()
