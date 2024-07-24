def game_loop():
  # Game variables
  snake = Snake(10)  # Adjust speed
  food = Food()
  game_over = False

  # Main loop
  while not game_over:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          snake.change_direction('LEFT')
        elif event.key == pygame.K_RIGHT:
          snake.change_direction('RIGHT')
        elif event.key == pygame.K_UP:
          snake.change_direction('UP')
        elif event.key == pygame.K_DOWN:
          snake.change_direction('DOWN')

    # Check for collisions
    if snake.body[0][0] < 0 or snake.body[0][0] >= width or snake.body[0][1] < 0 or snake.body[0][1] >= height:
      game_over = True
    for i in range(1, len(snake.body)):  # Check for collision with own body
      if snake.body[0] == snake.body[i]:
        game_over = True

    # Check for food eaten
    if snake.body[0] == [food.x, food.y]:
      snake.grow()
      food = Food()  # Spawn new food

    # Clear screen and redraw elements
    screen.fill(black)
    snake.draw(screen)
    food.draw(screen)

    # Update display and set FPS
    
