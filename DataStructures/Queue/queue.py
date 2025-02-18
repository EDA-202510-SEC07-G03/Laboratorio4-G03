from DataStructures.List import array_list as al

def new_queue():
    return al.new_list()

def peek(my_queue):
    first = al.first_element(my_queue)
    return first

def is_empty(my_queue):
    return  al.is_empty(my_queue)


def dequeue(my_queue):
    return al.remove_first(my_queue)

def size(my_queue):
    return al.size(my_queue)


def enqueue(my_queue,element):
    
    nueva_cola=al.add_last(my_queue,element)
    return nueva_cola