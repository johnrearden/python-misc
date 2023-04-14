from hashtable import HashTable
import random
import time
import math
import pandas


def main():
	results = []
	initial_counter = 16
	counter = initial_counter
	prev_result = 0
	while counter < 21:
		res = test_hashtable(2**counter)
		if prev_result == 0:
			ratio = 0
		else:
			ratio = res[1] / prev_result
		counter = counter + 1
		prev_result = res[1]
		results.append((res[0], res[1], res[2], ratio))

	
	df = pandas.DataFrame(results, columns=['number', 'time', 'log_2', 'ratio'])
	print(df)


def test_hashtable(num_elements=100000):
	
	# Assemble list of test data and shuffle it so that keys are unordered
	htable = HashTable(capacity=num_elements)
	data = []
	results = []
	for i in range(num_elements):
		val = random.randrange(0, 100)
		tup = (i, val)
		data.append(tup)
	random.shuffle(data)

	# Begin test
	print(f'Testing hashtable implementation with {num_elements} elements')
	start = time.time()
	insert_data_in_hashtable(htable, data)
	elapsed_time = time.time() - start
	print(f'Insertion took {elapsed_time} seconds')
	log_2 = math.log(num_elements, 2)
	print(f'Log {num_elements} to base 2 is {log_2}')
	return(num_elements, elapsed_time, log_2)
	

def insert_data_in_hashtable(htable, data):
	for element in data:
		htable[element[0]] = element[1]


if __name__ == '__main__':
	main()

