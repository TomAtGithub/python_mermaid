from .node import AbstractNode, StateNode, SequenceNode

# Link are created following the documentation here :
# https://mermaid.js.org/syntax/flowchart.html#links-between-nodes
LINK_SHAPES = {
    "normal": "---",
    "dotted": "-.-",
    "thick": "==="
}

LINK_HEADS = {
    "none": "",
    "arrow": ">",
    "left-arrow": "<",
    "bullet": "o",
    "cross": "x"
}

# https://mermaid.js.org/syntax/sequenceDiagram.html#messages
SEQUENCE_LINK_SHAPES = {
    "solid": "-",
    "dotted": "--"
}
SEQUENCE_LINK_HEADS = {
    "none": ">",
    "arrow": ">>",
    "cross": "x",
    "open": ")"
}


class Link:
    def __init__(
        self,
        origin: AbstractNode,
        end: AbstractNode,
        shape: str = "normal",
        head_left: str = "none",
        head_right: str = "arrow",
        message: str = ""
    ):
        self.origin = origin
        self.end = end
        self.head_left = LINK_HEADS[head_left]
        self.head_right = LINK_HEADS[head_right]
        self.shape = LINK_SHAPES[shape]
        self.message = message

    def __str__(self):
        elements = [
            self.origin.id + " ",
            self.head_left,
            self.shape,
            self.head_right,
            f"|{self.message}|" if self.message else "",
            " " + self.end.id
        ]
        return "".join(elements)
    
class StateLink(Link):
    def __init__(self, origin: StateNode, end: StateNode, message: str = ""):
        super().__init__(origin, end, "normal", "none", "arrow", message)

    def __str__(self):
        element = f"{self.origin.id} --> {self.end.id}"
        if self.message != "":
            element += f": {self.message}"
        return element

class SequenceLink():
    def __init__(
        self, 
        origin: SequenceNode,
        end: SequenceNode,
        shape: str = "solid",
        head_right: str = "arrow",
        message: str = "",
        activate: bool = False,
        deactivate: bool = False
    ):
        self.origin = origin
        self.end = end    
        self.shape = SEQUENCE_LINK_SHAPES[shape]
        self.head_right = SEQUENCE_LINK_HEADS[head_right]
        self.message = message
        self.activate = activate
        self.deactivate = deactivate
    
    def __str__(self):
        activation = "+" if self.activate == True else "-" if self.deactivate == True else ""
        #\n%w is an workaround. For some reason does the mermaid live editor render links with no comment but the browser version from jsdelivery requires one
        #Added a newline and a comment seems to solve this
        message = self.message if self.message != "" else " \n%"

        element = f"{self.origin.id}{self.shape}{self.head_right}{activation}{self.end.id}:{message}"
        
        return element