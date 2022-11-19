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

    """public int retornarChave(Map associados, String valor) {
        // Se não encontrar: retorna -1
        int chave = -1;
        Set<Map.Entry<Integer, String>> pares = associados.entrySet();
        for (Map.Entry<Integer, String> par : pares) {
            if ((String)par.getValue().equals(valor)) {
                chave = par.getKey();
            }
        }
        return chave;
    }
    """

    def find(self, key: int, value: str) -> Node | int:
        node: Node
        associated_nodes = {}
        node_index = key
        next_node = 0

        for index in range(1, self.__amount_active_nodes):
            next_node = self.get_next_node_key(node_index)
            node = self.__ring[next_node]
            associated_nodes = node.get_associated_keys()

            # if associados.containsValue(valorBuscado)
            if associated_nodes[index] == value:
                return self.get_node_key(associated_nodes, value)

            node_index = next_node

        return -1

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
                        associated_temp.reverse()
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
        random_active_nodes: list[int] = Utils(
        ).generate_random_active_nodes(self.__amount_active_nodes)

        for index, _ in enumerate(random_active_nodes):
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
                print(f"Next: {node.get_next_node().get_key()}")
                print(f"Associated Keys: {node.get_associated_keys()}")
                print("=====================================")

        print(f"Active Nodes: {self.get_amount_active_nodes()}")
        print("=====================================")
