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

    def get_node(self, key: int) -> Node:
        return self.__ring[key]

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
        start_index = -1
        end_index = -1
        for _, node in enumerate(self.__ring):
            if node.is_active():
                next_node = node.get_next_node()
                if next_node.is_active():
                    start_index = node.get_key()
                    end_index = next_node.get_key()
                    if start_index > end_index:
                        associated_temp.extend(self.__ring[start_index +
                                                           1: len(self.__ring)])
                        associated_temp.extend(
                            self.__ring[0:end_index+1])
                    else:
                        associated_temp.extend(self.__ring[start_index +
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

    def generate_table(self, table_length: int) -> None:
        ftp = 0
        node_ftp = []
        table = {}
        next_node: Node
        for index, node in enumerate(self.__ring):
            if node.is_active():
                node_ftp.clear()
                for table_index in range(1, table_length+1):
                    ftp = node.get_key() + 2**(table_index-1)
                    next_node = Node()
                    if ftp >= self.length():
                        ftp -= self.length()
                        # node = self.get_node(ftp)
                        next_node = self.get_node(ftp)
                        while next_node.is_active() is False:
                            ftp += 1
                            next_node = self.get_node(ftp)
                            # node = self.get_node(ftp)
                    # next_node = self.get_node(ftp)
                    tmp_node = node
                    tmp_next_node_active = node.get_next_node()
                    if not next_node.is_active():
                        next_node_active = node.get_next_node()
                        # tmp_node = node
                        # tmp_next_node_active = next_node_active
                        while ftp > next_node_active.get_key():
                            node = next_node_active
                            next_node_active = node.get_next_node()
                            if next_node_active.get_key() == 0 or next_node_active.get_key() == 1:
                                break
                        node_ftp.append(next_node_active.get_key())
                        # node = tmp_node
                        # next_node_active = tmp_next_node_active
                    elif next_node.is_active():
                        node_ftp.append(next_node.get_key())
                    node = tmp_node
                    next_node_active = tmp_next_node_active
                table.update({index: node_ftp.copy()})
                node.set_finger_table(node_ftp)
        # print(table)

    def print_finger_table(self) -> None:
        for _, node in enumerate(self.__ring):
            if node.is_active():
                print(f"Node {node.get_key()}: {node.get_finger_table()}")

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
