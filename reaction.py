import time
from random import uniform, choice

from gpiozero import Button, LED

from Adafruit_CharLCD import *


def initialise(the_lcd):
    the_lcd.clear()
    the_lcd.message("Press a button")


def player_wins(player, the_lcd):
    the_lcd.clear()
    the_lcd.message(player + " wins!")


yellow_led = LED(11)
red_led = LED(10)

blue_player = Button(8, pull_up=False)
red_player = Button(7, pull_up=False)

lcd = Adafruit_CharLCD()
initialise(lcd)


def is_led_on():
    return dir().count('selected_led') == 1


while True:
    if not is_led_on() and (red_player.is_pressed or blue_player.is_pressed):
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
