from Node import Node
from time import sleep


class Chord:

    def __init__(self, active_nodes: list[int]) -> None:
        self.__ring: list[Node] = []
        self.__amount_active_nodes: int = len(active_nodes)
        self.__active_nodes: list[int] = active_nodes

    def get_ring(self) -> list:
        return self.__ring

    def set_ring(self, ring: list) -> None:
        self.__ring = ring

    def print_node(self, key: int) -> None:
        node = self.__ring[key]
        print(f"Key: {node.get_key()}")
        print(f"Value: {node.get_value()}")
        print(f"Active: {node.is_active()}")
        if node.is_active():
            print(f"Next: {node.get_next_node().get_key()}")
            print(f"Associated Keys: {node.get_associated_keys()}")
        else:
            print("Next: {}")
            print("Associated Keys: {}")

    def get_amount_active_nodes(self) -> int:
        return self.__amount_active_nodes

    def set_amount_active_nodes(self, amount: int) -> None:
        self.__amount_active_nodes = amount

    def length(self) -> int:
        return len(self.__ring)

    def add_node(self, node: Node) -> None:
        self.__ring.append(node)

    def get_next_node_key(self, key: int) -> int:
        return self.__ring[key].get_key()

    def find(self, value: str) -> tuple[Node, list[Node]] | None:

        searched_nodes: list[Node] = []

        for _, node in enumerate(self.__ring):
            if node.is_active():
                searched_nodes.append(node)
                if node.get_value() == value:
                    return (node, searched_nodes)
        return None

    def set_associated_nodes(self) -> None:
        associated_nodes = {}
        associated_temp = []
        init_index = -1
        end_index = -1
        for _, node in enumerate(self.__ring):
            if node.is_active():
                next_node = node.get_next_node()
                if next_node.is_active():
                    init_index = node.get_key()
                    end_index = next_node.get_key()
                    if init_index > end_index:
                        associated_temp.extend(self.__ring[init_index +
                                                           1: len(self.__ring)])
                        associated_temp.extend(
                            self.__ring[0:end_index+1])
                    else:
                        associated_temp.extend(self.__ring[init_index +
                                                           1:end_index+1])
                associated_nodes.clear()
                for ass_node in associated_temp:
                    associated_nodes.update(
                        {ass_node.get_key(): ass_node.get_value()})
                next_node.set_associated_keys(associated_nodes)
            associated_temp.clear()

    def next_node(self) -> None:
        previous_node = -1
        first_node = -1

        for node_index, node in enumerate(self.__ring):
            if node.is_active():
                if previous_node >= 0:
                    self.__ring[previous_node].set_next_node(node)
                else:
                    first_node = node
                previous_node = node_index

        self.__ring[previous_node].set_next_node(first_node)

    def activate_initial_nodes(self) -> None:

        for index, _ in enumerate(self.__active_nodes):
            node_index = self.__active_nodes[index]
            node = self.__ring[node_index]
            node.active(True)

    def start(self) -> None:
        self.activate_initial_nodes()
        self.next_node()
        self.set_associated_nodes()

    def print(self) -> None:

        print(f"Active Nodes: {self.get_amount_active_nodes()}")
        print("=====================================")

        for node in self.__ring:
            if node.is_active():
                sleep(1)
                print(f"Key: {node.get_key()}")
                print(f"Value: {node.get_value()}")
                print(f"Active: {node.is_active()}")
                print(f"Next: {node.get_next_node().get_key()}")
                print(f"Associated Keys: {node.get_associated_keys()}")
                print("=====================================")
