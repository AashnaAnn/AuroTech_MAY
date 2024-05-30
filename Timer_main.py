import pygame
import sys
from button import Button
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer")

CLOCK = pygame.time.Clock()

BACKDROP = pygame.image.load("images/backdrop.png")
WHITE_BUTTON = pygame.image.load("images/button.png")

CLOCK_FONT_SIZE = 120
FONT = pygame.font.Font("images/ArialRoundedMTBold.ttf", CLOCK_FONT_SIZE)
timer_text = FONT.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2-25))

START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
                    pygame.font.Font("images/ArialRoundedMTBold.ttf", 20), "#000000", "#00008B")
POMODORO_BUTTON = Button(None, (WIDTH/2-150, HEIGHT/2-140), 120, 30, "Pomodoro", 
                    pygame.font.Font("images/ArialRoundedMTBold.ttf", 20), "#000000", "#00008B")
SHORT_BREAK_BUTTON = Button(None, (WIDTH/2, HEIGHT/2-140), 120, 30, "Short Break", 
                    pygame.font.Font("images/ArialRoundedMTBold.ttf", 20), "#000000", "#00008B")
LONG_BREAK_BUTTON = Button(None, (WIDTH/2+150, HEIGHT/2-140), 120, 30, "Long Break", 
                    pygame.font.Font("images/ArialRoundedMTBold.ttf", 20), "#000000", "#00008B")
CLOCK_BUTTON = Button(None, (WIDTH/2, HEIGHT/2-190), 120, 30, "Clock", 
                    pygame.font.Font("images/ArialRoundedMTBold.ttf", 20), "#000000", "#00008B")

POMODORO_LENGTH = 3000 #  50 mins
SHORT_BREAK_LENGTH = 300 #  5 mins
LONG_BREAK_LENGTH = 900 # 15 mins

current_seconds = POMODORO_LENGTH
mode = "pomodoro"
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                if started:
                    started = False
                else:
                    started = True
            if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = POMODORO_LENGTH
                mode = "pomodoro"
                started = False
            if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = SHORT_BREAK_LENGTH
                mode = "short_break"
                started = False
            if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = LONG_BREAK_LENGTH
                mode = "long_break"
                started = False
            if CLOCK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                mode = "clock"
                started = False
            if started:
                START_STOP_BUTTON.text_input = "STOP"
                START_STOP_BUTTON.text = pygame.font.Font("images/ArialRoundedMTBold.ttf", 20).render(
                                        START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
            else:
                START_STOP_BUTTON.text_input = "START"
                START_STOP_BUTTON.text = pygame.font.Font("images/ArialRoundedMTBold.ttf", 20).render(
                                        START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
        if event.type == pygame.USEREVENT and started and mode != "clock":
            current_seconds -= 1

    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))

    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    CLOCK_BUTTON.update(SCREEN)
    CLOCK_BUTTON.change_color(pygame.mouse.get_pos())

    if mode == "clock":
        current_time = datetime.now()
        clock_font_size = min(WIDTH // 6, HEIGHT // 4)  # Adjust font size based on window size
        clock_font = pygame.font.Font("images/ArialRoundedMTBold.ttf", clock_font_size)
        clock_text = clock_font.render(f"{current_time.hour:02}:{current_time.minute:02}:{current_time.second:02}", True, "white")
        clock_text_rect = clock_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(clock_text, clock_text_rect)
    elif current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
        timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
        SCREEN.blit(timer_text, timer_text_rect)
    pygame.display.update()