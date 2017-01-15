def big_weights(items, trips):
	for item in range(len(items)-1, -1, -1):
		if items[item] >= 50:
			trips=trips+1
			items.pop(item)
			if items != []:
				return big_weights(items, trips)
	return trips		

def small_weights(items, trips):
	last_item=items[-1]
	required_items=50//last_item
	if required_items > len(items):
		return trips
	else:
		if items != []:
			items.pop(-1)
			trips=trips+1
			while required_items > 0 and items !=[]:
				items.pop(0)
				required_items=required_items-1
			if len(items)>1:
				return small_weights(items, trips)
		return trips


def no_of_trips():
	with open('lazy_loading.txt', 'r') as f:
		m = list(map(int, (f.read().strip('\n').split('\n'))))
		T=m.pop(0)
		with open("lazy_loading_example_output.txt", "w") as fo:
			for i in range(1, T+1):
				if m != []:
					N=m.pop(0)
					W =m[0:N]
					W.sort()
					trips=big_weights(W, 0)
					if W != []:
						trips=small_weights(W, trips)
					del m[0:N]
					fo.write("Case #%d: %d\n" %(i, trips))
	f.close()


no_of_trips()
