from python_mermaid.link import SequenceLink
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
NODE_3 = SequenceNode(
    id="A",
    content="Alice"
)
NODE_4 = SequenceNode(
    id="A",
    content="Alice",
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
LINK_1 = SequenceLink(
    NODE_1,
    NODE_2
)
LINK_2 = SequenceLink(
    NODE_2,
    NODE_1,
    shape="dotted"
)
LINK_3 = SequenceLink(
    NODE_1,
    NODE_2,
    head_right="none",
    message="some message"
)
LINK_4 = SequenceLink(
    NODE_1,
    NODE_2,
    activate=True
)
LINK_5 = SequenceLink(
    NODE_1,
    NODE_2,
    deactivate=True
)