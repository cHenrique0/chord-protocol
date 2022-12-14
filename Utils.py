import os
from random import sample


class Utils:
    """
    Class with the utils methods like load files, generate random active nodes, etc.
    """

    def __init__(self) -> None:
        self.__active_nodes: list[int] = []
        self.__files: list[str] = []

    def load_files(self, path: str) -> list[str]:
        """
        Load files from the path

        Args:
            path (str): the path to load the files

        Returns:
            list: the list with the files
        """
        try:
            for file in os.listdir(path):
                self.__files.append(file)
        except FileNotFoundError as err:
            print(err)

        return self.__files

    def generate_active_nodes(self, active_nodes: tuple) -> list[int]:
        """
        Generate the active nodes

        Args:
            active_nodes (tuple): the tuple with the active nodes

        Returns:
            list: the list with the active nodes
        """

        self.__active_nodes.extend(active_nodes)

        # Generating the nodes in the list manually
        # self.__active_nodes.append(1)
        # self.__active_nodes.append(6)
        # self.__active_nodes.append(11)
        # self.__active_nodes.append(13)

        return self.__active_nodes

    def generate_random_active_nodes(self, qty_nodes: int, max_node: int) -> list[int]:
        """
        Generate random active nodes

        Args:
            qty_nodes (int): quantity of nodes to generate
            max_node (int): the max node in the ring

        Returns:
            list: the list of active nodes
        """

        self.__active_nodes.extend(sample(range(0, max_node), qty_nodes))

        # print(self.__active_nodes)
        return self.__active_nodes

    def get_active_nodes(self) -> list[int]:
        """
        Getting the active nodes

        Returns:
            list: the list with the active nodes
        """

        return self.__active_nodes
