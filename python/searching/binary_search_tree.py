class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.node_count = 1


	def __str__(self):
		left_report = 'None' if self.left == None else self.left
		right_report = 'None' if self.right == None else self.right
		str =  (f'''\nKey == {self.key}, value == {self.value}, left({self.key}) 
			== {left_report}, right({self.key}) == {right_report},
			node_count({self.key}) == {self.node_count}''')
		return str

class BSTree:
	def __init__(self):
		self.root = None

	def put(self, key, value):
		if self.root is None:
			self.root = Node(key, value)
		else :
			self._put(self.root, key, value)

	def get(self, key):
		if self.root is None:
			raise KeyError(key)
		node = self._search(self.root, key)
		if node is None:
			raise KeyError('key not found in tree')
		else: 
			return node.value

	def contains(self, key):
		try:
			self.get(key)
			return True
		except:
			return False

	def delete_min(self):
		self._delete_min(self.root, None)

	def _delete_min(self, node, parent):
		if node.left is None:
			if parent is not None:
				parent.left = node.right
			else:
				self.root = node.right
		else:
			self._delete_min(node.left, node)

		# Recalculate node_count for this node - this will filter back up the call stack
		count_left = node.left.node_count if node.left is not None else 0
		count_right = node.right.node_count if node.right is not None else 0
		node.node_count = count_right + count_left + 1

	def delete_max(self):
		self._delete_max(self.root, None)

	def _delete_max(self, node, parent):
		if node.right is None:
			if parent is not None:
				parent.right = node.left
			else: 
				self.root = node.left
		else:
			self._delete_max(node.right, node)

		# Recalculate node_count for this node - this will filter back up the call stack
		self._calculate_node_count(node)

	def delete(self, key):
		self._enumerate(self.root)
		print(f'key to delete is {key}')
		if not self.contains(key):
			raise KeyError('key does not exist')
		else:
			node, parent, side = self._search_and_return_parent(self.root, key, None, None)
			if parent is None:
				if self.root.right is not None:
					min_of_right_sub_child = self._min(self.root.right)
					min_of_right_sub_child.left = self.root.left
					self.root = self.root.right
				else:
					self.root = self.root.left 
			else:
				# Reassign the parent link to the nodes right child, and link the 
				# left child to the min of the right child.
				if side == 'left':
					if node.right is not None:
						parent.left = node.right
						min_of_right_sub_child = self._min(node.right)
						min_of_right_sub_child.left = node.left
					else:
						parent.left = node.left
				else :
					if node.right is not None:
						parent.right = node.right
						min_of_right_sub_child = self._min(node.right)
						min_of_right_sub_child.left = node.left
					else:
						parent.right = node.left
		self._recalculate_node_count_recursively(self.root)
		

	def keys(self):
		key_list = []
		if self.root == None:
			return key_list
		else: 
			self._add_child_keys(key_list, self.root)
			return key_list

	def floor(self, key):
		return self._floor(self.root, key)

	def _floor(self, node, key):
		if key == node.key:
			return key
		elif key < node.key and node.left is not None:
			return self._floor(node.left, key)
		else:
			return self._floor_of_right_node(node, key)

	def _floor_of_right_node(self, node, key):
		if node.right is None:
			return node.key
		else: 
			floor_of_right_node = self._floor(node.right, key)
			if floor_of_right_node <= key:
				return floor_of_right_node
			else: 
				return node.key

	def ceiling(self, key):
		return self._ceiling(self.root, key)

	def _ceiling(self, node, key):
		if key == node.key:
			return key
		elif key > node.key and node.right is not None:
			return self._ceiling(node.right, key)
		else:
			return self._ceiling_of_left_node(node, key)

	def _ceiling_of_left_node(self, node, key):
		if node.left is None:
			return node.key
		else:
			ceiling_of_left_node = self._ceiling(node.left, key)
			if ceiling_of_left_node >= key:
				return ceiling_of_left_node
			else:
				return node.key

	def max(self):
		return self._max(self.root).key

	def _max(self, node):
		if node.right is None:
			return node
		else:
			return self._max(node.right)

	def min(self):
		return self._min(self.root).key

	def _min(self, node):
		if node.left is None:
			return node
		else:
			return self._min(node.left)

	def rank(self, key):
		return self._rank(self.root, key)

	def _rank(self, node, key):
		if key == node.key:
			left_count = node.left.node_count if node.left is not None else 0
			return left_count
		elif key < node.key:
			if node.left == None:
				raise KeyError('Key does not exist')
			else:
				return self._rank(node.left, key)
		else:
			left_count = node.left.node_count if node.left is not None else 0
			return left_count + 1 + self._rank(node.right, key) 

	def size(self):
		return self.root.node_count if self.root is not None else 0

	def _add_child_keys(self, list, node):
		if node.left is not None:
			self._add_child_keys(list, node.left)
		list.append(node.key)
		if node.right is not None:
			self._add_child_keys(list, node.right)


	def _search(self, node, key):
		if key < node.key:
			return self._search(node.left, key)
		elif key > node.key:
			return self._search(node.right, key)
		else:
			return node

	def _search_and_return_parent(self, node, key, parent, side):
		if key < node.key:
			return self._search_and_return_parent(node.left, key, node, 'left')
		elif key > node.key:
			return self._search_and_return_parent(node.right, key, node, 'right')
		else: 
			return node, parent, side


	def _put(self, node, key, value):

		# Go down the tree recursively until the correct empty link is found.

		# If the key is equal to self.key, then replace the value.
		if key == node.key:
			node.value = value
			return

		# If key is smaller, check left branch
		if key < node.key:
			if node.left == None:
				node.left = Node(key, value)
				node.node_count = node.node_count + 1
			else:
				self._put(node.left, key, value)
		# If key is larger, check right branch
		elif key > node.key:
			if node.right == None:
				node.right = Node(key, value)
				node.node_count = node.node_count + 1
			else:
				self._put(node.right, key, value)
		
		# Recalculate node_count for this node - this will filter back up the call stack
		self._calculate_node_count(node)

	def _calculate_node_count(self, node):
		count_left = node.left.node_count if node.left is not None else 0
		count_right = node.right.node_count if node.right is not None else 0
		node.node_count = count_right + count_left + 1

	def _enumerate(self, node):
		print(node)

	def _is_tree_valid(self):
		if self.root is None:
			return True
		else:
			return self._check_children(self.root)

	def _check_children(self, node):
		if node.left is not None:
			if node.left.key > node.key:
				return False
			else:
				return self._check_children(node.left)
		if node.right is not None:
			if node.right.key < node.key:
				return False
			else:
				return self._check_children(node.right)
		return True

	def _recalculate_node_count_recursively(self, node):
		if node is None:
			return 0
		print(f'testing node {node.key}')
		if node.left is not None:
			self._recalculate_node_count_recursively(node.left)
		if node.right is not None:
			self._recalculate_node_count_recursively(node.right)
			
		self._calculate_node_count(node)
		

