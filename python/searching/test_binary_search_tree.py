import pytest
import random
from binary_search_tree import BSTree

SAMPLE_TREE_MEDIUM_SIZE = 1

@pytest.fixture
def sample_tree_small():
	bstree = BSTree()
	bstree.put(5, 'five')
	bstree.put(3, 'three')
	bstree.put(2, 'two')
	bstree.put(1, 'one')
	bstree.put(4, 'four')
	return bstree

@pytest.fixture
def sample_tree_medium():
	bstree = BSTree()
	key_list = []
	for i in range(SAMPLE_TREE_MEDIUM_SIZE):
		key_list.append(i)
	random.shuffle(key_list)
	for key in key_list:
		bstree.put(key, 'dummy value')
	return bstree

def test_should_create_bstree():
	bstree = BSTree()
	assert bstree is not None

def test_tree_should_contain_key_after_insert():
	key = 1
	value = 'a'
	bstree = BSTree()
	bstree.put(key, value)
	assert(bstree.contains(key) == True)

def test_contain_should_return_false_on_missing_key():
	bstree = BSTree()
	bstree.put(1, 'one')
	assert(bstree.contains(2) == False)

def test_get_should_raise_exception_on_empty_tree():
	bstree = BSTree()
	missing_key = -1
	with pytest.raises(KeyError) as exception_info:
		bstree.get(missing_key)
	assert exception_info.value.args[0] == missing_key

def test_tree_accepts_multiple_inserts():
	bstree = BSTree()
	bstree.put(1, 'one')
	bstree.put(3, 'three')
	bstree.put(2, 'two')

def test_min_returns_smallest_key(sample_tree_small):
	assert(sample_tree_small.min() == 1)

def test_max_returns_largest_key(sample_tree_small):
	assert(sample_tree_small.max() == 5)

def test_keys_returns_ordered_list(sample_tree_small):
	keys = sample_tree_small.keys()
	print (keys)
	assert keys == sorted(keys)

def test_keys_returns_all_inserted_keys(sample_tree_medium):
	assert len(sample_tree_medium.keys()) == SAMPLE_TREE_MEDIUM_SIZE	

def test_node_count_is_correct_for_root(sample_tree_small):
	assert sample_tree_small.root.node_count == 5

def test_putting_existing_key_replaces_value(sample_tree_small):
	sample_tree_small.put(1, 'replacement')
	assert sample_tree_small.get(1) == 'replacement'

def test_putting_existing_key_does_not_increase_node_count(sample_tree_small):
	initial_node_count = sample_tree_small.root.node_count
	sample_tree_small.put(2, 'replacement')
	sample_tree_small.put(2, 'another replacement')
	assert sample_tree_small.root.node_count == initial_node_count

def test_rank_returns_correct_value():
	bstree = BSTree()
	NUM_KEYS = 20
	key_list = []
	for i in range(NUM_KEYS):
		key_list.append(i)
	random.shuffle(key_list)
	for key in key_list:
		bstree.put(key, 'dummy value')
	test_key = random.randrange(NUM_KEYS)
	assert bstree.rank(test_key) == test_key

def test_size_returns_correct_number(sample_tree_medium):
	assert sample_tree_medium.size() == SAMPLE_TREE_MEDIUM_SIZE

def test_floor_returns_key_if_exists(sample_tree_medium):
	test_key = random.randrange(SAMPLE_TREE_MEDIUM_SIZE)
	assert sample_tree_medium.floor(test_key) == test_key

def test_floor_is_correct_if_key_not_exists():
	bstree = BSTree()
	key_list = []
	test_key = random.randrange(1, 20)
	for i in range(20):
		if i != test_key:
			key_list.append(i)
	random.shuffle(key_list)
	for key in key_list:
		bstree.put(key, 'Dummy value')
	assert bstree.floor(test_key) == test_key - 1

def test_ceiling_returns_key_if_exists(sample_tree_medium):
	test_key = random.randrange(SAMPLE_TREE_MEDIUM_SIZE)
	assert sample_tree_medium.ceiling(test_key) == test_key

def test_ceiling_is_correct_if_key_not_exists():
	bstree = BSTree()
	key_list = []
	test_key = random.randrange(0, 19)
	for i in range(20):
		if i != test_key:
			key_list.append(i)
	random.shuffle(key_list)
	for key in key_list:
		bstree.put(key, 'Dummy value')
	assert bstree.ceiling(test_key) == test_key + 1

def test_delete_min_removes_smallest_key(sample_tree_medium):
	smallest_key = sample_tree_medium.min()
	sample_tree_medium.delete_min()
	assert sample_tree_medium.contains(smallest_key) is False

def test_size_is_correct_after_delete_min(sample_tree_medium):
	sample_tree_medium.delete_min()
	assert sample_tree_medium.size() == SAMPLE_TREE_MEDIUM_SIZE - 1

def test_tree_is_valid_after_delete_min(sample_tree_medium):
	sample_tree_medium.delete_min()
	assert sample_tree_medium._is_tree_valid() is True

def test_sample_tree_medium_is_valid(sample_tree_medium):
	assert sample_tree_medium._is_tree_valid() is True

def test_delete_max_removes_largest_key(sample_tree_medium):
	largest_key = sample_tree_medium.max()
	sample_tree_medium.delete_max()
	assert sample_tree_medium.contains(largest_key) is False

def test_size_is_correct_after_delete_max(sample_tree_medium):
	sample_tree_medium.delete_max()
	assert sample_tree_medium.size() == SAMPLE_TREE_MEDIUM_SIZE - 1

def test_tree_does_not_contain_key_after_delete(sample_tree_medium):
	test_key = random.randrange(SAMPLE_TREE_MEDIUM_SIZE)
	sample_tree_medium.delete(test_key)
	assert sample_tree_medium.contains(test_key) is False

def test_size_is_correct_after_delete(sample_tree_medium):
	test_key = random.randrange(SAMPLE_TREE_MEDIUM_SIZE)
	sample_tree_medium.delete(test_key)
	sample_tree_medium._enumerate(sample_tree_medium.root)
	assert sample_tree_medium.size() == SAMPLE_TREE_MEDIUM_SIZE - 1

def test_recalculate_node_count_recursively(sample_tree_medium):
	sample_tree_medium._enumerate(sample_tree_medium.root)
	original_size = sample_tree_medium.size()
	sample_tree_medium._recalculate_node_count_recursively(sample_tree_medium.root)
	assert original_size == sample_tree_medium.size()









