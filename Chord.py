from time import sleep
from Node import Node
import matplotlib.pyplot as plt
import networkx as nx


class Chord:

    def __init__(self, active_nodes: list[int]) -> None:
        self.__ring: list[Node] = []
        self.__amount_active_nodes: int = len(active_nodes)
        self.__active_nodes: list[int] = active_nodes
        self.__searched_nodes: list[Node] = []

    def get_ring(self) -> list[Node]:
        return self.__ring

    def set_ring(self, ring: list[Node]) -> None:
        self.__ring = ring

    def get_node(self, key: int) -> Node:
        return self.__ring[key]

    def print_node(self, key: int) -> None:

        node: Node = self.__ring[key]

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

    def find(self, key: int, start: int) -> tuple[Node, list[Node]] | None:

        node: Node = self.get_node(start)
        finger_table: list[int] = []

        if node not in self.__searched_nodes:
            self.__searched_nodes.append(node)

        if node.is_active():
            if key not in node.get_associated_keys():
                finger_table.extend(node.get_finger_table())
                for tab_index, node_key in enumerate(finger_table):
                    if tab_index == len(finger_table)-1:
                        self.__searched_nodes.append(self.get_node(node_key))
                        return self.find(key, node_key)
                    if node_key < key <= finger_table[tab_index+1]:
                        self.__searched_nodes.append(self.get_node(node_key))
                        return self.find(key, node_key)
                    if key <= finger_table[tab_index + 1]:
                        self.__searched_nodes.append(self.get_node(
                            finger_table[tab_index + 1]))
                        return self.find(key, finger_table[tab_index + 1])
            if key in node.get_associated_keys():
                return (node, self.__searched_nodes)

        if not node.is_active():
            start += 1
            return self.find(key, start)

        return None

    def set_associated_nodes(self) -> None:

        associated_nodes: dict[int, str] = {}
        associated_temp: list[Node] = []
        start_index: int = -1
        end_index: int = -1

        for _, node in enumerate(self.__ring):
            if node.is_active():
                next_node: Node = node.get_next_node()
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

        previous_node: Node | None = None
        first_node: Node | None = None

        for _, node in enumerate(self.__ring):
            if node.is_active():
                if previous_node is not None and previous_node.get_key() >= 0:
                    self.__ring[previous_node.get_key()].set_next_node(node)
                else:
                    first_node = node
                previous_node = node

        if previous_node is not None and first_node is not None:
            self.__ring[previous_node.get_key()].set_next_node(first_node)

    def activate_initial_nodes(self) -> None:

        for index, _ in enumerate(self.__active_nodes):
            node_index = self.__active_nodes[index]
            node = self.__ring[node_index]
            node.active(True)

    def generate_table(self, table_length: int) -> None:

        ftp: int = 0
        node_ftp: list[int] = []
        next_node: Node
        next_node_active: Node
        tmp_node: Node
        tmp_next_node_active: Node

        for _, node in enumerate(self.__ring):
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
                node.set_finger_table(node_ftp)
        # print(table)

    def print_finger_table(self) -> None:

        # for _, node in enumerate(self.__ring):
        for _, node in enumerate(self.__searched_nodes):
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

    def show_graph(self) -> None:

        # Graph
        graph = nx.DiGraph()
        pos = nx.circular_layout(graph)

        # Nodes
        nodes = [node.get_key() for node in self.__ring]
        graph.add_nodes_from(nodes)

        # Edges
        edges = []
        for index, node in enumerate(nodes):
            if index < len(nodes) - 1:
                edges.append((node, index+1))
            else:
                edges.append((node, 0))
        graph.add_edges_from(edges)

        # add extra edges (path through searched nodes)
        searched_nodes = [node.get_key() for node in self.__searched_nodes]
        for index, node in enumerate(searched_nodes):
            if index < len(searched_nodes) - 1:
                graph.add_edge(node, searched_nodes[index+1])

        # Labels
        labels = {}
        for index, node in enumerate(nodes):
            labels[index] = f"{node}"

        opitions = {"node_size": 500,
                    "font_size": 16, "font_color": "white"}
        nx.draw_circular(graph, with_labels=True, **opitions)

        plt.axis("off")
        plt.show()
