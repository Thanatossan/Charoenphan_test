import math
import random
import string
from functools import total_ordering

alphabets = string.ascii_lowercase
W_row = 2
W_col = 3
W_height = 5
W_width = 5

class Warehouse:
    def __init__(self) -> None:
        self.all = []
        self.same_row = []
        self.same_col = []
        self.same_height = []


class Location:
    def __init__(self, row, column, height, width, is_empty, avaliable, area):
        self.row = row
        self.col = column
        self.height = height
        self.width = width
        self.is_empty = is_empty
        self.avaliable = avaliable
        self.area1 = area[0]
        self.area2 = area[1]
        self.name = f"{alphabets[row-1]}{alphabets[column-1]}{alphabets[height-1]}{width}"
        self.stored = [" "]
    
    def __repr__(self) -> str:
        return self.name
    
    def add_product(self, product):
        self.stored = [product]

class Product:
    def __init__(self, name, weight, root_location):
        self.name = name
        self.weight = weight
        self.root_location = root_location
    
    def __repr__(self) -> str:
        return self.name


product_stored_at = {}


def gen_all_product(products_info, lower_location):
    return [
        Product(info["name"], info["weight"], lower_location[index])
        for index, info in enumerate(products_info)
    ]


def gen_warehouse(row, column, height, width):
    warehouse = []
    lower_locations = []
    array_area = [(1, 1), (2, 2), (2, 3), (3, 3), (4, 4)]
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            for k in range(1, height + 1):
                for l in range(1, width + 1):
                    if k == 1:
                        location1 = Location(i, j, k, l, True, False, array_area[i - 1])
                        lower_locations.append(location1)
                    else:
                        location1 = Location(i, j, k, l, True, True, array_area[i - 1])
                    warehouse.append(location1)
    return (warehouse, lower_locations)    
    
def print_warehouse(warehouse):
    location_str = []
    info = ""
    for location in warehouse:
        info += f"{location.name}:{location.stored if not location.is_empty else '[   ]'}  "
        if location.width == W_width:
            location_str.insert(0, info)
            info = ""
            if location.height == W_height:
                for loc in location_str:
                    print(loc)
                location_str.clear()
                print("-----------------------"*4)
                
                if location.col == W_col:
                    print("------- END ----------"*4)
        
        

def cal_height(location_height, is_light):
    if is_light:
        if location_height <= 3:
            return (W_height+1) - location_height + 20
        else:
            return (W_height+1) - location_height

    elif location_height > 3:
        return math.inf
    else:
        return location_height - 1



def store_in_location(warehouse, product):
    array_cost = []
    for location in warehouse:
        dist_area1 = 1000 * abs(location.area1 - product.root_location.area1)
        dist_area2 = 1000 * abs(location.area2 - product.root_location.area2)

        dist_col = 100 * abs(location.col - product.root_location.col)
        dist_height = cal_height(location.height, product.weight)
        dist_width = abs(location.width - product.root_location.width)


        cost = (
            dist_col
            + min(dist_area1, dist_area2)
            + math.sqrt(pow(dist_height, 2) + pow(dist_width, 2))
        )

        if cost == 0:
            cost = 10000000000
        if location.is_empty and location.avaliable:
            array_cost.append(cost)
        else:
            array_cost.append(cost * 100000)


    min_cost = min(array_cost)
    warehouse_index = array_cost.index(min_cost)
    stored_location = warehouse[warehouse_index]
    stored_location.is_empty = False
    stored_location.add_product(product)

    print("Stored At", stored_location)


warehouse, lower_location = gen_warehouse(W_row, W_col, W_height, W_width)

products = gen_all_product(
    [
        {"name": "เลย์", "weight": True},
        {"name": "น้ำ1", "weight": True},
        {"name": "ปูน1", "weight": False},
        {"name": "ฝรั่ง", "weight": True},
        {"name": "น้ำ2", "weight": True},
        {"name": "ปูน2", "weight": False},
    ],
    lower_location
)

for i in range(len(products)):
    lower_location[i].stored = [products[i]]
    lower_location[i].is_empty = False


while True:
    try:
        print_warehouse(warehouse)
        print("Products:", tuple(enumerate(products)))
        product_index = input("รับ: ").strip()
        indexs = [int(x) for x in product_index.split(" ")]
        print(indexs)
        print("เอาเข้า warehouse")
        for product_index in indexs:
            store_in_location(warehouse, products[product_index])
    except Exception as e:
        print("Error", e)
    