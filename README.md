# Chord Protocol - DHT

A small project that simulates the chord protocol made as homework of the discipline of Distributed Systems at UFMA.

* This project was made with `python 3.
10`

## Instructions

Homework: Peer-to-peer architecture

Description:
- Implement the chord protocol in a language of your choice.
- The program must simulate a distributed system with several nodes.
- The finger table must be assembled for each node.
- Input: a node key
- Output: the ids of all nodes the request passed through until it found the node responsible for the key.


## Run the project

```sh
git clone git@github.com:cHenrique0/chord-protocol.git

cd chord-protocol

pip intall --upgrade pip

pip install networkx

python main.py
```