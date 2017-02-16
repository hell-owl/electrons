import math
fullcircle = math.radians(360)
radius = 7

class electron:
  def __init__(self, x = 0):
    self.x = x
    self.impuls = 0
  def distance(self, second):
    return math.sqrt(2) * radius * math.sqrt(1 - math.cos(self.x - second.x))
  def force(self, second):
    if (second.x - self.x) % 360 > fullcircle / 2:
      #print('force', -1 / (self.distance(second) ** 2))
      self.impuls += -1 / (self.distance(second) ** 2)
    else:
      #print('force', 1 / (self.distance(second) ** 2))
      self.impuls += 1 / (self.distance(second) ** 2)
  def move(self):
    self.impuls /= 2
    self.x += self.impuls
    self.x = self.x % fullcircle

electrons = []
electrons.append(electron(0))
electrons.append(electron(math.pi * 2/3))
electrons.append(electron(math.pi * 4/3))
i = 0
while i < 20000:
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
