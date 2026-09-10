def canShip(weights,days_have,capacity):
    #find the days needed to ship all the weights under choosen capacity
    days_needed=1
    cweightSum=0
    for w in weights:
        if cweightSum+w<=capacity:
            cweightSum+=w
        else:
            days_needed+=1
            cweightSum=w
    return days_needed<=days_have
    #compare days_needed <= days_have (capacity is a valid choice)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
          low=max(weights)
          high=sum(weights)
          while low<high:
            mid=(low+high)//2
            if canShip(weights,days,mid):
                high=mid
            else:
                low=mid+1
          return low