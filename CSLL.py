class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

class SinglyCircularLinkedList:

    def __init__(self):
        self.count = 0
        self.first = None
        self.last = None

    def InsertFirst(self, Data):
        newn = Node(Data)

        if self.first is None:
            self.first = newn
            self.last = newn
            self.last.Next = self.first
        else:
            newn.Next = self.first
            self.first = newn
            self.last.Next = self.first
        
        self.count+=1

    def InsertLast(self, Data):
        newn = Node(Data)

        if self.first is None:
            self.first = newn
            self.last = newn
            self.last.Next = self.first

        else:
            self.last.Next = newn
            newn.Next = self.first
            self.last = newn
        self.count+=1

    def InsertAtPos(self, Data, pos):
        if pos < 1 or pos > self.count+1:
            print("Invalid Position!")
            return
        
        if pos == 1:
            self.InsertFirst(Data)
            return
        
        elif pos == self.count+1:
            self.InsertLast(Data)
            return
        
        else:
            newn = Node(Data)
            temp = self.first
        
            for i in range(1,pos-1):
                temp = temp.Next
            
            newn.Next = temp.Next
            temp.Next = newn

            self.count+=1


    def DeleteFirst(self):

        if self.first is None:
            return
        
        if self.first.Next is None:
            self.first = None
            self.last = None
        
        else:
            self.first = self.first.Next
            self.last.Next = self.first
        
        self.count-=1


    def DeleteLast(self):
        if self.first is None:
            return
        
        if self.first.Next is None:
            self.first = None
            self.last = None
        
        else:
            temp = self.first
            
            while temp.Next.Next != self.first:
                temp = temp.Next
            temp.Next = self.first
            self.last = temp

        self.count-=1


    def DeleteAtPos(self, pos):
        if pos < 1 or pos > self.count:
            print("Invalid Position!")
            return
        
        if pos == 1:
            self.DeleteFirst()
        
        elif pos == self.count:
            self.DeleteLast()

        else:
            temp = self.first
            
            for i in range(pos-2):
                temp = temp.Next
            
            temp.Next = temp.Next.Next

            self.count-=1


    def Display(self):
        if self.first is None:
            return
        
        temp = self.first
        print("->",end="")
        while True:
            print("| ", temp.Data," |->",end="")
            temp = temp.Next
            if temp == self.first:
                break
        print(" Circular")
        
    def Count(self):
        print("Count of Node is : ",self.count)

class test:
    def main():
        sobj = SinglyCircularLinkedList()
        print("-----------------------------------------------------------")
        print("Operations of Insert First Node: ")

        size1 = int(input("How many insert of elements : "))
        
        for i in range(1,size1+1):
            print("Enter",i," Data : ")
            val = int(input())
            sobj.InsertFirst(val)

        print()

        sobj.Display()
        sobj.Count()
        print("-----------------------------------------------------------")
        print()

        print("Operations of Insert last Node : ")

        size2 = int(input("How many insert of elements : "))
        
        for i in range(1,size2+1):
            print("Enter", i," Data : ")
            val = int(input())
            sobj.InsertLast(val)

        sobj.Display()
        sobj.Count()
        print("-----------------------------------------------------------")
        print()

        print("Operations of Insert at position Node : ")
        posData = int(input("Enter the Data : "))
        pos = int(input("Enter the position : "))
        sobj.InsertAtPos(posData, pos)

        sobj.Display()
        sobj.Count()

        print("-----------------------------------------------------------")
        print()

        print("Operations of Delete First Node : ")
        sobj.DeleteFirst()

        sobj.Display()
        sobj.Count()
        print("-----------------------------------------------------------")
        print()

        print("Operations of Delete Last Node : ")
        sobj.DeleteLast()

        sobj.Display()
        sobj.Count()
        print("-----------------------------------------------------------")
        print()

        print("Operations of Delete at position Node : ")
        delPos = int(input("Enter the Delete position : "))
        sobj.DeleteAtPos(delPos)

        sobj.Display()
        sobj.Count()
        print("-----------------------------------------------------------")
        print()


    main()

