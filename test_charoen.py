import math
#genlocation
def genWarehouse(row,column,height,width):  
    Warehouse = []
    array_area = [(1,1),(2,2),(2,3),(3,3),(4,4)] 
    for i in range(1,row+1):
        # area1 = input('area1 :')
        # area2= input('area2 : ')
        for j in range(1,column+1):
            for k in range(1,height+1):
                for l in range(1,width+1):
                    if k == 1:
                        location1= location(i,j,k,l,True,False,array_area[i-1])
                    else:
                        location1= location(i,j,k,l,True,True,array_area[i-1])
                    Warehouse.append(location1)
    return Warehouse
    # for i in range(len(Warehouse)):
    #     print(Warehouse[i].name)
        
class location:
    def __init__(self,row,column,height,width,is_empty,avaliable,area):
        self.row = row
        self.col = column
        self.height = height
        self.width = width
        self.is_empty = is_empty
        self.avaliable = avaliable
        self.area1 = area[0]
        self.area2 = area[1]
        self.name = str(row)+ "|" +str(column)+ "|" +str(height)+ "|" +str(width)
        
    # Warehouse[array_score.index(min(array_score))].is_empty = False
    
def cal_height(location_height, is_light):
    
    if(is_light):
        if(location_height <= 3) :
            return (6 - location_height + 20)
        else : 
            return (6 - location_height)
    
    elif(location_height > 3):
        return 9000000000
    else:
        return (location_height - 1) 
    # print(array_score)
        
            
        # score = 0
        # if location.is_empty :
        #     score = 1

def genlocation(rootnode, weight):
    array_score = []
    for location in Warehouse:
        dist_area1 = 1000 * abs(location.area1 - rootnode.area1)
        dist_area2 = 1000 * abs(location.area2 - rootnode.area2)
        # dist_row = 1000*abs(location.row -rootnode.row)
        dist_col = 100*abs(location.col - rootnode.col)
        dist_height = cal_height(location.height, weight)
        dist_width = abs(location.width - rootnode.width) 
        # score = dist_row + dist_col + dist_height + dist_width + dist_area1 + dist_area2
        score =  dist_col  + min(dist_area1, dist_area2) + math.sqrt(pow(dist_height,2) + pow(dist_width,2))
        if(score == 0) :
            score = 10000000000
        if (location.is_empty and location.avaliable):
            array_score.append(score)
        else:
            array_score.append(score*100000)
    
    # print(array_score)
    # print(min(array_score))
    print(str(min(array_score)))
    
 #   print(Warehouse[array_score.index(min(array_score))].name +"     " + str(min(array_score)))
    
    Warehouse[array_score.index(min(array_score))].is_empty = False
    return Warehouse[array_score.index(min(array_score))]
    
        
W_row = 5
W_col = 3
W_height = 5
W_width = 16
Warehouse= genWarehouse(W_row,W_col,W_height,W_width)


root_location = location(2,3,1,5,False,True,(2,2))



product_is_light = True
for i in range(100):
    print(i)
    x = genlocation(root_location, product_is_light)
    print(x.name)