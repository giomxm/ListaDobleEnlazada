class NodoDoble:
    def __init__(self,value,siguiente,previo):
        self.data = value
        self.next = siguiente
        self.prev = previo
    
class ListaDoblementeEnlazada:
    def __init__(self):
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
      return self.get_size() == 0

    def insert(self,value):
        if self.__size == 0:
            nuevo = NodoDoble(value,self.__tail,self.__head)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
        else:
            nuevo = NodoDoble(value,self.__tail,self.__tail.prev)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo
        self.__size += 1

    def transversal(self):
        curr_Node = self.__head.next
        while curr_Node.next != None:
            print(curr_Node.data,"->",end=" ")
            curr_Node = curr_Node.next
        print("")

    def reverse_transversal(self):
        curr_Node = self.__tail.prev
        while curr_Node.prev != None:
            print(curr_Node.data,"->",end=" ")
            curr_Node = curr_Node.prev
        print("")

    def find_from_head(self,value):
      curr_Node = self.__head
      encontrado = None
      while curr_Node.data != value:
        curr_Node = curr_Node.next
       
      if curr_Node.data == value:
        encontrado = curr_Node
       
      return encontrado

    def find_from_tail(self,value):
      curr_Node = self.__tail
      encontrado = None
      while curr_Node.data != value:
        curr_Node = curr_Node.prev
       
      if curr_Node.data == value:
        encontrado = curr_Node
       
      return encontrado

    def remove_from_head(self,value):
      cur_Node = self.find_from_head(value)
      cur_Node.prev.next = cur_Node.next
      cur_Node.next.prev = cur_Node.prev
      cur_Node.next = None
      cur_Node.prev = None
      
      
      

    def remove_from_tail(self, value):
      cur_Node = self.find_from_tail(value)
      cur_Node.prev.next = cur_Node.next
      cur_Node.next.prev = cur_Node.prev
      cur_Node.next = None
      cur_Node.prev = None
      
      

    def insert_between(self, value, predecesor, sucesor):
      predecesor = self.find_from_head(predecesor)
      sucesor = self.find_from_head(sucesor)

      if predecesor.next != sucesor:
         print("Los nodos no son consecutivos")
      else:
        nuevo = NodoDoble(value,sucesor,predecesor)
        predecesor.next = nuevo
        sucesor.prev = nuevo
        



def main():

    ldl = ListaDoblementeEnlazada()

    print(f"Tamaño = {ldl.get_size()}")

    ldl.insert(10)

    ldl.insert(20)

    ldl.insert(30)

    ldl.insert(40)

    ldl.insert(50)

    ldl.transversal()

    ldl.insert_between(15,10,20)

    ldl.transversal()

    ldl.remove_from_head(15)

    ldl.transversal()

main()