import csv

stack = []
queue = []
route = []
num_adj = []
adj = []
adj_head = None
edgeto = []         # 到达该顶点的已知路径上最后一个顶点

class Node:
    def __init__(self,data,pnext):
        self.data = data
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

def BFS(x):         # 默认传入值 0
    node = adj[x][0]
    if num_adj[x][1] != 1:
        num_adj[x][1] = 1
    while node != None:         # 将元素加入队列
        data = node.data
        if num_adj[data][1] != 1:
            queue.append(data)
            edgeto.append([data])
            num_adj[data][1] = 1
        node = node._next
        # print(queue)
        # print(edgeto)
    if len(queue) == 0:
        # print(num_adj)
        edgeto.sort()
        SartNum = edgeto[0][0]
        BFSPutOut(SartNum)
        exit()
    tmp = queue[0]
    queue.remove(queue[0])
    lenght = len(edgeto)
    lenght1 = len(queue)
    for j in range(0,lenght1):          # 将已知路径中最后的一个节点加入
        data_tmp = queue[j]
        for i in range(0,lenght):
            if len(edgeto[i]) == 1:
                if edgeto[i][0] == data_tmp:
                    edgeto[i].append(x)
    BFS(tmp)

def BFSPutOut(x):                       # x--num 输出函数
    lenght = len(edgeto)
    for i in range(1,lenght):
        data1 = edgeto[i][0]
        data2 = edgeto[i][1]
        print("{} to {}: ".format(x, data1),end="")
        if data2 == x:
            print("{}-{}".format(data2,data1))
        else:
            j = 1
            print("{}".format(x),end="")
            while edgeto[j][1] == x & j < lenght:
                if data2 == edgeto[j][0]:
                    print("-{}".format(edgeto[j][0]),end="")
                j = j + 1
            print("-{}".format(edgeto[i][0]))

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
            VD = list(map(int, row))  # 性质转换 VD[0] VD[1]
            Node.NodeAppend(VD[0], VD[1])
    edgeto.append([0])
    queue.append(0)
    BFS(0)
