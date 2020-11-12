def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict = {}
    for i in nums:
      if not i in dict:
        dict[i] = 1
      else:
        dict[i] += 1
    maxkey = 0
    maxvalue = 0
    for k in dict:
      if dict[k] > maxvalue:
        maxvalue = dict[k]
        maxkey = k
    return maxkey
