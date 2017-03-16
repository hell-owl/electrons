#-*-coding:utf8;-*-
#qpy:3
#qpy:console

class Point:#2d point
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __str__(self):
    return '(' + str(self.x) + ';' + str(self.y) + ')'

def pointdistance(p1, p2):#distance between 2 point with (x; y) coordinates
  return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

polygon = []#wire form
polygon.append(Point(0, 0))
polygon.append(Point(6, 8))
polygon.append(Point(12, 0))
#polygon.append(Point(5, 0))

totallen = 0#length of the wire
i = 0
while i < len(polygon) - 1:
  totallen += pointdistance(polygon[i], polygon[i + 1])
  i += 1
totallen += pointdistance(polygon[-1], polygon[0])

def coordtoxy(c):#getting (x; y) coordinates from on-polyline coordinate
  i = 0
  while i < len(polygon) - 1:
    c -= pointdistance(polygon[i], polygon[i + 1])
    if c <= 0:
      k = -c/ pointdistance(polygon[i], polygon[i + 1])
      x = polygon[i + 1].x + (polygon[i].x - polygon[i + 1].x) * k
      y = polygon[i + 1].y + (polygon[i].y - polygon[i + 1].y) * k
      return Point(x, y)
    i += 1
  c -= pointdistance(polygon[-1], polygon[0])  
  k = -c/ pointdistance(polygon[-1], polygon[0])
  x = polygon[0].x + (polygon[-1].x - polygon[0].x) * k
  y = polygon[0].y + (polygon[-1].y - polygon[0].y) * k
  return Point(x, y)

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
    if self.c < second.c:
      self.impuls += -1 / ((self.c - second.c) ** 2)
    else:
      self.impuls += 1 / ((self.c - second.c) ** 2)
  def move(self):#move electron
    if self.c + sign(self.impuls) > xmin and self.x + sign(self.impuls) < xmax:
      self.c += sign(self.impuls)
    elif self.impuls > 0:
      self.c = xmax
    else:
      self.c = xmin
    self.ximpuls = 0
    self.yimpuls = 0

electrons = []
electrons.append(electron(-2))
electrons.append(electron(-1))
electrons.append(electron(0))
electrons.append(electron(1))
electrons.append(electron(2))
i = 0
while i < 2000:#moving loop
  for j in electrons:
    for k in electrons:
      if k != j:
        j.force(k)
  for j in electrons:
    j.move()
  """for j in range(len(electrons)):
    print(j, electrons[j].x)"""
  i += 1
for j in range(len(electrons)):
  print(j, electrons[j].x)
