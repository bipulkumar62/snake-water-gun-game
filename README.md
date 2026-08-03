# 🐍 Snake Water Gun Game (Python)

A simple command-line implementation of the classic **Snake 🐍, Water 💧, Gun 🔫** game using Python.

## 📖 About

This project is a beginner-friendly Python game where the player competes against the computer.

The computer randomly selects one of the three choices:

* 🐍 Snake (`1`)
* 💧 Water (`-1`)
* 🔫 Gun (`0`)

The player's choice is then compared with the computer's choice to determine whether the player **wins**, **loses**, or the game ends in a **tie**.

---

## 🎮 Game Rules

| Player      | Computer    | Result |
| ----------- | ----------- | ------ |
| Snake 🐍    | Water 💧    | ✅ Win  |
| Water 💧    | Gun 🔫      | ✅ Win  |
| Gun 🔫      | Snake 🐍    | ✅ Win  |
| Same Choice | Same Choice | 🤝 Tie |
| Otherwise   | -           | ❌ Lose |

---

## 🛠️ Features

* Random computer choice
* User input from terminal
* Win / Lose / Tie detection
* Beginner-friendly Python logic
* Easy to understand and modify

---

## 📂 Project Structure

```text
snake-water-gun/
│
├── main.py
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/snake-water-gun.git
```

### 2. Open the project

```bash
cd snake-water-gun
```

### 3. Run the game

```bash
python main.py
```

---

## 💡 Concepts Used

* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* Random Module
* Comparison Logic
* Basic Game Development

---

## 🎯 Learning Outcome

This project helped me practice:

* Python fundamentals
* Writing conditional logic
* Using the `random` module
* Building a simple interactive CLI game
* Organizing a basic Python project

---

## 📌 Future Improvements

* Play multiple rounds
* Keep score
* Better input validation
* Difficulty levels
* GUI version using Tkinter or Pygame

---

## 👨‍💻 Author

**Bipul Kumar**

Learning Python by building small projects and gradually moving toward production-level software development.

⭐ If you found this project useful, consider giving it a star!
