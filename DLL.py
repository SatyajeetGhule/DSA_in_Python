class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None
        self.Prev = None

class DoublyLinearLinkedList:
    def __init__(self):
        self.count = 0
        self.first = None

    def InsertFirst(self, Data):
        newn = Node(Data)

        if self.first is None:
            self.first = newn

        else:
            newn.Next = self.first
            self.first.Prev = newn
            self.first = newn
        self.count+=1

    def InsertLast(self, Data):
        newn = Node(Data)

        if self.first is None:
            self.first = newn

        else:
            temp = self.first

            while temp.Next != None:
                temp = temp.Next

            temp.Next = newn
            newn.Prev = temp
            newn.Next = None
        
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

            for i in range(pos-2):
                temp = temp.Next

            newn.Next = temp.Next
            temp.Next = newn
            temp.Next.Prev = newn
            newn.Prev = temp

            self.count+=1

    def DeleteFirst(self):
        if self.first is None:
            print("Empty Node!")
            return
        
        temp = self.first

        if self.first.Next is None:
            self.first = None

        else:
            
            self.first = temp.Next
            self.first.Prev = None

            temp = None

        self.count-=1
        
    def DeleteLast(self):
        if self.first is None:
            print("Empty Node!")
            return
        
        temp = self.first

        if self.first.Next is None:
            self.first = None

        else:
            temp = self.first

            while temp.Next.Next != None:
                temp = temp.Next
            
            temp.Next = None
        
        self.count-=1

    
    def DeleteAtPos(self, pos):
        if pos < 1 or pos > self.count:
            print("Invalid Position!") 
            return
        
        if pos == 1:
            self.DeleteFirst()
            return
        
        elif pos == self.count:
            self.DeleteLast()
            return
        
        else:
            temp = self.first

            for i in range(1, pos-1):
                temp = temp.Next
            
            temp.Next = temp.Next.Next
            temp.Next.Prev = temp

            self.count-=1

    
    def Desplay(self):
        if self.first is None:
            print("Node is Empty!")
            return
        
        temp = self.first

        print("None -> ")
        while temp:
            print("|",temp.Data,"| -> ",end="")
            temp = temp.Next
        print("None")

    def Count(self):
        print("Count of Node is : ",self.count)

class test:
    def main():
        dobj = DoublyLinearLinkedList()

        print("Operation of Insert First Node : ")
        size1 = int(input("How many insert of element : "))

        for i in range(1, size1+1):
            print("Insert ",i," Data : ")
            val = int(input())
            dobj.InsertFirst(val)

        dobj.Desplay()
        dobj.Count()
        print("-----------------------------------------------------------")

        print("Operation of Insert Last Node : ")
        size2 = int(input("How many insert of element : "))

        for i in range(1, size2+1):
            print("Insert ",i," Data : ")
            val = int(input())
            dobj.InsertLast(val)

        dobj.Desplay()
        dobj.Count()
        print("-----------------------------------------------------------")

        print("Operation of Insert at position Node : ")
        insData = int(input("Enter the Data : "))
        insPos = int(input("Enter the position : "))
        dobj.InsertAtPos(insData,insPos)

        dobj.Desplay()
        dobj.Count()
        print("-----------------------------------------------------------")

        print("Operation of Delete First Node : ")
        dobj.DeleteFirst()

        dobj.Desplay()
        dobj.Count()
        print("-----------------------------------------------------------")

        print("Operation of Delete Last Node : ")
        dobj.DeleteLast()

        dobj.Desplay()
        dobj.Count()
        print("-----------------------------------------------------------")

        print("Operation of Delete at position Node : ")
        DelPos = int(input("Enter the position : "))
        dobj.DeleteAtPos(DelPos)

        dobj.Desplay()
        dobj.Count()
        
    
    main()