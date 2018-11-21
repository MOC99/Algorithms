import csv

stack = []
route = []
num_adj = []
adj = []
adj_head = None


class Node:                                     # Node类
    def __init__(self, data, pnext):            # node定义
        self.data = data
        # self.bool = BoolData
        self._next = pnext

    def NodeAppend(self, data1):                # node方法
        num_pre = self
        num_next = data1
        if not adj[num_pre]:                    # 链表插入
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


def DFS(x, y):                                   # x = Start ,y = End
    if x == y:
        i = 0
        lenght = len(route)
        for i in range(0, lenght):
            print("{}".format(route[i]),end="")
            if i != lenght-1:
                print("-",end="")
        exit()
    num_adj[x][1] = 1
    node = adj[x][0]
    num = node.data
    if num_adj[num][1] != 1:                    # 判断节点是否被标记
        num_adj[num][1] = 1                     # 标记节点
        stack.append(num)
        route.append(num)
        DFS(num, y)
    else:
        node = node._next
        num_tmp = node.data
        if num_adj[num_tmp][1] != 1:
            num_adj[num_tmp][1] = 1
            stack.append(num_tmp)
            route.append(num_tmp)
            DFS(num_tmp, y)
        else:
            node = node._next
            if node == None:
                stack.pop()
                adj_tmp = stack.pop()
                route.pop()
                DFS(adj_tmp, y)
            else:
                num_tmp = node.data
                stack.append(num_tmp)
                route.append(num_tmp)
                DFS(num_tmp, y)


# def check_marked():                   # 标记检查,用不上
#     adj_lenght = len(num_adj)
#     i = 0
#     for i in range(0, adj_lenght):
#         if num_adj[i][1] != 1:
#             return False
#         i = +1
#     return True

with open("d://dfs.csv", "r", encoding="utf-8", newline="") as f:
    i = 1
    b = csv.reader(f)
    for row in b:
        if i <= 2:
            if i == 1:
                Vector_tmp = list(map(int, row))
                Vector = Vector_tmp[0]
                j = 0
                for j in range(0, Vector):
                    adj.append([])
                    num_adj.append([j, 0])
            else:
                Edge_tmp = list(map(int, row))
                Edge = Edge_tmp[0]
            i += 1
        else:
            VD = list(map(int, row))            # 性质转换 VD[0] VD[1]
            Node.NodeAppend(VD[0], VD[1])
    StartVector = int(input("start:"))          # 输入开始节点
    EndVector = int(input("end:"))              # 输入结束节点
    route.append(StartVector)
    print("{} to {}:".format(StartVector,EndVector),end="")
    DFS(StartVector, EndVector)