# 같이 동봉한 입력값을 넣을 시 정답과 결과값이 다른 것을 알 수 있다.

class Solution:
    def solution(self, scores):
        #scores.sort()
        scores = list(set(scores)) #중복 제거
        print(scores)
        
        if len(scores)>1:
            scores.remove(max(scores)) # 최대값 제거
            scores.remove(min(scores)) # 최소값 제거
            
        avg = sum(scores)/len(scores) #평균
        
        return avg
  
