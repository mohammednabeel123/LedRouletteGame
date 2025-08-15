from gpiozero import Button, PWMLED
import time
import random
import shelve

startButton = Button(21, pull_up=True)
stopButton = Button(22, pull_up=True)

led_pins = [26, 19, 13, 6, 5, 27, 17, 4, 3, 2]
LEDs = [PWMLED(pin) for pin in led_pins]

running = False
current_led = None
round_done = False

username = input("Enter your name: ").strip()

# create score
with shelve.open("scores.db") as db:
    if username not in db:
        db[username] = 0
    print(f"Welcome {username}! Current score: {db[username]}")

# Pick a lucky LED
def pick_lucky_led():
    led = random.choice(LEDs)
    print("Lucky LED is:", led.pin)
    led.on()
    time.sleep(1)
    led.off()
    return led

lucky_led = pick_lucky_led()

def start_roulette():
    global running, round_done
    running = True
    round_done = False
    print("Roulette started!")

def stop_roulette():
    global running, round_done, lucky_led
    if round_done:
        return  # prevent multiple scoring in same round

    running = False
    round_done = True
    if current_led:
        print(f"Stopped at LED: {current_led.pin}")
        with shelve.open("scores.db", writeback=True) as db:
            if current_led.pin == lucky_led.pin:
                print("✅ Good, you got the right LED!")
                db[username] += 1
            else:
                print("❌ Wrong LED.")
            print(f"Your score is now: {db[username]}")
    # Pick a new lucky LED for the next round
    lucky_led = pick_lucky_led()

startButton.when_pressed = start_roulette
stopButton.when_released = stop_roulette

while True:
    if running:
        for led in LEDs:
            if not running:
                break
            current_led = led
            led.on()
            time.sleep(0.05)
            led.off()
    else:
        time.sleep(0.1)
