import pygame

class Runner:
    def __init__(self,x,y,color,size,speed):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        self.x_change = 0
        self.y_change = 0
    
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.x_change = self.speed
            elif event.key == pygame.K_LEFT:
                self.x_change = -self.speed
            elif event.key == pygame.K_UP:
                self.y_change = -self.speed
            elif event.key == pygame.K_DOWN:
                self.y_change = self.speed
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                self.x_change = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                self.y_change = 0
    
    def move(self, walls):
        # X direction
        new_x = self.x + self.x_change
        new_rect_x = pygame.Rect(new_x, self.y, self.size, self.size)
        if not any(new_rect_x.colliderect(wall) for wall in walls):
            self.x = new_x
        # Y direction
        new_y = self.y + self.y_change
        new_rect_y = pygame.Rect(self.x, new_y, self.size, self.size)
        if not any(new_rect_y.colliderect(wall) for wall in walls):
            self.y = new_y

    def draw(self,screen):
        pygame.draw.rect(screen, self.color,self.rect)
    
    