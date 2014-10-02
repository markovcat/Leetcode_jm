# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        
        start = UndirectedGraphNode(node.label)
        map = {node: start}
        currentNodes = [node]
        while currentNodes:
            nextNodes = []
            for currentNode in currentNodes:
                for currentNeighbor in currentNode.neighbors:
                    # if the neighbor does not have a copy already
                    if currentNeighbor not in map:
                        # make a node copy
                        newNode = UndirectedGraphNode(currentNeighbor.label)
                        # establish the hash
                        map[currentNeighbor] = newNode
                        # copy the link
                        map[currentNode].neighbors.append(newNode)
                        '''This is the key debugging step
                        if the neighbor already has a copy'''
                    else:
                        # copy the link
                        map[currentNode].neighbors.append(map[currentNeighbor])
                    # add the neighbor node to the next set
                    nextNodes.append(currentNeighbor)
            currentNodes = nextNodes
        return start

print(Solution().cloneGraph({}))