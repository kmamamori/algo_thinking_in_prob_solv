def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
      return 1
    if n == 2:
      return 2
    if n == 3:
      return 3
    return climb_stairs(n-1) + climb_stairs(n-2)
    
    