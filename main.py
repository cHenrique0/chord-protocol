from Node import Node
from Chord import Chord
from Utils import Utils

RING_SIZE = 16
AMOUNT_ACTIVE_NODES = 4
PATH = "./data"
files = Utils().load_files(PATH)

if __name__ == "__main__":
    chord: Chord = Chord(AMOUNT_ACTIVE_NODES)

    # Generating the nodes
    for index in range(RING_SIZE):
        node = Node()
        node.set_key(index)
        node.set_value(files[index])
        chord.add_node(node)

    # Starting the system
    chord.start()
    # chord.print()
