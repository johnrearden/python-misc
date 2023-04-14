import random
import sys

def main():
	data = []
	for i in range(30):
		data.append(i)
	random.shuffle(data)
	print(data)
	insertion_sort(data)
	print(data)


def selection_sort(data):
	for i in range(len(data)):
		min_index = i
		for j in range(i + 1, len(data)):
			if data[j] < data[min_index]:
				min_index = j
		temp = data[i]
		data[i] = data[min_index]
		data[min_index] = temp

def insertion_sort(data):
	for i in range(0, len(data)):
		temp = data[i]
		for j in range(i):
			if temp < data[j]:
				# Move everything from i - 1 to j forward 1
				for k in range(i - 1, j - 1, -1):
					data[k + 1] = data[k]
				data[j] = temp
				break

if __name__ == '__main__':
	main()

