import math
fullcircle = math.radians(360)
radius = 7

def sign(n):
  if n > 0:
    return 0.01
  elif n == 0:
    return 0
  else:
    return -0.01

class electron:
  def __init__(self, x = 0):
    self.x = x
    self.impuls = 0
  def distance(self, second):
    return math.sqrt(2) * radius * math.sqrt(1 - math.cos(self.x - second.x))
  def force(self, second):
    if (second.x - self.x) % fullcircle > fullcircle / 2:
      #print('force', -1 / (self.distance(second) ** 2))
      self.impuls += -1 / (self.distance(second) ** 2) * math.cos((second.x - self.x) % (fullcircle / 2) / 2)
    else:
      #print('force', 1 / (self.distance(second) ** 2))
      self.impuls += 1 / (self.distance(second) ** 2) * math.cos((second.x - self.x) % (fullcircle / 2) / 2)
  def move(self):
    self.x -= sign(self.impuls)
    self.x = self.x % fullcircle
    self.impuls = 0

electrons = []
electrons.append(electron(0))
electrons.append(electron(1))
electrons.append(electron(2))
#electrons.append(electron(3))
#electrons.append(electron(4))
#electrons.append(electron(5))
i = 0
while i < 10000:
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
  print(j, math.degrees(electrons[j].x))
