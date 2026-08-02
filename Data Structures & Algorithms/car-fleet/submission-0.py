class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        stack=[]

        for pos,spd in cars:
            time_required=(target-pos)/spd
            if not stack or time_required > stack[-1]:
                stack.append(time_required)
        return len(stack)