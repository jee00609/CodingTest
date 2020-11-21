class Solution:
    def solution(self, scores):
        scores.sort()
        arr=[]
        if len(scores)==1:
            return scores[0]
        if len(scores)%2==0:
            for k in range(0,int(len(scores)/2)):
                count=0
                for j in range(k,len(scores)-k):
                    count+=scores[j]
                count/=(len(scores)-(2*k))
                arr.append(count)
                
            return max(arr)    
                
        if len(scores)%2==1:
            for k in range(0,int(len(scores)/2)+1):
                count=0
                for j in range(k,len(scores)-k):
                    count+=scores[j]
                count/=(len(scores)-(2*k))
                arr.append(count)
                
            return max(arr)
        
