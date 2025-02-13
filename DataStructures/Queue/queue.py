import DataStructures.List.array_list as ar

def new_queue():
    return ar.new_list

def enqueue(my_queue,element):
    
    nueva_cola=ar.add_last(my_queue,element)
    return nueva_cola