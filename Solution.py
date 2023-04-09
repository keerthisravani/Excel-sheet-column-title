class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        map={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,  "N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
        n=len(columnTitle)-1
        i=0
        result=0
        while n>=0:
            result=result+(map[columnTitle[n]]*(26**i))
            n-=1
            i+=1
        return result
        
strs="AB"
obj=Solution()
print(obj.titleToNumber(strs))
        