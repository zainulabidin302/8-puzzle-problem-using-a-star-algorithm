import queue as Q
from Node import Node


def a_star(node, goal):
    open_list = Q.PriorityQueue()
    close_list = []
    moves_counter = 0
    max_move_counter = 10000
    while True:
        if max_move_counter == moves_counter:
            print('MOVE COUNTER EXCEEDED MAX MOVE COUNTER ')
            return
        moves_counter += 1

        for neighbour in (list(set(node.neighbours) - set(close_list))):
            open_list.put(neighbour)

        node = open_list.get()

        if node == goal:
            print('Moves = ', moves_counter)
            print('Explored Nodes = ', len(open_list.queue) + len(close_list))

            return

        close_list.append(node)

a_star(Node('123457086'), Node('123456780'))
a_star(Node('163487052'), Node('123456780'))
a_star(Node('175432086'), Node('123456780'))
a_star(Node('517324806'), Node('123456780'))
a_star(Node('754320816'), Node('123456780'))
a_star(Node('178542063'), Node('123456780'))
a_star(Node('178564203'), Node('123456780'))
