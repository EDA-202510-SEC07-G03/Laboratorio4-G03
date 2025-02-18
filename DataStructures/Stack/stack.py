from DataStructures.List import single_linked_list as sl
from DataStructures.List import list_node as ln
def new_stack():
    return sl.new_list()

def push(my_stack,element):
    """
    Añade un elemento al final de la estructura de datos
    """
    new_node=ln.new_single_node(element)
    my_stack["last"]=new_node
    
    if my_stack["size"]==0:
        my_stack["first"]=new_node
    
    my_stack["size"]+=1
    
    return my_stack

def size(my_stack):
    return my_stack["size"]

def pop(my_stack):
    removed_info=0
    if is_empty(my_stack)==True:
         raise Exception('IndexError: list index out of range')
    else:
         if my_stack["size"]==1:
             removed_info=sl.remove_first(my_stack)
         else:
             current=my_stack["first"]
             removed_info=my_stack["last"]
             while current != my_stack["last"]:
                 current=current["next"]
                 if current["next"]==my_stack["last"]:
                    current["next"]=None
                    my_stack["last"]=current
                    my_stack["size"]-=1
    return removed_info

def is_empty(my_stack):
    return sl.is_empty(my_stack)

def top(my_stack):
    return my_stack["last"]["info"]

def size(my_stack):
    print(my_stack["size"])
    return my_stack["size"]