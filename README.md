# 🎡 Raspberry Pi LED Roulette Game

Welcome to the **LED Roulette Game** — part arcade, part electronics experiment, and part “why did I press the stop button too soon again?”

This is a simple Raspberry Pi game where LEDs light up in sequence, and you have to stop them exactly on the *lucky LED* to score a point. It’s not perfect yet, but it’s fun to play, and it saves your score so you can try to beat yourself later.

---

## 🛠 What You’ll Need

* A Raspberry Pi with GPIO pins (any model works)
* **10 LEDs** (with resistors \~220Ω each)
* **2 Push buttons** (one for Start, one for Stop)
* A bunch of jumper wires
* A breadboard (or a very steady hand with alligator clips)

---

## ⚡ How It Works

1. When you start the game, one LED will blink — that’s your **lucky LED**.
2. Press **Start** to begin the roulette.
3. LEDs will light up in order, like a spinning wheel.
4. Press **Stop** to halt the game — if the LED you stopped on matches the lucky LED, you score a point!
5. Your score is saved in a local file (`scores.db`) so it’s ready for next time.

---

## 🎮 How to Play

1. Connect everything according to the pin list in the code:

   ```
   Start button → GPIO 21
   Stop button  → GPIO 22
   LEDs → GPIO 26, 19, 13, 6, 5, 27, 17, 4, 3, 2
   ```
2. Run the script:

   ```bash
   python3 roulette_game.py
   ```
3. Type your name when asked — your score will be saved under that name.
4. Play as many rounds as you want — the score updates after each stop.

---

## 🐞 Known Quirks

* Sometimes the **Stop** button reacts more than once if you press it too long (needs debounce).
* The **lucky LED** is picked once per game (would be cooler to change each round).
* Score messages sometimes appear multiple times if the button bounces.
* The game works, but it’s still a bit “Version 1.0 experimental.”

---

## 🚀 Future Ideas

* Pick a new lucky LED after each round
* Add difficulty modes (faster LED cycling)
* Show top scores after each round
* Play sound effects when you win or lose
* Make it multiplayer (pass the Pi!)


## 💡 Tip

Don’t hold the Stop button down — tap it. Unless you like hearing “Your score is now 0” five times in a row.

![a8560b34-5c41-4ad4-8342-0fcbd6ab0ebd](https://github.com/user-attachments/assets/e05b15f9-8326-49ec-8477-98e1186fbef0)

