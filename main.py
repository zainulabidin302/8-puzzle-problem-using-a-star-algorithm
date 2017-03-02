import random


# I will replace this at the end because it is in-efficient but
# for now let's stick with it
# so I can do the rest of assignment


def random_state():
    ls = []
    while len(ls) < 9:
        r = random.randint(0, 8)
        if r in ls:
            continue
        ls.append(r)
    return ls


# node value format is a list (1D array) -> [1,2,3,4,5,6,7,8,0]
# zero represets the blank tile





class Node:
    def __init__(self, value):
        self.__value = value
        self.__child = None

    def __str__(self):
        return ''.join(map(str, self.value))

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return (other.value) == (self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def child(self):
        if self.__child is None:
            self.__child = self.discover_child()
        return self.__child

    @child.setter
    def child(self, child):
        self.__child = child

    def discover_child(self):
        map = {
            0: [self.get_new_node(0, 1), self.get_new_node(0, 3)],
            1: [self.get_new_node(1, 0),
                self.get_new_node(1, 2),
                self.get_new_node(1, 4)],
            2: [self.get_new_node(2, 1), self.get_new_node(2, 5)],
            3: [self.get_new_node(3, 0),
                self.get_new_node(3, 4),
                self.get_new_node(3, 6)],
            4: [self.get_new_node(4, 1),
                self.get_new_node(4, 3),
                self.get_new_node(4, 5),
                self.get_new_node(4, 7)],
            5: [self.get_new_node(5, 2),
                self.get_new_node(5, 4),
                self.get_new_node(5, 8)],
            6: [self.get_new_node(6, 3), self.get_new_node(6, 7)],
            7: [self.get_new_node(7, 4),
                self.get_new_node(7, 6),
                self.get_new_node(7, 8)],
            8: [self.get_new_node(8, 7), self.get_new_node(8, 5)]
        }

        # for itm in map.get(self.value.index(0)):
        #    print (itm)
        
        return map.get(self.value.index(0))


    def get_new_node(self, x, y):
        # swap_index_x_with_y_and_return_new_node
        lis = list(self.__value)
        tmp = lis[x]
        lis[x] = lis[y]
        lis[y] = tmp
        return Node(lis)


def print_board(node):
    base = 3
    print('___________')
    for i in range(0, 3):
        for j in range(0, 3):
            print(node.value[(base * i)  + j], end=' | ')
        print('')
        print('-----------')


counter = 0
def dfs(root, visited):
    global goal_state
    global counter
    visited.append(root)
    print(counter)
    counter = counter + 1
    print_board(root)
    #print([n.value for n in visited])
    #print('\n')
    if root == goal_state:
        return root

    for child in root.child:
        if child in visited:
            #print('duplicate found -', child)
            continue
                
        path = dfs(child, visited)

        if path is not None:   # goal is found
            root.child = path
            return root
    return None


initial_state = Node(random_state())
goal_state = Node([1, 2, 3, 4, 5, 6, 7, 8, 0])
vis = []
result = dfs(initial_state, vis)

print(initial_state)

print(result)
