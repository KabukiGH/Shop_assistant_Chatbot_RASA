#!/usr/bin/env python

from multiprocessing import Process, Pipe

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

    def append_prod(self, key, value): 
        if value not in self[key]:
            num = 0
        else:
            num = self[key][value]
        self[key].update({value: num+1})


#Variables
global users
users = []
global shop_lists
shop_lists = my_dictionary()


# def fun(child_conn):
#    msg = "Hello"
#    child_conn.send(msg)
   
#    new_msg = child_conn.recv()
#    print(new_msg)
#    child_conn.close()



def shoplist(child_conn):
    name = child_conn.recv()
    product = child_conn.recv()
    if name not in users:
        users.append(name)
        shop_lists.add(users[users.index(name)], {product:1})
    else: #known user 
        shop_lists.append_prod(name, product)

    print(shop_lists)
    child_conn.send(shop_lists)
    child_conn.close()




 
   

# import multiprocessing
# # import ctypes

# def fun(l,num):    
#     l.acquire()
#     try:
#         num.value = 1
#         # print(num.value)
#     finally:
#         l.release()



   