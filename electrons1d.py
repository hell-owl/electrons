xmin = -10
xmax = 10

class electron:
  def __init__(self, x = 0):
    self.x = x
    self.impuls = 0
  def distance(self, second):
    return self.x - second.x
  def force(self, second):
    if self.x < second.x:
      self.impuls += -1 / (self.distance(second) ** 2)
    else:
      self.impuls += 1 / (self.distance(second) ** 2)
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
