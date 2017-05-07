from Node import Node

MAX_MOVE_COUNTER = 10000


def a_star(node, goal):
    open_list = []
    close_list = []
    moves_counter = 0

    while True :
        if MAX_MOVE_COUNTER == moves_counter:
            print('MOVE COUNTER EXCEEDED MAX MOVE COUNTER -> ')
            return
        moves_counter += 1
        open_list.extend(list(set(node.neighbours) - set(close_list)))

        # prioritize the queue based on heuristic function
        open_list.sort(key=lambda i: i.fn, reverse=True)
        node = open_list.pop()

        if node == goal:
            # node.print_path()
            print('Moves = ', moves_counter)
            print('Explored Nodes = ', len(open_list) + len(close_list))
            return

        close_list.append(node)


a_star(Node('123457086'), Node('123456780'))
a_star(Node('163487052'), Node('123456780'))
a_star(Node('175432086'), Node('123456780'))
a_star(Node('517324806'), Node('123456780'))
a_star(Node('754320816'), Node('123456780'))
a_star(Node('178542063'), Node('123456780'))
a_star(Node('178564203'), Node('123456780'))

# a_star(Node('841265307'), Node('123456780'))
# a_star(Node('783425061'), Node('123456780'))
# a_star(Node('103452786'), Node('123456780'))
# a_star(Node('623457081'), Node('123456780'))
# a_star(Node('183457026'), Node('123456780'))
# a_star(Node('675432081'), Node('123456780'))
# a_star(Node('715432086'), Node('123456780'))
# a_star(Node('874563201'), Node('123456780'))
