from Node import Node
from Utils import Utils


class Chord:

    def __init__(self, active_nodes: int) -> None:
        self.__ring: list[Node] = []
        self.__amount_active_nodes: int = active_nodes

    def get_ring(self) -> list:
        return self.__ring

    def set_ring(self, ring: list) -> None:
        self.__ring = ring

    def get_amount_active_nodes(self) -> int:
        return self.__amount_active_nodes

    def set_amount_active_nodes(self, amount: int) -> None:
        self.__amount_active_nodes = amount

    def length(self) -> int:
        return len(self.__ring)

    def add_node(self, node: Node) -> None:
        self.__ring.append(node)

    def set_associated_nodes(self) -> None:
        associated_nodes = {}
        first_node = -1
        # end = 0

        for node_index in range(len(self.__ring) - 1, -1, -1):

            node = self.__ring[node_index]

            if node.is_active():
                node.set_associated_keys(associated_nodes)

                if first_node == -1:
                    first_node = node_index

            if first_node >= 0:
                associated_nodes.update({node.get_key(): node.get_value()})

            if node_index == 0:
                # end = first_node+1
                node_index = len(self.__ring)

    def next_node(self):
        previous_node = -1
        first_node = -1

        for node_index in range(len(self.__ring)):
            node = self.__ring[node_index]
            if node.is_active():
                if previous_node >= 0:
                    self.__ring[previous_node].set_next_node(node.get_key())
                else:
                    first_node = node.get_key()

                previous_node = node_index

        self.__ring[previous_node].set_next_node(first_node)

    def activate_initial_nodes(self) -> None:
        random_active_nodes: list[int] = Utils(
        ).generate_random_active_nodes(self.__amount_active_nodes)
        node = Node()
        # for e in enumerate(random_active_nodes):
        #     for i in e:
        #         node = self.__ring[i]
        #         node.active(True)
        for index in range(len(random_active_nodes)):
            node_index = random_active_nodes[index]
            node = self.__ring[node_index]
            node.active(True)

    def start(self) -> None:
        self.activate_initial_nodes()
        self.next_node()
        self.set_associated_nodes()

    def print(self) -> None:
        for node in self.__ring:
            if node.is_active():
                print(f"Key: {node.get_key()}")
                print(f"Value: {node.get_value()}")
                print(f"Active: {node.is_active()}")
                print(f"Next: {node.get_next_node()}")
                print(f"Associated Keys: {node.get_associated_keys()}")
                print("=====================================")

        print(f"Active Nodes: {self.get_amount_active_nodes()}")
        print("=====================================")
