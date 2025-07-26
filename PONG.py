import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.font.init()

win_width, win_height = 858, 525

pygame.init()
win = pygame.display.set_mode((858, 525))
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()

Deaths_left = 0
Deaths_right = 0

down, up = False, True
left, right = False, True
Paul_height, Paul_width = 5, 5
Paul_speed_y, Paul_speed_x = 2, 4
Paul = pygame.Rect(win_width / 2 - Paul_width, win_height / 2 - Paul_height, Paul_width, Paul_height)

Player_height, Player_width = 100, 10
Player_speed = 1
Left_player = pygame.Rect(25, win_height / 2, Player_width, Player_height)
Right_player = pygame.Rect(win_width - 25, win_height / 2, Player_width, Player_height)

FONT = pygame.font.SysFont("comicsans", 30)
try:
    image = pygame.image.load("cat.png")
except:
    FileNotFoundError

running = False
menu_running = False

def draw(Paul, Left_player, Right_player):
    FONT = pygame.font.SysFont("comicsans", 30)
    score_text = FONT.render(f"{Deaths_right} | {Deaths_left}", 1, "White")
    win.fill("black")

    pygame.draw.rect(win, "white", Left_player)
    pygame.draw.rect(win, "white", Right_player)
    pygame.draw.rect(win, "white", Paul)
    win.blit(score_text, (win_width / 2 - score_text.get_width() / 2, 10))

def main():
    global running, up, down, right, left, Deaths_right, Deaths_left, menu_running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
            menu_running = True

        if keys[pygame.K_w]:
            if Left_player.y > 0:
                Left_player.y -= Player_speed
        if keys[pygame.K_s]:
            if Left_player.y < win_height - Player_height:
                Left_player.y += Player_speed

        if keys[pygame.K_UP]:
            if Right_player.y > 0:
                Right_player.y -= Player_speed
        if keys[pygame.K_DOWN]:
            if Right_player.y < win_height - Player_height:
                Right_player.y += Player_speed

        #Paul movement Y
        if up:
            Paul.y -= Paul_speed_y
            if Paul.y <= 0 + Paul_height / 2:
                up = False
                down = True
        elif down:
            Paul.y += Paul_speed_y
            if Paul.y >= win_height - Paul_height:
                down = False
                up = True

        #Paul movement X
        if right:
            Paul.x += Paul_speed_x
            if Paul.x >= win_width - Paul_width or Paul.colliderect(Right_player):
                right = False
                left = True
        elif left:
            Paul.x -= Paul_speed_x
            if Paul.x <= 0 or Paul.colliderect(Left_player):
                right = True
                left = False
        
        #Death check
        if Paul.x >= win_width - Paul_width:
            Deaths_right += 1
        if Paul.x <= 0:
            Deaths_left += 1

        draw(Paul, Left_player, Right_player)
        pygame.display.update()
        clock.tick(120)

def main_menu():
    global running, menu_running
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu_running = False
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False
            menu_running = False
            pygame.quit()
            return
            
        if keys[pygame.K_SPACE]:
            menu_running = False
            running = True
            main()

        win.fill("black")
        title_text = FONT.render("PONG", 1, "white")
        start_text = FONT.render("Press SPACE to Play", 1, "white")

        win.blit(title_text, (win_width / 2 - title_text.get_width() / 2, win_height / 7))
        win.blit(start_text, (win_width / 2 - start_text.get_width() / 2, win_height / 3))
        try:
            win.blit(image, (win_width / 2 - image.get_width() / 2, 200))
        except:
            NameError
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    menu_running = True
    main_menu()