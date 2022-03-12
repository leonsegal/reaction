import time
from random import uniform, choice
from gpiozero import Button, LED
from Adafruit_CharLCD import *
from os import system


def show_menu(counter):
    lcd.clear()
    lcd.message(menu_items[counter] + ": \nYellow to select")


def tennis():
    leading_spaces = 0
    asc = True
    while True:
        if asc == True:
            leading_spaces += 1
            if leading_spaces == 15:
                asc = False
        else:
            leading_spaces -= 1
            if leading_spaces == 0:
                asc = True

        sleep(0.03)
        lcd.clear()
        lcd.message((" " * leading_spaces) + "*\n")


def reaction():
    while True:
        if red_player.is_pressed or blue_player.is_pressed:
            lcd.clear()
            lcd.message("Get ready...")
            delay = uniform(2, 3)
            time.sleep(delay)

            selected_led = choice([red_led, yellow_led])
            if selected_led == red_led:
                delay = 3
                close_time = time.time() + delay
                if time.time() > close_time:
                    initialise(lcd)

            selected_led.on()

            lcd.clear()
            lcd.message("Go!")

        if blue_player.is_pressed:
            if selected_led == yellow_led:
                player_wins("Blue", lcd)
            else:
                player_wins("Red", lcd)
            selected_led.off()
            time.sleep(3)
            initialise(lcd)
        if red_player.is_pressed:
            if selected_led == yellow_led:
                player_wins("Red", lcd)
            else:
                player_wins("Blue", lcd)
            selected_led.off()
            time.sleep(3)
            initialise(lcd)


def golf():
    lcd.clear()
    lcd.message("golf")


def shut_down():
    system("sudo halt")


def player_wins(player, the_lcd):
    the_lcd.clear()
    the_lcd.message(player + " wins!")


# Output items
yellow_led = LED(11)
red_led = LED(10)
lcd = Adafruit_CharLCD()

# Input items
blue_player = Button(8, pull_up=False)
red_player = Button(7, pull_up=False)
menu_button = Button(10, pull_up=False)
select_button = Button(11, pull_up=False)

# Game items
red_score = 0
blue_score = 0
menu_items = [
    "Tennis",
    "Reaction",
    "Golf",
    "Shut Down",
]
menu_counter = 0
is_playing_game = False

show_menu(menu_counter)
