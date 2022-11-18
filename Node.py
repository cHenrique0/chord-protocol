class Node:
    def __init__(self):
        self.key = None
        self.value = ""
        self.associated_keys = {}
        self.active_node = False
        self.next_node = None
    
    def getKey(self) -> int:
        return self.key
    
    def setKey(self, key: int) -> None:
        self.key = key
    
    def getValue(self) -> str:
        return self.value
    
    def setValue(self, value: str) -> None:
        self.value = value
    
    def getAssociatedKeys(self) -> dict:
        return self.associated_keys
    
    def setAssociatedKeys(self, associated_keys: dict) -> None:
        self.associated_keys = associated_keys
    
    def getActiveNode(self) -> bool:
        return self.active_node
    
    def setActiveNode(self, active: bool) -> None:
        self.active_node = active
    
    def getNextNode(self) -> int:
        return self.next_node
    
    def setNextNode(self, node: int) -> None:
        self.next_node = node

