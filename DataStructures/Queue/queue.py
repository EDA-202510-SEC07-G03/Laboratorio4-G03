from DataStructures.List import array_list as al
def peek(my_queue):
    first = al.first_element(my_queue)
    return first
def is_empty(my_queue):
    x = al.is_empty(my_queue)
    return x


def dequeue(my_queue):
    my_queue["elements"].pop(0)
    return dequeue

def size(dequeue):
    return dequeue["size"]


def new_queue():
    return al.new_list

def enqueue(my_queue,element):
    
    nueva_cola=al.add_last(my_queue,element)
    return nueva_cola