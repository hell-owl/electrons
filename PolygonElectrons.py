#-*-coding:utf8;-*-
#qpy:3
#qpy:console

class Point:#2d point
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __str__(self):
    return '(' + str(self.x) + ';' + str(self.y) + ')'

def distance(p1, p2):#distance between 2 point with (x; y) coordinates
  return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

polygon = []#wire form
polygon.append(Point(0, 0))
polygon.append(Point(6, 8))
polygon.append(Point(12, 0))
polygon.append(Point(6, -8))
"""polygon.append(Point(0, 0))
polygon.append(Point(5,0))"""

totallen = 0#length of the wire
i = 0
while i < len(polygon) - 1:
  totallen += distance(polygon[i], polygon[i + 1])
  i += 1
totallen += distance(polygon[-1], polygon[0])

def coordtoxy(c):#getting (x; y) coordinates from on-polyline coordinate
  i = 0
  while i < len(polygon) - 1:
    c -= distance(polygon[i], polygon[i + 1])
    if c <= 0:
      k = -c/ distance(polygon[i], polygon[i + 1])
      x = polygon[i + 1].x + (polygon[i].x - polygon[i + 1].x) * k
      y = polygon[i + 1].y + (polygon[i].y - polygon[i + 1].y) * k
      return Point(x, y)
    i += 1
  c -= distance(polygon[-1], polygon[0])  
  k = -c/ distance(polygon[-1], polygon[0])
  x = polygon[0].x + (polygon[-1].x - polygon[0].x) * k
  y = polygon[0].y + (polygon[-1].y - polygon[0].y) * k
  return Point(x, y)

def whatline(c):#getting (x; y) coordinates from on-polyline coordinate
  i = 0
  while i < len(polygon) - 1:
    c -= distance(polygon[i], polygon[i + 1])
    if c < 0:
      return i
    i += 1
  return len(polygon) - 1

def sign(n):#sign of number * 0.1
  if n > 0:
    return 0.1
  elif n == 0:
    return 0
  else:
    return -0.1

class electron:#electron: can be moved by electro-force
  def __init__(self, c = 0):
    self.c = c
    self.ximpuls = 0
    self.yimpuls = 0
  def force(self, second):#calculaste 1 force and add it's value to sum of forces
    x1 = coordtoxy(self.c).x
    y1 = coordtoxy(self.c).y
    x2 = coordtoxy(second.c).x
    y2 = coordtoxy(second.c).y
    self.ximpuls += (x1 - x2) / (distance(Point(x1, y1), Point(x2, y2)) ** 3)
    self.yimpuls += (y1 - y2) / (distance(Point(x1, y1), Point(x2, y2)) ** 3)
  def move(self):#move electron
    p = polygon[whatline(self.c)]
    s = coordtoxy(self.c)#if electron on a polygon node, then (s.x - p.x) = (s.y - p.y) = 0 => (v1*v2) = 0 => electron does not move
    if s.x == p.x:
      p = polygon[(whatline(self.c) - 1) % len(polygon)]
      #print('wl', (whatline(self.c) - 1) % len(polygon))
      #print(sign((s.x - p.x) * self.ximpuls + (s.y - p.y) * self.yimpuls))
      #raise Exception()
    self.c += sign((s.x - p.x) * self.ximpuls + (s.y - p.y) * self.yimpuls)
    if self.c < 0:
      self.c = totallen + self.c
    if self.c >= totallen:
      self.c -= totallen
    self.ximpuls = 0
    self.yimpuls = 0

electrons = []
electrons.append(electron(0))
electrons.append(electron(2))
electrons.append(electron(3))
electrons.append(electron(39))
i = 0
while i < 200:#moving loop
  for j in electrons:
    for k in electrons:
      if k != j:
        j.force(k)
  #print(electrons[0].ximpuls, electrons[0].yimpuls)
  #print(electrons[1].ximpuls, electrons[1].yimpuls)
  for j in electrons:
    j.move()
  """for j in range(len(electrons)):
    print(j, ':', electrons[j].c)"""
  i += 1
for j in range(len(electrons)):
  print(j, ':', electrons[j].c)
print(totallen)
