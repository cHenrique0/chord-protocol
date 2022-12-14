# for python 3.10: allow use the class name how type hint
from __future__ import annotations


class Node:
    """
    The class that represents a node in the chord ring.
    """

    def __init__(self):
        self.__key: int = 0
        self.__value: str = ""
        self.__associated_keys: dict[int, str] = {}
        self.__active_node: bool = False
        self.__next_node: Node
        self.__finger_table: list[int] = []

    def get_key(self) -> int:
        """
        Getting the key

        Returns:
            int: the node key
        """
        return self.__key

    def set_key(self, node_key: int) -> None:
        """
        Setting the key

        Args:
            node_key (int): setting the node key
        """
        self.__key = node_key

    def get_value(self) -> str:
        """
        Getting the value

        Returns:
            str: the node value
        """
        return self.__value

    def set_value(self, node_value: str) -> None:
        """
        Setting the value

        Args:
            node_value (str): the node value
        """
        self.__value = node_value

    def get_associated_keys(self) -> dict:
        """
        Getting the associated keys for the node

        Returns:
            dict: a dictionary(map) with the associated keys
        """
        return self.__associated_keys

    def set_associated_keys(self, associated_keys: dict[int, str]) -> None:
        """
        Setting the associated keys for the node

        Args:
            associated_keys (dict): a dictionary with the keys to associate with the node
        """
        self.__associated_keys.update(associated_keys)

    def is_active(self) -> bool:
        """
        Verifying if the node is active

        Returns:
            bool: return true if the node is active
        """
        return self.__active_node

    def active(self, active: bool) -> None:
        """
        Activating or deactivating the node

        Args:
            active (bool): if true, the node will be activated
        """
        self.__active_node = active

    def get_next_node(self):
        """
        Getting the next node

        Returns:
            int: the next node in the ring
        """
        return self.__next_node

    def set_next_node(self, next_node: Node) -> None:
        """
        Adding the next node

        Args:
            next_node (int): the next node
        """
        self.__next_node = next_node

    def get_finger_table(self) -> list[int]:
        """
        Getting the finger table

        Returns:
            list[int]: the finger table for the node
        """
        return self.__finger_table

    def set_finger_table(self, node_keys: list[int]) -> None:
        """
        Setting the finger table

        Args:
            finger_table (list[int]): the keys for the nodes
        """
        self.__finger_table.extend(node_keys)
