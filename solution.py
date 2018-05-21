def parse_graph(stream):
    lineList = [str(x.rstrip()) for x in stream.readlines()];
    nodes = int(lineList[0]);
    links = [[int(a), int(b)] for [a,b] in [x.split(',') for x in lineList[1:]]];

    # Parsing graph as adjacency list
    adjList = [[] for i in range(nodes)];
    for link in links:
        adjList[link[0]].append(link[1]);

    return(nodes, adjList);

def bfs(graph, start):
    queue, explored = [start], set();
    while(queue):
        node = queue.pop(0);
        for n in graph[node]:
            if n not in explored:
                explored.add(n);
                queue.append(n);
    return explored;

def dfs_paths(graph, start):
    # Base case
    if(len(graph[start]) == 0):
        return [[start]];

    # Recursion case
    allPaths = [];
    for node in graph[start]:
        paths = dfs_paths(graph, node);
        for path in paths:
            allPaths.append([start] + path);
    return allPaths

def get_root_nodes(nodes, graph):
    rootNodes = set(range(nodes));

    explored = set();
    # Running BFS for all nodes in graph
    for n in range(nodes):
        start = n
        if start not in explored:
            explored = explored | bfs(graph, start);
            rootNodes = rootNodes - explored;
    return rootNodes;

def get_paths(roots, graph):
    pathLists = [];
    for root in roots:
        pathLists.append(dfs_paths(graph, root));

    paths = []
    for pathList in pathLists:
        for path in pathList:
            paths.append(path);
    return paths;

def process_output(nodes, paths):
    formattedRootNodesString = ",".join([str(x) for x in nodes]);

    formattedOutputPathsString = "";
    for path in paths:
        formattedOutputPathsString += "->".join([str(x) for x in path]) + "\n";

    print_output(formattedRootNodesString, formattedOutputPathsString);
    write_output(formattedRootNodesString, formattedOutputPathsString);

def print_output(rootsString, pathsString):
    print('Root Nodes:');
    print(rootsString);
    print('Output Paths:');
    print(pathsString);

def write_output(rootsString, pathsString):
    outputStream = open('data/output.txt', 'w')
    outputStream.write('Root Nodes: \n');
    outputStream.write(rootsString + '\n');
    outputStream.write('Output Paths: \n');
    outputStream.write(pathsString);

if __name__ == "__main__":
    inputStream = open('data/input.txt');
    [nodes, graph] = parse_graph(inputStream);

    roots = get_root_nodes(nodes, graph);
    paths = get_paths(roots, graph);

    process_output(roots, paths);
