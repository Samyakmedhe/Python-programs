

class Node:

    def __init__(self,No):
        self.data = No
        self.next = None 
    
class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0
    
    def Display(self):

        temp = self.first
        print()
        while(temp !=  None):
            print(f"| {temp.data} | -> ",end = "")
            temp = temp.next
        
        print("None")
###################################################################################
    def InsertFirst(self, No):
        newn = Node(No)
     
        if(self.first == None):
            self.first = newn 
        else:
            newn.next = self.first
            self.first = newn
        
        self.iCount+=1   

################################################################################### 

    def InsertLast(self, No):
        newn = Node(No)
     
        if(self.first == None):
            self.first = newn 
        else:
            temp = self.first 
            while(temp.next != None):
                temp = temp .next
                
            temp.next = newn
            
        
        self.iCount+=1   
##################################################################################
    def DeleteFirst(self):

        if(self.first == None):
            return 
        
        else:
            temp = self.first

            self.first = self.first.next

        del temp

        self.iCount-= 1 
##################################################################################
    def DeleteLast(self):

        if(self.first == None):
            return 
        
        elif self.first.next == None:
            del self.first 
        else:
            temp = self.first 
            while(temp.next.next != None):
                temp = temp.next
               
            del temp.next
            temp.next = None

        self.iCount-= 1 
##################################################################################
    


###################################################################################
    def Count(self):
        return self.iCount


###################################################################################
def main():
    print("----- Demonstraction of Singly linear linked list -----")
    
    sobj = SinglyLL()
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of Nodes om linked list are  : {iRet}")

    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)

    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of Nodes om linked list are  : {iRet}")

    sobj.DeleteFirst()
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of Nodes om linked list are  : {iRet}")

    sobj.DeleteLast()
    sobj.Display()
    iRet = sobj.Count()
    print(f"Number of Nodes om linked list are  : {iRet}")




if __name__=="__main__":
    main()