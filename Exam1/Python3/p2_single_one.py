def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    sets = set()
    for i in nums:
      if not i in sets:
        sets.add(i)
      else:
        sets.remove(i)
    return sets.pop()