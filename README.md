# Asteroids (Python / Pygame)

A modern Python recreation of the classic **Asteroids** arcade game, built using **Pygame**.  
This project focuses on clean game architecture, responsive controls, and classic arcade mechanics with a few quality-of-life improvements.

---

## Features

- **Player Movement & Acceleration**
  - Smooth thrust-based movement
  - Acceleration and deceleration handling
  - Fixed shooting behavior while accelerating

- **Shooting System**
  - Projectile-based shooting
  - Shooting cooldown to prevent spam
  - Reliable firing direction tied to player rotation

- **Asteroids**
  - Randomly spawned asteroids
  - Asteroid destruction on impact
  - Asteroid splitting into smaller pieces when destroyed

- **Screen Wrapping**
  - Player wraps around screen edges
  - Asteroids and projectiles respect screen boundaries

- **Scoring System**
  - Score increases when destroying asteroids
  - Score tracked and displayed during gameplay

- **Lives System**
  - Player starts with a limited number of lives
  - Lives decrease on collision with asteroids

- **Stamina System**
  - Stamina limits continuous actions
  - Regeneration over time

- **Visuals**
  - Background image added for improved presentation
  - Clean, minimal arcade-style visuals

---

## Controls

| Action       | Key |
|--------------|-----|
| Rotate Left  | A |
| Rotate Right | D |
| Forward      | W |
| Shoot        | Space |
| Accelerate   | L-Shift |

---

## Requirements

- Python 3.10+
- Pygame

Install dependencies:

```bash
pip install pygame
```

git clone https://github.com/ethanewl/asteroids.git
cd asteroids
python main.py

