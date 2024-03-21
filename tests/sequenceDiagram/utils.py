from python_mermaid.link import Link
from python_mermaid.node import SequenceNode
from python_mermaid.interaction import Interaction
from python_mermaid.diagram import (
    MermaidDiagram
)

DUMMY_TITLE = "My diagram"
NODE_1 = SequenceNode(
    "My first node"
)
NODE_2 = SequenceNode(
    "My second node"
)
NODE_1_ACTOR = SequenceNode(
    "My first node",
    shape="actor"
)
INTERACTION_1 = Interaction(
    NODE_1,
    args=["https://wikipedia.org"]
)
# BIG_NODE_1 = SequenceNode(
#     "My big node",
#     sub_nodes=[NODE_1]
# )
LINK_1 = Link(
    NODE_1,
    NODE_2
)
LINK_2 = Link(
    NODE_2,
    NODE_1
)
LINK_3 = Link(
    NODE_1,
    NODE_2,
    shape="thick"
)