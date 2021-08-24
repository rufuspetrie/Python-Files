import sys,time
sys.setrecursionlimit(2 ** 20)
n=875714

def openGraph():
    f = open('SCC.txt')
    lines = f.readlines()
    graph, graph_r = {}, {}
    for i in range(1,n+1):
        graph[i],graph_r[i]=[],[]
    for line in lines:
        ints = [int(x) for x in line.split()]
        graph[ints[0]].append(ints[1])
        graph_r[ints[1]].append(ints[0])
    f.close()
    return graph, graph_r
	
def DFS_loop(graph):
    # t tracks finishing times, s tracks leader nodes
    global t, s, explored
    t=0
    s=0
    explored={}
    for i in range(1,n+1):
        explored[i]=0
    for i in range(n,0,-1):
        if explored[i]==0:
            s=i
            DFS(graph,i)
    return # blank b/c of global variables
	
def DFS(graph,i):
    global t
    explored[i]=1
    leaders[i]=s
    for j in graph[i]:
        if explored[j]==0:
            DFS(graph,j)
    t+=1
    times[i]=t
    return # blank b/c of global variables
	
def Kosaraju(graph,graph_r):
    
    # Step one: run dfs loop on graph_r to compute finishing times
    global leaders, times
    leaders={}
    times={}
    DFS_loop(graph_r)
    
    # Step two: swap node names with finishing times and perform DFS
    graph_values=graph.values()
    graph_swapped={}
    for i in range(1,n+1):
        value=graph_values[i-1]
        graph_swapped[times[i]]=[times[x] for x in value]
    DFS_loop(graph_swapped)
    return leaders


def most_common(lst,x):
    # This functions returns the 'x' most common elements from 'lst' 
    from collections import Counter
    c = Counter(lst)
    result = []
    for number,count in c.most_common(x):
        result.append(count)
    return result

if __name__=="__main__":
    start = time.time()
    G, G_rev = openGraph()
    print "Graph grabbed in", time.time() - start,"seconds"

    start = time.time()
    leader = Kosaraju(G,G_rev)
    print "Kosaraju's Algorithm ran in", time.time() - start,"seconds"

    print "Size of the top 5 strongly connected components:"
    print most_common(leader.values(),5)
	
'''
graph, graph_r = openGraph()
x=Kosaraju(graph,graph_r)
'''