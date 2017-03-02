import random
import queue as Q
import sys


# I will replace this at the end because it is in-efficient but
# for now let's stick with it
# so I can do the rest of assignment


def pop(lis):
    a = None
    if len(lis) > 0:
        a = lis[-1]
    del list[-1]

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
    def __init__(self, value, moves=0, parent=None):
        self.__value = value
        self.__child = None
        self.__moves = moves
        self.__parent = parent

    def __str__(self):
        return ''.join(map(str, self.value))

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return (other.value) == (self.value)

    def __lt__(self, other):
        full_cost_a = self.moves  + self.hamming_distance()    # f(x) = g(x) + h(x)
        full_cost_b = other.moves + other.hamming_distance()   # f(x) = g(x) + h(x)
        
        # full_cost_a = self.moves  + self.manhatan_distance()    # f(x) = g(x) + h(x)
        # full_cost_b = other.moves + other.manhatan_distance()   # f(x) = g(x) + h(x)
        
        # print('a cost = ', full_cost_a, 'b cost = ', full_cost_b)

        return (full_cost_a < full_cost_b)

    def build_path(node, path):
        path.append(node)
        if node.parent == None:
            return path
        return Node.build_path(node.parent, path)

    def hamming_distance(self):
        index = 0
        distance = 0
        for n in self.value:

            if index + 1 != n:
                distance += 1
            index = index + 1
        return distance

    def manhatan_distance(self):
        distance = 0

        def get_actual_cordinates(n):
            y = x = None
            if n in [1, 4, 7]:
                x = 0
            if n in [2, 5, 8]:
                x = 1
            if n in [3, 6]:
                x = 2

            if n in [1, 2, 3]:
                y = 0
            if n in [4, 5, 6]:
                y = 1
            if n in [7, 8]:
                y = 2

            if n == 0:
                x = y = 0

            return x, y

        row = col = 0
        for n in self.value:
            if n == 0:
                continue
            x1, y1 = get_actual_cordinates(n)
            x2 = col
            y2 = row

            if col == 2:
                row = row + 1
                col = -1
            col = col + 1
            x = x2 - x1
            y = y2 - y1
            distance = distance + abs(x) + abs(y)
        return distance





    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def moves(self):
        return self.__moves

    @moves.setter
    def moves(self, value):
        self.__moves = value

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

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
        # print('prev self moves = ', self.moves)
        mov = self.moves + 1 # increment the move cost
        tmp = lis[x]
        lis[x] = lis[y]
        lis[y] = tmp
        return Node(lis, mov, self)


def print_board(node):
    base = 3
    print('___________')
    for i in range(0, 3):
        for j in range(0, 3):
            print(node.value[(base * i)  + j], end=' | ')
        print('')
        print('-----------')


def astar(initial_state, goal_state, visited):
    state_counter = 0
    move_counter = 0

    pQ = Q.PriorityQueue()

    pQ.put(initial_state)
    parent = None

    while 1:
        parent = pQ.get()

        if parent == goal_state:
            break

        if parent in visited:
            continue


        visited.append(parent)

        # print_board(parent)
        for ch in parent.child:

            if ch in visited:
                continue
            pQ.put(ch)
            state_counter = state_counter + 1

        move_counter = move_counter + 1

    print('total states traversed = ', state_counter)
    print('total moves traversed = ', move_counter)





if __name__ == '__main__':
    goal_state = Node([1, 2, 3, 4, 5, 6, 7, 8, 0], -1)
    if len(sys.argv) > 1:
        initial_state = sys.argv[1]
        initial_state = Node(list(map(int, initial_state.split(','))), 0)
    else:
        print ('No intial state was provided, building a random initial state instead.')
        initial_state = Node(random_state(), 0)
    print('Starting Board: ')
    print_board(initial_state)
    closed_list = []
    print('working ....')

    astar(initial_state, goal_state, closed_list)

    path = []
    Node.build_path(closed_list[-1], path)
    #print('closed list', [n.value for n in closed_list])

    for n in reversed(path):
        print_board(n)

    print('total moves of solution', len(path))
