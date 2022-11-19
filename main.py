from time import sleep
from Node import Node
from Chord import Chord
from Utils import Utils

# Setting for Chord Ring
RING_SIZE = 16
AMOUNT_ACTIVE_NODES = 6
NODES = (1, 4, 7, 12, 15)

# Generating the nodes
random_active_nodes = Utils().generate_random_active_nodes(
    AMOUNT_ACTIVE_NODES, RING_SIZE)
active_nodes = Utils().generate_active_nodes(NODES)

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
    print("Starting the system...")
    sleep(1)

    # Show the ring
    print("\n> Ring:")
    chord.print()
    sleep(1)

    # Searching a content
    VALUE = input("\n> Enter the value to search: ")
    sleep(1)

    SEARCH_RESULT = chord.find(VALUE)
    print(f"\n> SEARCHING FOR: {VALUE}")

    if SEARCH_RESULT is not None:

        sleep(1)
        FOUND_NODE = SEARCH_RESULT[0]
        SEARCHED_NODES = SEARCH_RESULT[1]

        print(f"\n> FOUND IN: {FOUND_NODE.get_key()}")
        sleep(1)

        print("\n> Node info:")
        chord.print_node(FOUND_NODE.get_key())
        sleep(1)

        print("\n> Searched nodes:\n")
        for node in SEARCHED_NODES:
            sleep(1)
            chord.print_node(node.get_key())
            print("=====================================")
    else:
        sleep(1)
        print("NOT FOUND")
