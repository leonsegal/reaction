from gpiozero import Button, LED
import time
from random import uniform, choice
from Adafruit_CharLCD import *
from os import system


def initialise(lcd):
    lcd.clear()
    lcd.message("Yellow to start")


def player_wins(player, lcd):
    lcd.clear()
    lcd.message(player + " wins!")


yellow_led = LED(11)
red_led = LED(10)

blue_player = Button(8, pull_up=False)
red_player = Button(7, pull_up=False)
menu_button = Button(15, pull_up=False)  # yellow
back_button = Button(14, pull_up=False)  # white

lcd = Adafruit_CharLCD()
initialise(lcd)

while True:
    if back_button.is_pressed:
        lcd.clear()
        lcd.message("Shutting down...")
        system("sudo halt")
        break

    if menu_button.is_pressed:
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
