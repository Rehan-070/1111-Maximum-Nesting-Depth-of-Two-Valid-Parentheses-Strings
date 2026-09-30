# class Solution:
#     def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        # depth=0
        # ans=[]
        # for i in seq:
            
        #     if i=='(':
        #         depth+=1
        #         ans.append(depth%2)
        #     else:
        #         depth-=1
        #         ans.append(depth%2)
        # return ans

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []

        for i in range(len(seq)):
            res.append((i ^ ord(seq[i])) & 1)

        return res





            

            
            


          
