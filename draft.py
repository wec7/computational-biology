def find_longest_increasing_subsequence(ls_sequance):
	'''
	@summary: The longest increasing subsequence problem for a set of numbers 
	is to find a subsequence of a given set of numbers, in which elements are 
	in sorted order, from lowest to highest.
	@param ls_sequance: list of the original set of numbers
	@return: list of longest subsequence
	'''
	# list of list of longest subsequence for each entry
	ll_longest_subseq = []
	for i, i_number in enumerate(ls_sequance):
		# list of longest subsequence for each entry and initialization
		ls_longest_subseq = [i_number] 
		if i == 0:
			ll_longest_subseq.append(ls_longest_subseq)
		else:
			i_longest_length = 0
			for j in range(i):
				if len(ll_longest_subseq[i-j-1])>=i_longest_length \
				and ls_sequance[i-j-1]<i_number:
					ls_longest_subseq = ll_longest_subseq[i-j-1]+[i_number]
					i_longest_length = len(ls_longest_subseq)-1
			ll_longest_subseq.append(ls_longest_subseq)
	return ll_longest_subseq[-1]

print find_longest_increasing_subsequence([9,5,8,7,15])
# the return result is 5, 8, 15