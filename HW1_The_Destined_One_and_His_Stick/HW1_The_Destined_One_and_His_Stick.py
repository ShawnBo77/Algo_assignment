class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return (abs((p1.x - p2.x)**2 + (p1.y - p2.y)**2))**(1/2)

def exhaustive_cal_min_dist(points):
    if len(points) < 2:
        return 0
    min_dist = dist(points[0], points[1])
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            if dist(points[i], points[j]) < min_dist:
                min_dist = dist(points[i], points[j])
    return min_dist

def recursive_cal_closest(points):
    if len(points) <= 3:
        return exhaustive_cal_min_dist(points)
    mid = points[len(points)//2]
    dl = recursive_cal_closest(points[:len(points)//2])
    dr = recursive_cal_closest(points[len(points)//2:])
    d = min(dl, dr)
    points_in_d = []
    for p in points:
        if abs(p.x - mid.x) < d:
            points_in_d.append(p)
    points_in_d.sort(key=lambda point: point.y)
    for i in range(len(points_in_d)-1):
        for j in range(i+1, len(points_in_d)):
            if abs(points_in_d[i].y - points_in_d[j].y) >= d:
                break
            if dist(points_in_d[i], points_in_d[j]) < d:
                d = dist(points_in_d[i], points_in_d[j])
    return d

def closest_pair_distance(points):
    points.sort(key = lambda point: point.x)
    return recursive_cal_closest(points)

num_of_case = int(input())
for i in range(num_of_case):
    num_of_p = int(input())
    points = []
    for j in range(num_of_p):
        x, y = map(float, input().split())
        points.append(Point(x, y))
    print(round(closest_pair_distance(points), 6))
