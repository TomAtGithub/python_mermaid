from python_mermaid.diagram import MermaidDiagram
from .utils import *

def test_setup_diagram_with_only_a_title():
    m = MermaidDiagram(title=DUMMY_TITLE, type="sequenceDiagram")
    diagram = """---
title: My diagram
---
sequenceDiagram""";
    assert str(m) == diagram

def test_diagram_with_only_a_participant():
    m = MermaidDiagram(title=DUMMY_TITLE, type="sequenceDiagram",
        nodes=[NODE_1])
    print(m)
    diagram = """---
title: My diagram
---
sequenceDiagram
participant my_first_node as My first node""";

    print(diagram)
    assert str(m) == diagram

def test_diagram_with_only_an_actor():
    m = MermaidDiagram(title=DUMMY_TITLE, type="sequenceDiagram",
        nodes=[NODE_1_ACTOR])
    diagram = """---
title: My diagram
---
sequenceDiagram
actor my_first_node as My first node""";
    assert str(m) == diagram
