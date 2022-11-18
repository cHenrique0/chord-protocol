from Node import Node
from Utils import Utils

class Chord:
    def __init__(self, activeNodes: int) -> None:
        self.__ring = []
        self.__amountActiveNodes = activeNodes
    
    def getRing(self) -> list:
        return self.__ring
    
    def setRing(self, ring: list) -> None:
        self.__ring = ring
    
    def getAmountActiveNodes(self) -> int:
        return self.__amountActiveNodes
    
    def setAmountActiveNodes(self, amount: int) -> None:
        self.__amountActiveNodes = amount
    
    def ringLength(self) -> int:
        return len(self.__ring)
    
    def addNode(self, node: Node) -> None:
        self.__ring.append(node)
        # self.getRing().append(node)
    
    def setAssociatedNodes(self) -> None:
        node = Node()
        associated_nodes = {}
        first_node = -1
        end = 0

        for node_index in range(len(self.__ring) - 1, -1, -1):
            
            node = self.__ring[node_index]
            
            if(node.getActiveNode()):
                node.setAssociatedKeys(associated_nodes)

                if(first_node == -1):
                    first_node = node_index

            if(first_node >= 0):
                print(associated_nodes)
                associated_nodes.update({node.getKey(), node.getValue()})
                print(associated_nodes)
            
            if(node_index == 0):
                node_index = len(self.__ring)
                end = first_node+1
            

    
    def setNext(self):
        previous_node = -1
        first_node = -1
        node = Node()
        
        for node_index in range(len(self.__ring)):
            node = self.__ring[node_index]
            if node.getActiveNode():
                if previous_node >= 0:
                    self.__ring[previous_node].setNextNode(node.getKey())
                else:
                    first_node = node.getKey()

                previous_node = node_index

        self.__ring[previous_node].setNextNode(first_node)

    
    def activateInitialNodes(self) -> None:
        random_active_nodes = Utils().generateRandomActiveNodes(self.__amountActiveNodes)
        node = Node()
        index = 0
        for node_index in range(len(random_active_nodes)):
            index = random_active_nodes[node_index]
            node = self.__ring[index]
            node.setActiveNode(True)

    def start(self) -> None:
        self.activateInitialNodes()
        self.setNext()
        self.setAssociatedNodes()

    def printRing(self) -> None:
        for node in self.__ring:
            if(node.getActiveNode()):
                print(f"Key: {node.getKey()}")
                print(f"Value: {node.getValue()}")
                print(f"Active: {node.getActiveNode()}")
                print(f"Next: {node.getNextNode()}")
                print(f"Associated Keys: {node.getAssociatedKeys()}")
                print("=====================================")
        
        print(f"Active Nodes: {self.getAmountActiveNodes()}")
        print("=====================================")


