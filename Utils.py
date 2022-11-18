class Utils:
    def __init__(self) -> None:
        self.__activeNodes = []
    
    def generateRandomActiveNodes(self, nodes: int) -> list:
        # for node in range(nodes):
        #     self.__activeNodes.append(node)
        self.__activeNodes.append(1)
        self.__activeNodes.append(6)
        self.__activeNodes.append(11)
        self.__activeNodes.append(13)

        return self.__activeNodes
    
    def getNodes(self) -> list:
        return self.__activeNodes




