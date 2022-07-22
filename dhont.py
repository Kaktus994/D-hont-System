from itertools import chain


def same_number_of_votes_priority(census_dict, overall_votes_dict):
	"""
	return: key with priority
	"""
	temp_rev_dict = {}
	temp_dict = census_dict.copy()
	for key, value in temp_dict.items():
		temp_rev_dict.setdefault(value, set()).add(key)

	keys = list(chain.from_iterable(values for key, values in temp_rev_dict.items() if len(values) > 1)) 
	if keys:
		temp_max = overall_votes_dict[keys[0]]
		temp_key = keys[0]
		for key in keys:
			if overall_votes_dict[key] > temp_max:
				temp_max = overall_votes_dict[key]
				temp_key = key
		return temp_key

	else:
		return None


def calculate_mandates(overall_votes_dict, census_dict, mandate_dict, number_of_mandates):
	"""
	returns: mandate_dict, census_dict
	"""
	while number_of_mandates > 0:
		temp_max_same = same_number_of_votes_priority(census_dict, overall_votes_dict)
		temp_max_votes_key = max(census_dict, key=census_dict.get)

		if temp_max_same:
			"""
			if same values exist (temp_max_same is with priority) -> check if there is higher, if not take temp_max_same  
			"""
			if census_dict[temp_max_same] >= census_dict[temp_max_votes_key]:
				temp_max_votes_key = temp_max_same

		mandate_dict[temp_max_votes_key] += 1
		census_dict[temp_max_votes_key] = overall_votes_dict[temp_max_votes_key] / (1 + mandate_dict[temp_max_votes_key])
		number_of_mandates -= 1
		print(census_dict, mandate_dict)

	return mandate_dict, census_dict


"""
For testing purposes
"""
if __name__ == "__main__":
	overall_votes_dict_1 = {0:2950, 1:480, 2:1100, 3:1900}
	overall_votes_dict_2 = {0:2900, 1:400, 2:1000, 3:2000}
	overall_votes_dict = {0:10000, 1:10000}
	mandate_dict = {}
	census_dict = {}
	CENSUS = 0.03
	new_dict = overall_votes_dict.copy()
	overall_votes_sum = sum(overall_votes_dict_1.values())


	for key in overall_votes_dict_1.keys():
		if overall_votes_dict_1[key] >= overall_votes_sum*CENSUS:
			census_dict[key] = overall_votes_dict_1[key]

	for key in census_dict.keys():
		mandate_dict[key] = 0

	calculate_mandates(overall_votes_dict_1, census_dict, mandate_dict, 25)