class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int) # this one checks how many of each points exists
        self.pts = [] # tracks actual points

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1 # keys are the unique points, val is the counts
        self.pts.append(point) # saves the points in list

    def count(self, point: List[int]) -> int:
        res = 0 # result that is returned
        px, py = point # point here is the target point
        for x,y in self.pts:
            if(abs(px-x) != abs(py-y)) or x == px or y == py: # check if not squares
                continue # If not squares, check others and continue
            # since points are aligned to target, px and py exists in either of points
            res += self.ptsCount[(x, py)] * self.ptsCount[(px,y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)