import copy
import pandas as pd

keys = ['room_name', 'socket_quantity','item_name', 'uses_socket', 'broken', 'consumables_keys', 'consumables_values']

class item:
    name : str
    uses_socket : bool = False
    broken : bool = False
    consumables : dict[str, int]
    
    def __init__(self, name : str, consumables : dict, broken : bool = False, uses_socket : bool = False) -> None:
        self.name = name
        self.consumables = consumables
        self.uses_socket = uses_socket
        self.broken = broken
    
    def new(self, consumables : dict = {}, broken : bool = False):
        nw = copy.deepcopy(self)
        nw.consumables = consumables
        nw.broken = broken
        return nw 

printer = item('Printer', {}, True, False)

class room:
    name : str
    socket_quantity : int
    facility_list : list = []
    facility_names : list[str] = []
    resources : dict = {}
    def __init__(self, name : str, socket_quantity : int) -> None:
        self.name = name
        #self.resources = resources
        self.socket_quantity = socket_quantity
    
    def pin(self, obj) -> None:
        tip = type(obj)
        if tip == item:
            self.facility_list.append(obj)
            if obj.name not in self.facility_names:
                self.facility_names.append(obj.name)
        elif tip == resource:
            if obj.name not in self.resources.keys():
                self.resources.update({obj.name : obj.quantity})
   
   def copy(self, cl):
       return cl.
'''    def display_all(self) -> str:
        message = ''
        for i in self.facility_names:
            for j in self.facility_list:
                if j.name == i:
                    message += i
                    message += ' '
                    for h in j.consumables.keys():
                        message += h
                        message += ' : '
                        message += str(j.consumables[h])
                        message += ' '

        return message
'''
class resource:
    name : str
    target : item
    quantity : int

    def __init__(self, name : str, target : item, quantity : int) -> None:
        self.name = name
        self.target = target
        self.quantity = quantity

def import_memory(keys: list[str]) -> list[room]:
    memory: list[room] = []
    tmp = []
    file = pd.read_csv(__file__.replace('kaka.py', 'items.csv'))
    for i in range(len(file[keys[0]])):
        for j in keys:
            tmp.append(file[j][i])
        
        print(memory)
        print(tmp)
        kes = []
        values = []
        dct = {}
        for h in list(str(tmp[5]).split()):
            kes.append(h)
        for h in list(str(tmp[6]).split()):
            values.append(int(h))
        for h in range(len(values)):
            dct.update({kes[h] : values[h]})    
        obj = room(tmp[0], tmp[1]) 
        
        

        obj.pin(item(tmp[2], dct, tmp[4], tmp[3]))
        
        if tmp[0] != '-':
            memory.append(copy.deepcopy(obj))
            del(obj)
        tmp = []
    return memory

def export_memory(memory):
   ... 
    

all_facilities: list[room]
all_facilities = import_memory(keys)

#print(all_facilities[0].facility_list, all_facilities[1].facility_list)
for i in all_facilities:
    print(i.name, i.socket_quantity, i.facility_list[1].consumables)
