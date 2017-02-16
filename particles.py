xmin = -10
xmax = 10

class particle:
  def __init__(self, charge = -1, x = 0):
    self.x = x
    self.charge = charge
    self.impuls = 0
  def force(self, second):
    if self.x < second.x:
      self.impuls += -(self.charge * second.charge) / ((self.x - second.x) ** 2)
    else:
      self.impuls += (self.charge * second.charge) / ((self.x - second.x) ** 2)
  def move(self):
    self.impuls /= 2
    if self.x + self.impuls > xmin and self.x + self.impuls < xmax:
      self.x += self.impuls
    elif self.impuls > 0:
      self.x = xmax
    else:
      self.x = xmin

particles = []
"""particles.append(particle(-1, -2))
particles.append(particle(-1, -1))
particles.append(particle(-1, 0))
particles.append(particle(-1, 1))
particles.append(particle(-1, 2))"""
particles.append(particle(2, 10))
particles.append(particle(1, -10))
particles.append(particle(1, -5))
i = 0
while i < 2000:
  for j in particles:
    for k in particles:
      if k != j:
        j.force(k)
  for j in particles:
    j.move()
  for j in range(len(particles)):
    pass
    #print(j, particles[j].x)
  i += 1
for j in range(len(particles)):
  print(j, particles[j].x)
