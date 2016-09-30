def dijkstra(graph,sourceNode,destinationNode,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in sourceNode
    """    
    # a few sanity checks
    if sourceNode not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if destinationNode not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')    
    # ending condition
    if sourceNode == destinationNode:
        # We build the shortest path and display it
        path=[]
        pred=destinationNode
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[destinationNode])) 
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[sourceNode]=0
        # visit the neighbors
        for neighbor in graph[sourceNode] :
            if neighbor not in visited:
                new_distance = distances[sourceNode] + graph[sourceNode][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = sourceNode
        # mark as visited
        visited.append(sourceNode)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with sourceNode='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,destinationNode,visited,distances,predecessors)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()


    '''
    graph = {'s': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
    dijkstra(graph,'s','t')
    '''

    graph = {'OC':{'TCR':900,'PC':1200,'BS':700,'GP':1500},
             'BS':{'GP':1400,'OC':700},
             'TCR':{'OC':900,'LS':800},
             'LS':{'TCR':800,'PC':600,'CC':700},
             'PC':{'LS':600,'OC':1200,'CC':1100},
             'CC':{'E':300,'PC':1100,'LS':700},
             'GP':{'BS':1400,'PC':800,'OC':1500,'BS':1400,'V':1900,'W':2100},
             'W':{'V':2200,'E':1000,'GP':2100},
             'E':{'W':1000,'CC':300,'T':900},
             'T':{'E':900}}
    # works - why?
    dijkstra(graph,'OC','W')
    # fails - why?
    #dijkstra(graph,'LS','V')
