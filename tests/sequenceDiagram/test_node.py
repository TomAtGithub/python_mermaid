import pytest
from .utils import *

def test_node():
    assert str("participant my_first_node as My first node") == str(NODE_1)

def test_node_with_content():
    assert str("participant a as Alice") == str(NODE_3)

def test_node_with_content_and_shape():
    assert str("actor a as Alice") == str(NODE_4)