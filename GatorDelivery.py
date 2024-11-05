class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = None
        self.height = 1

class Order:
    def __init__(self, order_id, current_system_time, order_value, delivery_time):
        self.order_id = order_id
        self.current_system_time = current_system_time
        self.order_value = order_value
        self.delivery_time = delivery_time
        valueweight = 0.3
        timeweight = 0.7
        normalizedorervalue= order_value/50
        self.priority=valueweight*normalizedorervalue-timeweight*current_system_time
        self.eta = 0        




class AVLTree:
    def insert(self, node, key, value):
        if not node:
            return Node(key, value)
        if key < node.key:
            node.left = self.insert(node.left, key, value)
        else:
            node.right = self.insert(node.right, key, value)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1:
            if key < node.left.key:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        if balance < -1:
            if key > node.right.key:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        return node

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left, z.right = z, T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right, y.left = y, T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0
    
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


def in_order(node, list):
    if node:
        in_order(node.left, list)
        list.append(node.val)
        in_order(node.right, list)

# Usage
# tree = AVLTree()
# root = None
# for key in [10, 20, 30, 40, 50, 25]:
#     root = tree.insert(root, key, key * 1000)

class GatorDelivery:
    def __init__(self):
        self.priority_tree_root = None
        self.priority_tree = AVLTree()
        self.eta_tree_root = None
        self.eta_tree = AVLTree()
        self.delivering_order = None

    def createOrder( self, order_id, current_system_time, order_value, delivery_time):
        order = Order( order_id, current_system_time, order_value, delivery_time)#all oder in loop function read file
        self.priority_tree_root = self.priority_tree.insert(self.priority_tree_root, order.priority, order)
        
        list = []
        in_order(self.priority_tree_root, list)

       

        #print("LEN: ", len(list))
        if len(list) == 1:
            order.eta = order.current_system_time + order.delivery_time
            self.delivering_order = order
        else:
            
            delivering_order_index = 0
            # for i in range(len(list)):
            #     ord = list[i]
            #     if ord.order_id == self.delivering_order.order_id:
            #         delivering_order_index = i
            #         break
            
            listb = []
            for i in range(len(list)):
                if list[i].order_id == self.delivering_order.order_id:
                    delivering_order_index = i
                else :
                    listb.append(list[i]) 
            listb.append(list[delivering_order_index])
            next_index =0

            for i in range(len(listb)):
                if order.order_id == listb[i].order_id:
                    next_index = i+1
            
            order.eta = listb[next_index].delivery_time + order.delivery_time + listb[next_index].eta
           
            
            for i in range(next_index,0,-1):
               listb[i-1].eta = listb[i].delivery_time + listb[i].eta + listb[i-1].delivery_time     

        self.eta_tree_root = self.eta_tree.insert(self.eta_tree_root,order.eta,order)

        list = []
        in_order(self.eta_tree_root, list)
        print("ETA Inorder:")
        for ord in list:
            print(ord.eta, end=' ')
        print()

        delivered = None
        for ord in list:
            if ord.eta < current_system_time:
                delivered = i

                self.priority_tree_root = self.priority_tree.delete(self.priority_tree_root, ord.priority)
                self.eta_tree_root = self.eta_tree.delete(self.eta_tree_root, ord.eta)

        if delivered != None:
            self.delivering_order = list[len(list) - 1]

    def cancelOrder(self, order_id, current_system_time):

        plist = []
        elist = []

        in_order(self.priority_tree_root, plist)
        in_order(self.eta_tree_root, elist)
        
        order = None
        del_index = -1
        i = 0
        for ord in plist:
            if ord.order_id == order_id:
                if self.delivering_order.order_id == ord.order_id or ord.eta < current_system_time:
                    print('Cannot cancel. Order delivered')
                else:
                    order = ord
            if ord.order_id == self.delivering_order.order_id:
                del_index = i
            i += 1
        
        if order == None:
            return
        
        # 1 2 3 4 D 5 6
        ord_before_i = -1
        ord_after_i = -1
        if del_index == i + 1:
            if i + 2 < len(plist):
                ord_after_i = i + 2
            else:
                ord_after_i = del_index
            ord_before_i = i - 1
        elif del_index == i - 1:
            if i - 2 > -1:
                ord_before_i = i - 2
            else:
                ord_before_i = -1
            ord_after_i = i + 1
        
        ord_before = plist[ord_before_i]
        ord_after = plist[ord_after_i]

        # delete
        self.priority_tree_root = self.priority_tree.delete(self.priority_tree_root, ord.priority)
        self.eta_tree_root = self.eta_tree.delete(self.eta_tree_root, ord.eta)

        # update others
        if ord_before_i > -1:

            ord_before.eta = ord_after.eta + ord_after.delivery_time + ord_before.delivery_time
            
            # aage vaale order ke eta
            for i in range(ord_before_i - 1, 0, -1):    
                prev_order = list[i - 1]

                # delivering order needs to be ignored
                if i - 1 == del_index and i - 2 > -1:
                    prev_order = list[i - 2]
                
                if i - 2 > -1:
                    prev_order.eta = order_after.eta + order_after.delivery_time + prev_order.delivery_time
                    order_after = prev_order
        
        # delivering
        elist = []
        in_order(self.eta_tree_root, elist)
        delivered = -1
        for ord in list:
            if ord.eta < current_system_time:
                delivered = i

                self.priority_tree_root = self.priority_tree.delete(self.priority_tree_root, ord.priority)
                self.eta_tree_root = self.eta_tree.delete(self.eta_tree_root, ord.eta)

        if delivered > -1:
            self.delivering_order = list[len(list) - 1]

            
    def updateTime(self,order_id, current_system_time, newDeliveryTime):
        list = []
        in_order(self.priority_tree_root, list)
        
        delivering_order_index = None
        
        listb = [None] * (len(list)-1)
        
        for i in range(len(list)):
                if list[i].order_id == self.delivering_order.order_id:
                    delivering_order_index = i
                    i+=1
                else :
                    listb[i] = list[i] 
        listb.append(list[delivering_order_index])
        
        new_index = None
        
        for i in range(0, len(list)):
            ord = listb[i]
            if ord.order_id == order_id:
                new_index = i
                break
        listb[new_index].eta = newDeliveryTime + listb[new_index+1].eta + listb[new_index+1].delivery_time
        
        for i in range(new_index,0,-1):
               listb[i-1].eta = listb[i].delivery_time + listb[i].eta + listb[i-1].delivery_time 

    def getRankOfOrder(self,orderId):
        list = []
        in_order(self.priority_tree_root, list)
        
        delivering_order_index = None
        
        listb = [None] * (len(list)-1)
        
        for i in range(len(list)):
                if list[i].order_id == self.delivering_order.order_id:
                    delivering_order_index = i
                    i+=1
                else :
                    listb[i] = list[i] 
        listb.append(list[delivering_order_index])
        
        number_of_order = None

        for i in range (len(listb)):
            if listb[i].orderId == orderId:
                number_of_order = (len(listb)-1) - i
                break
            #print   Order {orderId} will be delivered after {numberOfOrders} orders

        

    def print(self,orderId):
        list = []
        in_order(self.eta_tree_root, list)
        for ord in list:
            if ord.order_id ==orderId:
                print(ord.order_id , ord.current_system_time,ord.order_value,ord.delivery_time,ord.eta)
                break
    
    def print(self,time1, time2):
        list = []
        in_order(self.priority_tree_root, list)
        
        delivering_order_index = None
        
        listb = [None] * (len(list)-1)
        
        for i in range(len(list)):
                if list[i].order_id == self.delivering_order.order_id:
                    delivering_order_index = i
                    i+=1
                else :
                    listb[i] = list[i] 
        listb.append(list[delivering_order_index])
        start_time = None
        end_time = None
        for i in range (len(listb)-1):
            if listb[i].eta >= time1:
                start_time = i
                break
        for i in range (len(listb)-1):
            if listb[i].eta >=  time2:
                end_time = i-1
                break
        #print all the orders ffrom start time to end time

    
    


        


gator_delivery = GatorDelivery()

gator_delivery.createOrder(1001, 1, 200, 3)
gator_delivery.createOrder(1002, 3, 250, 6)
gator_delivery.createOrder(1003, 8, 100, 3)
gator_delivery.createOrder(1004, 13, 100, 5)

# command =  input ("Enter a command")
# if command == "print":
#     printorder(command[1])



