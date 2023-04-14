import pytest
from red_black_bst import Node, RedBlackBSTree

def test_should_create_rbbst():
	rbbst = RedBlackBSTree()
	assert rbbst is not None