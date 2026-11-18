class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=float(inf)
        d={}
        instant='balloon'
        for i in instant:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        d1={}
        for i in text:
            if i in d1.keys():
                d1[i]+=1
            else:
                d1[i]=1
        for i in d:
            count=min(count,d1.get(i,0)//d[i])
        return count
