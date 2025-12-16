def combine_lists(list1, list2):

	for item in list1 + list2:
		if not isinstance(item, int):
			raise TypeError("All elemtents must be integers")

	combined = list(set(list1 + list2))

	for i in range (len(combined)):
		max_index = i
		for j in range(i + 1, len(combined)):
			if combined[j] > combined[max_index]:
				max_index = j
		combined[i], combined[max_index] = combined[max_index], combined[i]

	return combined
