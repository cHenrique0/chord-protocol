class Utils:
    def __init__(self) -> None:
        self.__active_nodes: list = []
        self.__files: list = []
    


    def generate_random_active_nodes(self, qty_nodes: int) -> list:
        """
        Generate random active nodes

        Args:
            qty_nodes (int): quantity of nodes to generate

        Returns:
            list: the list of active nodes
        """

        # for node in range(qty_nodes):
        #     self.__active_nodes.append(node)
        
        # Generating the nodes in the list manually
        self.__active_nodes.append(1)
        self.__active_nodes.append(6)
        self.__active_nodes.append(11)
        self.__active_nodes.append(13)

        return self.__active_nodes


    def get_active_nodes(self) -> list:
        """
        Getting the active nodes

        Returns:
            list: the list with the active nodes
        """

        return self.__active_nodes




