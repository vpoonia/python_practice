def Binary_search(arr,element):
	start_index = 0
	last_index = len(arr)-1
	mid=0
	while (start_index<= last_index):
		mid =int((start_index+last_index)/2)
		if (element == arr[mid][1]):
			return mid
		elif (element>arr[mid][1]):
			start_index = mid+1
		elif (element<arr[mid][1]):
			last_index = mid-1
	return last_index

def bisect_left(arr, threshold):
	insert_index =Binary_search(arr, threshold)
	if insert_index<0:
		return []
	else:
		return arr[:insert_index+1]


def std_lib_main(max_distance, forwards_routes, backward_routes):
	from bisect import bisect
	forwards_routes.sort(key=lambda x: x[1])
	backward_routes.sort(key=lambda x: x[1])
	forwards_routes = forwards_routes[:bisect([item[1] for item in forwards_routes], max_distance)]
	if not forwards_routes:
		return []
	possible_combs = []
	for item in forwards_routes:
		temp_list = backward_routes[:bisect([i[1] for i in backward_routes], max_distance-item[1])]
		if not temp_list:
			break
		possible_combs.extend([[item[0], backward_item[0],max_distance-item[1]-backward_item[1]]for backward_item in temp_list])
	possible_combs.sort(key=lambda x: x[2])
	if not possible_combs:
		return []
	return [[item[0],item[1]] for item in possible_combs if item[2]==possible_combs[0][2]]


def simple_main(max_distance, forwards_routes, backward_routes):
	forwards_routes = [item for item in forwards_routes if item[1]<=max_distance]
	if not forwards_routes:
		return []
	forwards_routes.sort(key=lambda x: x[1])
	possible_combs = []
	for item in forwards_routes:
		temp_list = [backward_item for backward_item in backward_routes if backward_item[1]+item[1]<=max_distance]
		if not temp_list:
			break
		possible_combs.extend([[item[0], backward_item[0],max_distance-item[1]-backward_item[1]]for backward_item in temp_list])
	possible_combs.sort(key=lambda x: x[2])
	if not possible_combs:
		return []
	return [[item[0],item[1]] for item in possible_combs if item[2]==possible_combs[0][2]]
		

def main(max_distance, forwards_routes, backward_routes):
	forwards_routes.sort(key=lambda x: x[1])
	backward_routes.sort(key=lambda x: x[1])
	forwards_routes = bisect_left(forwards_routes, max_distance)
	if not forwards_routes:
		return []
	possible_combs = []
	for item in forwards_routes:
		temp_list =bisect_left(backward_routes, max_distance-item[1])
		if not temp_list:
			break
		possible_combs.extend([[item[0], backward_item[0],max_distance-item[1]-backward_item[1]]for backward_item in temp_list])
	possible_combs.sort(key=lambda x: x[2])
	if not possible_combs:
		return []
	return [[item[0],item[1]] for item in possible_combs if item[2]==possible_combs[0][2]]


if __name__=='__main__':
	max_distance = 10000
	forwards_routes = [[1,2000], [3,5000], [2,3000],[4,7000]]
	backward_routes = [[1,3000],[2,7000]]
	print(main(max_distance, forwards_routes, backward_routes))
	print(simple_main(max_distance, forwards_routes, backward_routes))
	print(std_lib_main(max_distance, forwards_routes, backward_routes))
