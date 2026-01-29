# TinyDormLifeSim_py
A small Python simulation game where you manage a group of people living together (dorm or family vibes) and try to keep everyone alive, sane, and not broke over a fixed number of days
The game focuses on resource management, random events, and decision balancing between money, energy, and happiness.

Gameplay Overview
- 3–5 characters living together
- Around 3 job types to earn money
- Simulation runs for 5–30 days (configurable)
- Each day, characters perform actions that affect their stats

Your goal is simple: Survive all days without anyone collapsing mentally or financially.

Character Stats
Each character has the following attributes:
- Money: shared resource for the whole group
- Energy: needed to work or perform actions
- Happiness: affects overall stability

Stats are capped at 100 to prevent infinite stacking.

Actions & Mechanics
- Work
- Earns money
- Costs energy
- May reduce happiness if overused

Entertainment (Random Event)
- Costs -10 to -15 money
- Restores +10 energy
- Helps prevent burnout
- Adds randomness so gameplay isn’t deterministic

Daily Loop
Each day:
- Characters choose actions
- Stats update
- Caps & checks are applied
- Day advances
- Poor decisions early can snowball hard later 👀

Design Goals
- Simple but expandable system
- Minimal UI (text-based)
- Easy to tweak values for balance testing
- Focus on logic, not graphics
- This project is built as a prototype/learning project, not a full game.

More Information

Language: Python
Style: Object-Oriented Programming
Dependencies: None (pure Python)

Notes: This project is mainly for:
- Practicing OOP
- Simulation logic
- Game system balancing

Feel free to fork, tweak, or break it :)
