def best_time(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dif = -1
    for i in range(0, len(prices)):
      for j in range(i, len(prices)):
        if dif < prices[j]-prices[i]:
          dif = prices[j]-prices[i]
    return dif