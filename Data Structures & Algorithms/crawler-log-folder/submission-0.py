class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for each in logs:
            if each not in ["../","./"]:
                stack.append(each)
            elif each =="../" and stack:
                stack.pop()
        return len(stack)
                