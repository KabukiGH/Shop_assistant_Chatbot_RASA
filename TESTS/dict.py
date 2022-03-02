class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict()
          
    # Function to add key:value 
    def add(self, key, value): 
        # self[key] = value 
        if key not in self:
            self[key] = {value:0}
        if value not in self[key]:
            num = 0
        else:
            num = self[key][value]
        self[key].update({value: num+1})

    def pop_product(self, key, value):
        self[key].pop(value)

    def show(self, key='all'):
        if key == 'all':
            for key in self:
                print(f'{key}: ')
                for iter in self[key]:
                    print('\t',iter, self[key][iter])
        else:
            if key in self:
                print(f'{key}: ')
                for iter in self[key]:
                    print('\t',iter, self[key][iter])

#Variables
global users
users = []
global shop_lists
shop_lists = my_dictionary()


for iter in range(5):
    name = input('Name: ')
    product = input(' Product: ')
    shop_lists.add(name, product)
    print(shop_lists)

shop_lists.show()
