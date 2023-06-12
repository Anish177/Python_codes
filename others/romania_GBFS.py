#use a file to import to graph and values

graph = {
        'arad': ['sibiu', 'zerind', 'timisoara'],
        'bucharest': ['fagaras', 'pitesti', 'giurgiu', 'urziceni'],
        'craiova': ['pitesti', 'rimnicu', 'dobreta'],
        'dobreta': ['mehadia', 'craiova'],
        'eforie': ['hirsova'],
        'fagaras': ['sibiu', 'bucharest'],
        'giurgiu': ['bucharest'],
        'hirsova': ['eforie', 'urziceni'],
        'iasi': ['neamt', 'vaslui'],
        'lugoj': ['timisoara', 'mehadia'],
        'mehadia': ['lugoj', 'dobreta'],
        'neamt': ['iasi'],
        'oradea': ['zerind', 'sibiu'],
        'pitesti': ['rimnicu', 'craiova', 'bucharest'],
        'rimnicu': ['sibiu', 'pitesti', 'craiova'],
        'sibiu': ['oradea', 'fagaras', 'rimnicu'],
        'timisoara': ['arad', 'lugoj'],
        'urziceni': ['hirsova', 'vaslui', 'bucharest'],
        'vaslui': ['urziceni', 'iasi'],
        'zerind': ['arad', 'oradea']
}
        
values = {
        'arad': 366,
        'bucharest': 0,
        'craiova': 160,
        'dobreta': 242,
        'eforie': 161,
        'fagaras': 178,
        'giurgiu': 77,
        'hirsova': 151,
        'iasi': 226,
        'lugoj': 244,
        'mehadia': 241,
        'neamt': 234,
        'oradea': 380,
        'pitesti': 98,
        'rimnicu': 193,
        'sibiu': 253,
        'timisoara': 329,
        'urziceni': 80,
        'vaslui': 199,
        'zerind': 374
}

def bfs(graph, values, start, end):
    queue = []
    queue.append([start])
    visited = ()
    while queue:
        
        path = queue.pop(0)
        
        node = path[-1]
        
        if node == end:
            return path
        
        paths={}

        for adjacent in graph.get(node, []):
            try:
                if (adjacent in list(visited)[0]): continue
                else: paths[adjacent] = values[adjacent]

                if len(paths) == 0: raise Exception

            except: 
                paths[adjacent] = values[adjacent]


            adjacent0 = min(paths, key = paths.get)  # type: ignore

 
        else:
            new_path = list(path)
            new_path.append(adjacent0)
            queue.append(new_path)
            #print('The path is: ', end = '')
            print(queue)
            visited = tuple(queue)
            del paths        
   
start = 'arad'
end = 'bucharest'

print('Using greedy BFS, the path is:')
bfs(graph, values, start, end)