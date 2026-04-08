# Design a hit counter that counts the number of hits received in the past 5 minutes (300 seconds).

class HitCounter:
    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300


    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            # same timestamp just increment
            self.hits[idx] +=1


    def get_hits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            # Only count hits within last 300 seconds
            if timestamp - self.times[i] <300:
                total += self.hits[i]
        return total           
    
if __name__ == "__main__":
    counter = HitCounter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    print(counter.get_hits(4))  #counts hits in [1,4] → 3 Output: 3
    print(counter.get_hits(300))  # counts hits in [1,300] → 3 Output: 3
    print(counter.get_hits(301))  # counts hits in [2,301] → 3 (hit at timestamp 1 is now too old) Output: 2
# -HitCounter()
#   Initializes the object.
# -void hit(int timestamp)
#   Records a hit at the given timestamp (in seconds).
#   Multiple hits can occur at the same timestamp.
# -int getHits(int timestamp)
#   Returns the number of hits in the past 300 seconds from the given timestamp.
#   That is, count hits in the interval:

# Complexity
# hit() → O(1)
# getHits() → O(300) ≈ O(1)