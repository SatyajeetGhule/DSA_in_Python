class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None
        self.Prev = None

class CircularDoubllyLinkedList:
    def __init__(self):
        self.count = 0
        self.first = None
        self.last = None

    def InsertFirst(self, Data):
        newn = Node(Data)

        if self.first is None:
            self.first = newn
            self.last = newn
            self.first.Next = self.first
            self.first.Prev = self.first
        
        else:
            newn.Next = self.first
            newn.Prev = self.last

            self.first.Prev = newn
            self.last.Next = newn

            self.first = newn
        
        self.count += 1

    def InsertLast(self, Data):
        newn = Node(Data)

        if self.first is None:
            self.first = newn
            self.last = newn
            self.last.Next = self.first
            self.first.Prev = self.last
        
        else:
            self.last.Next = newn
            newn.Prev = self.last
            self.last = newn
            self.last.Next = self.first
            self.first.Prev = self.last
        
        self.count +=1

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
            newn.Prev = temp

            temp.Next.Prev = newn
            temp.Next = newn

            self.count+=1


    def DeleteFirst(self):
        if self.first is None:
            print("Node is Empty!")
            return
    
        elif self.first.Next == self.first:
            self.first = None
            self.last = None
        
        else:
            temp = self.first
            
            self.first = self.first.Next
            self.first.Prev = self.last

            self.last.Next = self.first

            temp = None

        self.count-=1

    def DeleteLast(self):
        if self.first is None:
            print("Node is Empty!")
            return
    
        elif self.first.Next == self.first:
            self.first = None
            self.last = None
        
        else:
            temp = self.last

            self.last = self.last.Prev
            self.last.Next = self.first
            self.first.Prev = self.last

            temp = None
            
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

            for i in range(1, pos):
                temp = temp.Next

            temp.Prev.Next = temp.Next
            temp.Next.Prev = temp.Prev

            temp = None

            self.count-=1
        

    
    def Display(self):
        if self.first is None:
            print("Node is Empty")
            return

        temp = self.first
        print("Circular |<->|",end=" ")

        while True:
            print(temp.Data,"|<->|",end=" ")
            temp = temp.Next
            if temp == self.first:
                break
        print("Circular")


    def DisplayAtPos(self,pos):
        if self.first is None:
            print("Node is Empty")
            return
        
        temp = self.first
        for i in range(1,pos):
            temp = temp.Next

        print(temp.Data)


    def Count(self):
        print("Count of Node is : ",self.count)



class test:
    def main():
        obj = CircularDoubllyLinkedList()

        print("Operation for Insert First Data : ")
        size1 = int(input("How many Insert first the Elements : "))
        
        for i in range(size1):
            print("Insert",obj.count+1,"Data : ")
            val = int(input())
            obj.InsertFirst(val)

        obj.Display()
        obj.Count()
        print("---------------------------------------------------------------")

        print("Operatiopn for Insert Last Data : ")
        size2 = int(input("How many Insert the Last Elements : "))
        
        for i in range(size2):
            print("Insert",obj.count+1,"Data : ")
            val = int(input())
            obj.InsertLast(val)
        
        obj.Display()
        obj.Count()

        print("---------------------------------------------------------------")

        # n = obj.count+1
        # print("Operation of Insert At Position : ")
        # insData = int(input("Insert the Data : "))
        # insPos = int(input(f"Enter a position number less than or equal to {n} : "))
        # obj.InsertAtPos(insData, insPos)

        # obj.Display()
        # obj.Count()

        # print("---------------------------------------------------------------")

        # print("Operation for Delete First Element : ")
        
        # obj.DeleteFirst()

        # obj.Display()
        # obj.Count()
        
        # print("---------------------------------------------------------------")

        # print("Operation for Delete Last Element : ")
        
        # obj.DeleteLast()

        # obj.Display()
        # obj.Count()

        # print("---------------------------------------------------------------")

        # print("Operation for Delete at position Element : ")
        # n1 = obj.count
        # delPos = int(input(f"Enter a position number less than or equal to {n1} : "))
        # obj.DeleteAtPos(delPos)

        # obj.Display()
        # obj.Count()
        pos = int(input("Enter the Position"))
        obj.DisplayAtPos(pos)

    main()
