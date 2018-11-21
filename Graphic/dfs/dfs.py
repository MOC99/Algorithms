import csv

stack = []
num_adj = []
adj = []
adj_head = None


class Node:  # node定义
    def __init__(self, data, pnext):
        self.data = data
        # self.bool = BoolData
        self._next = pnext

    def NodeAppend(self, data1):  # node方法
        num_pre = self
        num_next = data1
        if not adj[num_pre]:  # 链表插入
            node = Node(num_next, None)
            adj[num_pre].append(node)
        else:
            node1 = adj[num_pre][0]
            node2 = Node(num_next, node1)
            adj[num_pre][0] = node2

        if not adj[num_next]:
            node = Node(num_pre, None)
            adj[num_next].append(node)
        else:
            node1 = adj[num_next][0]
            node2 = Node(num_pre, node1)
            adj[num_next][0] = node2


def DFS(x):  # 默认传进值 0
    a_tmp = check_marked()
    if a_tmp == True:
        exit()
    # print(a_tmp)
    num_adj[x][1] = 1
    # print(num_adj)
    node = adj[x][0]
    num = node.data
    # print(num)
    if num_adj[num][1] != 1:
        num_adj[num][1] = 1  # 标记节点
        stack.append(num)
        DFS(num)
    else:
        node = node._next
        # print(node.data)
        num_tmp = node.data
        if num_adj[num_tmp][1] != 1:
            num_adj[num_tmp][1] = 1
            stack.append(num_tmp)
            DFS(num_tmp)
        else:
            num_tmp = node.data
            node = node._next
            if node == None:
                adj_tmp = stack.pop()
                DFS(adj_tmp)
            else:
                num_tmp = node.data
                stack.append(num_tmp)
                DFS(num_tmp)


def check_marked():  # 标记检查
    adj_lenght = len(num_adj)
    i = 0
    for i in range(0, adj_lenght):
        if num_adj[i][1] != 1:
            return False
        i = +1
    return True


with open("d://dfs.csv", "r", encoding="utf-8", newline="") as f:
    i = 1
    b = csv.reader(f)
    for row in b:
        if i <= 2:
            if i == 1:
                Vector_tmp = list(map(int, row))
                Vector = Vector_tmp[0]
                # print(type(Vector))
                j = 0
                for j in range(0, Vector):
                    adj.append([])
                    num_adj.append([j, 0])
                print(adj)
            else:
                Edge_tmp = list(map(int, row))
                Edge = Edge_tmp[0]
            i += 1
        else:
            VD = list(map(int, row))  # 性质转换 VD[0] VD[1]
            Node.NodeAppend(VD[0], VD[1])
    DFS(0)
