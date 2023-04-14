RED = True
BLACK = False

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.color = BLACK
		self.node_count = 1

class RedBlackBSTree:
	def __init__(self):
		self.root = None

	def _recursive_validity_check(self, node, current_black_depth=0, max_black_depth=None):
		if node is not None:

			# Check 1 : ensure there are no right-leaning red links
			if node.right is not None and node.right.color == RED:
				return false

			# Check 2 : ensure no node has 2 red links connected to it
			if node.left is not None:
				if node.color == RED and node.left.color == RED:
					return false

			# Check 3: ensure perfect black balance
			if node.left is None and node.right is None:
				# This is a leaf
				if max_black_depth is None:
					# If this is the first leaf encountered, set the max_depth value
					max_black_depth = current_black_depth
				else :
					if current_black_depth != max_black_depth:
						return False

			# Proceed down the tree
			if node.left is not None:
				current_black_depth = current_black_depth + 1
				tree_valid, current_black_depth = self._recursive_validity_check(
					node.left, 
					current_black_depth, 
					max_black_depth)
			if node.right is not None:
				current_black_depth = current_black_depth + 1
				tree_valid, current_black_depth = self._recursive_validity_check(
					node.right, 
					current_black_depth , 
					max_black_depth)
			return (True, current_black_depth - 1)

