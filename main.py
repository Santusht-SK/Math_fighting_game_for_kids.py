import pygame
import random
# import math
import time

# Initializes the pygame
pygame.init()

# creates the display size of the game (1200pixels by 800pixels) stores in the variable screen
screen = pygame.display.set_mode((1200, 800))

# Creating a title and icon
pygame.display.set_caption("Addition District")  # renames the name of the game
background = pygame.image.load("background.jpg")


def start():
    global player_health
    global battle_points
    global enemy_health
    player_health = 20
    battle_points = 0
    enemy_health = 15
    main()

def main():
    global player_health
    global battle_points
    global enemy_health
    font = pygame.font.Font("freesansbold.ttf", 40)
    question_font = pygame.font.Font("freesansbold.ttf", 60)


    x = random.randint(0, 10)
    y = random.randint(0, 10)
    answer = x + y

    my_answer = ""
    my_answer_X = 567
    my_answer_Y = 300
    question_text_X = 500
    question_text_Y = 200
    game_not_over = True
    time_sec = 5
    counter = 0
    time_list = []

    def ability_rules():
        game_over_text = font.render(" 2 BP does 2 dmg (press z)", True, (150, 150, 150))
        screen.blit(game_over_text, (40, 50))
        game_over_text = font.render("4 BP does 5 dmg (press x)", True, (150, 150, 150))
        screen.blit(game_over_text, (50, 100))
        game_over_text = font.render("10 BP does 15 dmg (press c)", True, (150, 150, 150))
        screen.blit(game_over_text, (50, 150))





# text functions (questions and answers)
    def question_text(a, b):
        if player_health > 0 and enemy_health > 0:
            game_over_text = question_font.render(str(x) + " + " + str(y), True, (255, 255, 255))
            screen.blit(game_over_text, (a, b))

    def my_answer_text(x, y):
        game_over_text = font.render(str(my_answer), True, (255, 255, 255))
        screen.blit(game_over_text, (x, y))




# health functions
    def player_HP():
        game_over_text = font.render("Player HP: " + str(player_health), True, (150, 255, 255))
        screen.blit(game_over_text, (50, 700))

    def enemy_HP():
        game_over_text = font.render("Enemy HP: " + str(enemy_health), True, (255, 50, 100))
        screen.blit(game_over_text, (900, 700))




# Battle points function
    def battle_point_func():
        game_over_text = font.render("Battle Points: " + str(battle_points), True, (150, 255, 255))
        screen.blit(game_over_text, (50, 600))

    def timer():
        game_over_text = font.render(str(time_sec), True, (255, 255, 255))
        screen.blit(game_over_text, (1000, 50))







# statement win/lose functions
    def you_win():
        you_win_text = font.render("You Won! Press Return to restart", True, (255, 255, 255))
        screen.blit(you_win_text, (300, 300))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start()


    def wrong_answer():
        game_over_text = font.render("Wrong Answer, Press Return to restart", True, (255, 255, 255))
        screen.blit(game_over_text, (100, 500))

    def you_lose():
        game_over_text = font.render("Game Over, Press Return to restart", True, (255, 255, 255))
        screen.blit(game_over_text, (250, 300))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start()

    def you_lose_timer():
        game_over_text = font.render("Game Over, Press Return to restart", True, (255, 255, 255))
        screen.blit(game_over_text, (250, 300))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start()

    running = True
    while running:
        print(int(time.time()))
        # function for timer
        begin = int(time.time()) # remove milliseconds
        time_list.append(begin) # append the current time to a list

        counter += 1
        if counter > 1:
            if time_list[0] == time_list[1]: # if the time in the list is the same (a second has not passed yet)
                time_list.pop(0) # remove the first item from the list (this allows us to keep comparing the next 2 timers to see if a second passed)

            elif time_list[0] != time_list[1] and game_not_over is True: # if the the items in the list do not match each other, that means a second has passed
                time_sec -= 1 #the visual timer  decreases by 1
                time_list.pop(0) # remove the first timer in the list (allows to compare the next two timers and repeat the process)


        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            # pygame.QUIT is the close button (x at the top right) If it is pressed, the window closes and the while loop is terminated (running = False)
            if event.type == pygame.QUIT:
                pygame, quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key).isnumeric() is True and player_health > 0 and enemy_health > 0:
                    my_answer += pygame.key.name(event.key)
                    my_answer_X -= 10.5 # shift the answer a bit to the left so that the answer is always centered

                if event.key == pygame.K_BACKSPACE and player_health > 0 and enemy_health > 0:
                    my_answer = my_answer[:-1] # [-1] is not inclusive (new length is up to the second last character (removes the first))
                    my_answer_X += 10.5 # shift the answer a bit to the right so that the answer is always centered

                if event.key == pygame.K_RETURN and game_not_over is True:
                    if str(answer) == my_answer:
                        battle_points += time_sec # add remaining time as battle points
                        time_sec = 5
                        main()

                    elif str(answer) != my_answer:
                        wrong_answer()
                        player_health -= 3
                        main()


                # abilities
                if battle_points >= 2 and event.key == pygame.K_z:
                    battle_points -= 2
                    enemy_health -= 2

                elif battle_points >= 4 and event.key == pygame.K_x:
                    battle_points -= 4
                    enemy_health -= 5

                elif battle_points >= 10 and event.key == pygame.K_c:
                    battle_points -= 10
                    enemy_health -= 15



            if player_health <= 0:
                game_not_over = False
                player_health = 0

            elif enemy_health <= 0:
                game_not_over = False
                enemy_health = 0






        # mainly text functions and the you_lose function

        if game_not_over is False and player_health <= 0:
            player_health = 0
            you_lose()
        elif game_not_over is False and enemy_health <= 0:
            enemy_health = 0
            you_win()

        if time_sec == 0 and game_not_over is True:
            player_health -= 3
            main()
        if player_health <= 0:
            time_sec = 5
            player_health = 0
            you_lose_timer()



        # function calling
        player_HP()
        enemy_HP()

        ability_rules()
        battle_point_func()

        question_text(question_text_X, question_text_Y)
        my_answer_text(my_answer_X, my_answer_Y)

        timer()

        pygame.display.update()


start()
