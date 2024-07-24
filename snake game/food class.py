class Food:
  def __init__(self):
    self.x = random.randint(0, width - 10)
    self.y = random.randint(0, height - 10)

  def draw(self, screen):
    pygame.draw.rect(screen, red, pygame.Rect(self.x, self.y, 10, 10))
