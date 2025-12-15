def combine_lists(list1, list2):
	combined = []

	for item in list1 + list2:
		if not isinstance(item, int):
			raise TypeError("All elemtents must be integers")
		if item not in combined:
			combined.append(item)

	for i in range (len(combined)):
		max_index = 1
		for j in range(i + 1, len(combined)):
			if combined[j] > combined[max_index]:
				max_indez = j
		combined[i], combined[max_index] = combined[max_index], combined[i]

	return combined
