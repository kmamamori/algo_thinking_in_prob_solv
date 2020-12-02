def house_robber(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  
  S1 = nums[0]
  S2 = nums[1] if S1 < nums[1] else S1
  for w in nums[2:]:
    if S2 > S1+w: S1 = S2
    else: S1, S2 = S2, S1+w
  return S2
 