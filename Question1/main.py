import numpy as np
from scipy.spatial import ConvexHull
import math
from scipy.ndimage.interpolation import rotate
def smallest_rect(points):
  pi2 = np.pi / 2.
  hull_points = points[ConvexHull(points).vertices]
  edges = np.zeros((len(hull_points) - 1, 2))
  edges = hull_points[1:] - hull_points[:-1]
  angles = np.zeros((len(edges)))
  angles = np.arctan2(edges[:, 1], edges[:, 0])
  angles = np.abs(np.mod(angles, pi2))
  angles = np.unique(angles)
  rotations = np.vstack([
      np.cos(angles),
      np.cos(angles - pi2),
      np.cos(angles + pi2),
      np.cos(angles)
  ]).T
  rotations = rotations.reshape((-1, 2, 2))
  rot_points = np.dot(rotations, hull_points.T)
  min_x = np.nanmin(rot_points[:, 0], axis=1)
  max_x = np.nanmax(rot_points[:, 0], axis=1)
  min_y = np.nanmin(rot_points[:, 1], axis=1)
  max_y = np.nanmax(rot_points[:, 1], axis=1)
  areas = (max_x - min_x) * (max_y - min_y)
  best_idx = np.argmin(areas)
  x1, x2, y1, y2 = max_x[best_idx], min_x[best_idx], max_y[best_idx], min_y[best_idx]
  r = rotations[best_idx]
  rval = np.zeros((4, 2))
  rval[0], rval[1], rval[2], rval[3] = np.dot([x1, y2], r), np.dot([x2, y2], r), np.dot([x2, y1], r), np.dot([x1, y1], r)
  return rval
prepoints = []
with open("input.in") as input_file:
  filecontent = input_file.read().split('\n')
  filecontent.pop(0)
  for elm in filecontent:
    oklist = elm.split(" ")
    prepoints.append([int(oklist[0]), int(oklist[1])])
  filecontent.pop(-1)

points = np.array(prepoints)
dabox = smallest_rect(points)
pointlist = dabox.tolist()
area = round(
    math.dist(pointlist[0], pointlist[1]) *
    math.dist(pointlist[1], pointlist[2]))

Ysmallesty = []
Xsmallesty = []
for counter in range(0, 2):
  smallesty = 1000
  coorX = 0
  num = 0
  remnum = 0
  for elm in pointlist:
    if elm[1] < smallesty:
      smallesty = elm[1]
      coorX = elm[0]
      remnum = num
    num += 1
  Xsmallesty.append((coorX))
  Ysmallesty.append((smallesty))
  pointlist.pop(remnum)
c1 = [Xsmallesty[0], Ysmallesty[0]]
c2 = [Xsmallesty[1], Ysmallesty[1]]
a = abs(c1[1] - c2[1])
b = abs(c1[0] - c2[0])
finalangle = ((np.arctan(a / b)) * 180) / np.pi
with open("ouput.out", "w") as out_file:
  out_file.write(str(area) + " " + str(round(finalangle, 2)))
