class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def sign(n):
  if n > 0:
    return 0.1
  elif n == 0:
    return 0
  else:
    return -0.1

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
    if self.x + sign(self.impuls) > xmin and self.x + sign(self.impuls) < xmax:
      self.x += sign(self.impuls)
    elif self.impuls > 0:
      self.x = xmax
    else:
      self.x = xmin
    self.impuls = 0

electrons = []
electrons.append(electron(-2))
electrons.append(electron(-1))
electrons.append(electron(0))
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

polygon = []
