xmin = -10
xmax = 10

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def rowcrossline(p, p1, p2):
  if (p1.x - p2.x) != 0:
    k = (p1.y - p2.y) / (p1.x - p2.x)
    b = p1.y - k * p1.x
    result = (((p1.y < p.y) and (p2.y >= p.y)) or ((p2.y < p.y) and (p1.y >= p.y))) and (((p.y - b) / k) >= p.x)
  else:
    return (((p1.y < p.y) and (p2.y >= p.y)) or ((p2.y < p.y) and (p1.y >= p.y))) and (p1.x >= p.x)

def inpoly(poly, point):
  if length(poly) < 3:
    return False
  x = 0
  for i in range(0, length(poly) - 2):
    if rowcrossline(p, poly[i], poly[i + 1]):
      x = x + 1;
  if rowcrossline(p, poly[0], poly[i]):
    x = x + 1  
  return (x % 2) == 1

def perpendicular(p, p1, p2):
  if (p1.x != p2.x) and (p1.y != p2.y):
    k = (p1.y - p2.y) / (p1.x - p2.x)
    b = p1.y - k * p1.x
    k2 = -1/k
    #y = -1/k(x - x1) + y1
    #y = kx + b
    #k2(x - x1) + y1 = kx + b
    #k2x - kx = b - y1 + k2x1
    #x = (b + k2x1 - y1)/(k2 - k) ?(k2 = k if k^2 = -1)
    xr = (b + k2 * p.x - p.y) / (k2 - k)
    yr = k * xr + b
    if ((xr > p1.x and xr < p2.x) or (xr < p1.x and xr > p2.x)) and ((yr > p1.y and yr < p2.y) or (yr < p1.y and yr > p2.y)):
      return Point(xr, yr)
  elif p1.x == p2.x:
    if (p.y > p1.y and p.y < p2.y) or (p.y < p1.y and p.y > p2.y):
      return Point(p1.x, p.y)
  else:
    if (p.x > p1.x and p.x < p2.x) or (p.x < p1.x and p.x > p2.x):
      return Point(p.x, p1.y)

def crosspoint(p1, p2, p3, p4):
  k1 = (p1.y - p2.y) / (p1.x - p2.x)
  b1 = p1.y - k * p1.x

class electron:
  def __init__(self, x = 0):
    self.x = x
    self.impuls = 0
  def force(self, second):
    if self.x < second.x:
      self.impuls += -1 / ((self.x - second.x) ** 2)
    else:
      self.impuls += 1 / ((self.x - second.x) ** 2)
  def move(self):
    self.impuls /= 2
    if self.x + self.impuls > xmin and self.x + self.impuls < xmax:
      self.x += self.impuls
    elif self.impuls > 0:
      self.x = xmax
    else:
      self.x = xmin

electrons = []
electrons.append(electron(-2))
electrons.append(electron(-1))
#electrons.append(electron(0))
electrons.append(electron(1))
electrons.append(electron(2))
i = 0
while i < 2000:
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
