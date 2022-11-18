from Node import Node
from Chord import Chord

if __name__ == "__main__":
    
    ring_size = 16
    amount_active_nodes = 4
    node = None
    chord = Chord(amount_active_nodes)

    # Generating the nodes
    for node_index in range(ring_size):
        node = Node()
        node.setKey(node_index)
        node.setValue(f"Node {node_index}")
        chord.addNode(node)
    
    # Starting the system
    chord.start()
    chord.printRing()