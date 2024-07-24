class Snake:
  def __init__(self, speed):
    self.speed = speed
    self.body = [[width // 2, height // 2]]
    self.direction = 'RIGHT'

  def draw(self, screen):
    for x, y in self.body:
      pygame.draw.rect(screen, green, pygame.Rect(x, y, 10, 10))  # Adjust size as needed

  def change_direction(self, direction):
    if direction == 'LEFT' and self.direction != 'RIGHT':
      self.direction = direction
    elif direction == 'RIGHT' and self.direction != 'LEFT':
      self.direction = direction
    elif direction == 'UP' and self.direction != 'DOWN':
      self.direction = direction
    elif direction == 'DOWN' and self.direction != 'UP':
      self.direction = direction

  def move(self):
    x, y = self.body[0]
    if self.direction == 'LEFT':
      x -= self.speed
    elif self.direction == 'RIGHT':
      x += self.speed
    elif self.direction == 'UP':
      y -= self.speed
    elif self.direction == 'DOWN':
      y += self.speed
    self.body.insert(0, [x, y])
    self.body.pop()  # Remove tail if not grown

  def grow(self):
    self.body.append(self.body[-1])  # Duplicate last segment
