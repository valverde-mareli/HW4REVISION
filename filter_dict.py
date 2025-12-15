
def filter_young(people):
	result = []

	for name in people:
		age, phone = people[name]
		if age < 30:
			result.append((name, phone))

	for i in range(len(result)):
		min_index = i
		for j in range(i + 1, len(result)):
			if result[j][0] < result[min_index][0]:
				min_index = j
		result[i], result[min_index] = result[min_index], result[i]

	return result

