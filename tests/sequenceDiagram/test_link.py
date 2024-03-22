import pytest
from python_mermaid.link import SequenceLink
from .utils import *

def test_link_without_message():
    assert str(LINK_1) == f"{LINK_1.origin.id}->>{LINK_1.end.id}: "

def test_link_without_message_and_dotted_shape():
    assert str(LINK_2) == f"{LINK_2.origin.id}-->>{LINK_2.end.id}: "

def test_link_with_message():
    assert str(LINK_3) == f"{LINK_3.origin.id}->{LINK_3.end.id}:{LINK_3.message}"

def test_link_with_activation():
    assert str(LINK_4) == f"{LINK_4.origin.id}->>+{LINK_4.end.id}: "

def test_link_with_deactivation():
    assert str(LINK_5) == f"{LINK_5.origin.id}->>-{LINK_5.end.id}: "
