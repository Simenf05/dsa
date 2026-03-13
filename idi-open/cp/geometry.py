"""Geometry utilities for competitive programming."""

from typing import List, Optional, Tuple

Point = Tuple[float, float]


def orient(a: Point, b: Point, c: Point) -> float:
    """Orientation test (cross product)."""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a: Point, b: Point, p: Point) -> bool:
    """Check if p is on segment ab."""
    if min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]):
        return abs(orient(a, b, p)) < 1e-9
    return False


def segment_intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    """Check if segments ab and cd intersect."""
    o1 = orient(a, b, c)
    o2 = orient(a, b, d)
    o3 = orient(c, d, a)
    o4 = orient(c, d, b)

    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    if abs(o1) < 1e-9 and on_segment(a, b, c):
        return True
    if abs(o2) < 1e-9 and on_segment(a, b, d):
        return True
    if abs(o3) < 1e-9 and on_segment(c, d, a):
        return True
    if abs(o4) < 1e-9 and on_segment(c, d, b):
        return True
    return False


def convex_hull(points: List[Point]) -> List[Point]:
    """Monotone chain convex hull (returns hull in CCW order)."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def build_half(pts: List[Point]) -> List[Point]:
        hull: List[Point] = []
        for p in pts:
            while len(hull) >= 2 and orient(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull

    lower = build_half(pts)
    upper = build_half(reversed(pts))
    return lower[:-1] + upper[:-1]


def dist2(a: Point, b: Point) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


def rotating_calipers(points: List[Point]) -> Tuple[Point, Point]:
    """Return pair of points giving the farthest pair (diameter of convex hull)."""
    hull = convex_hull(points)
    n = len(hull)
    if n <= 1:
        return (hull[0], hull[0])
    j = 1
    best = (hull[0], hull[0])
    best_d = 0.0
    for i in range(n):
        while True:
            ni = (i + 1) % n
            nj = (j + 1) % n
            if abs(orient(hull[i], hull[ni], hull[nj])) > abs(orient(hull[i], hull[ni], hull[j])):
                j = nj
            else:
                break
        d = dist2(hull[i], hull[j])
        if d > best_d:
            best_d = d
            best = (hull[i], hull[j])
    return best
