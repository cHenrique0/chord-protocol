from time import sleep
from Node import Node
from Chord import Chord
from Utils import Utils

# Setting for Chord Ring
# [1] - for exemples/ring_1.png
# RING_SIZE = 16
# NODES = (1, 6, 11, 13)

# [2] - for exemples/ring_2.png
RING_SIZE = 32
NODES = (1, 4, 9, 11, 14, 18, 20, 21, 28)

# [3] - for exemples/ring_3.png
# RING_SIZE = 16
# NODES = (1, 4, 7, 12, 15)

AMOUNT_ACTIVE_NODES = len(NODES)

# Generating the nodes
# If you want generate random nodes
# random_active_nodes = Utils().generate_random_active_nodes(
#     AMOUNT_ACTIVE_NODES, RING_SIZE)

# If you want to use the nodes defined in NODES
active_nodes = Utils().generate_active_nodes(NODES)

# Creating mock values to the keys in nodes (max nodes = 32)
# Path to the files
PATH = "./data"
# Loading the files
files = Utils().load_files(PATH)

# Main
if __name__ == "__main__":
    # Initializing the chord ring
    chord: Chord = Chord(active_nodes)

    # Creating the nodes
    for index in range(RING_SIZE):
        node = Node()
        node.set_key(index)
        node.set_value(files[index])
        chord.add_node(node)

    # Starting the system
    chord.start()
    print("STARTING THE SYSTEM...")
    sleep(1)
    print(f"GENERATING THE RING FOR NODES: {NODES}")
    sleep(1)

    # # Showing the ring
    print("\n> RING:")
    chord.print()
    sleep(1)

    # Generating the finger table for the active nodes
    chord.generate_table(table_length=5)
    sleep(1)

    # Searching a content
    KEY = int(input("\n> Enter the key to search: ").strip())
    START = int(input("> Enter the start node: ").strip())
    sleep(1)

    SEARCH_RESULT = chord.find(KEY, START)
    print(f"\n> SEARCHING FOR: {KEY}")

    if SEARCH_RESULT is not None:

        sleep(1)
        FOUND_NODE = SEARCH_RESULT[0]
        SEARCHED_NODES = SEARCH_RESULT[1]

        print(f"\n> FOUND IN: {FOUND_NODE.get_key()}")
        sleep(1)

        print("\n> NODE INFO:")
        chord.print_node(FOUND_NODE.get_key())
        sleep(1)

        print("\n> SEARCHED NODES:\n")
        for node in SEARCHED_NODES:
            sleep(1)
            chord.print_node(node.get_key())
            print("=====================================")
    else:
        sleep(1)
        print("NOT FOUND")

    # Showing the finger table for the active nodes
    print("\n> FINGER TABLES:")
    chord.print_finger_table()
