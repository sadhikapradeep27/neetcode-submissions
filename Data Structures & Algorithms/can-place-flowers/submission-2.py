class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]  # pad edges so we can safely check neighbors
        count = 0
        for i in range(1, len(bed) - 1):
            if bed[i] == 0 and bed[i - 1] == 0 and bed[i + 1] == 0:
                bed[i] = 1  # plant, so future checks see this spot as filled
                count += 1
        return count >= n