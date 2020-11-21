class Solution:
    def solution(self, scores):
        #scores.sort()
        scores = list(set(scores)) #중복 제거
        print(scores)
        
        if len(scores)>1:
            scores.remove(max(scores)) # 최대값 제거
            scores.remove(min(scores)) # 최소값 제거
        print(scores)
        print(sum(scores))
        print(len(scores))
        avg = sum(scores)/len(scores) #평균
        
        return avg
  