import pygame
from settings import *
from map import ALL_MAZES as maze
from runner import Runner

def build_rects(maze):
    WALL, START, END = [],[],[]
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            cell = maze[row][col]
            rect = pygame.Rect(col * WALL_SIZE, row * WALL_SIZE, WALL_SIZE, WALL_SIZE)
            if cell == "M":
                WALL.append(rect)
            elif cell == "S":
                START.append(rect)
            elif cell == "E":
                END.append(rect)
    return WALL, START, END

def get_start_pos(START):
    if START:
        return START[0].x, START[0].y
    return 0, 0

def get_end_pos(END):
    if END:
        return END[0].x, END[0].y
    return 0, 0

def play_level(screen, clock, maze):
    WALL, START, END = build_rects(maze)
    START_X, START_Y = get_start_pos(START)
    END_X, END_Y = get_end_pos(END)
    runner = Runner(START_X,START_Y,RUNNER_COLOR,RUNNER_SIZE, RUNNER_SPEED)
    running = True
    while running:
        screen.fill(BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            runner.handle_event(event)
        runner.move(WALL)

        for wall in WALL:
            pygame.draw.rect(screen, BRICK_COLOR, wall)
        for start in START:
            pygame.draw.rect(screen, END_START_COLOR, start)
        for end in END:
            pygame.draw.rect(screen, END_START_COLOR, end)
        
        runner.draw(screen)

        if runner.x == END_X and runner.y == END_Y:
            return True
        
        pygame.display.flip()
        clock.tick(FPS)
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("MAZE RUNNER 1")
    clock = pygame.time.Clock()

    for LEVEL_NUM, MAZE in enumerate(maze,1):
        COMPLETED = play_level(screen, clock, MAZE)
        if not COMPLETED:
            print("Game Exited.")
            break
        print(f"Level {LEVEL_NUM} Completed!")
    else:
        print("All Levels Completed!")
    pygame.quit()

if __name__ == "__main__":
    main()


