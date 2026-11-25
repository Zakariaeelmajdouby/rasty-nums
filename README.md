# Rastynums

A small desktop number-guessing game built with **Python** and **Tkinter**.

This project was created as a learning project after working through multiple tutorials and using AI assistance for explanations, troubleshooting, and development support. I used these learning resources to understand the concepts and bring them together into a working application.

## About the Game

The game randomly selects a secret number between **1 and 100**. The player has **7 attempts** to guess it.

After each valid guess, the game gives a hint:
- **Too low** — the secret number is greater.
- **Too high** — the secret number is lower.
- **Correct** — the player wins.

If all 7 attempts are used, the game reveals the secret number. A dialog then asks whether the player wants to play again.

## Features

- Random secret number for each round
- 7 attempts per game
- Higher/lower hints after each guess
- Input validation for invalid numbers and values outside 1–100
- Attempt counter showing used and remaining attempts
- Start, Guess, and Reset buttons
- Press **Enter** to submit a guess
- Replay option after the game ends
- Simple graphical user interface (GUI)

## Built With

- **Python 3**
- **Tkinter** — graphical user interface
- **random** — secret number generation

Tkinter is included with most standard Python installations, so no additional Python packages are normally required.

## How to Run the exe

open dist
run the .exe

### Run from Python source

1. Install Python 3 if it is not already installed.
2. Download or clone this project.
3. Open a terminal or command prompt in the project folder.
4. Run:

   ```bash
   python Rastynums(1).py
   ```

   If your file has a different name, replace the filename with your own.

### Run the Windows executable

If you are using the provided Windows build, open the `dist` folder and launch the game executable.

> The executable is intended for Windows. If Windows displays a security warning, make sure the file came from a source you trust before running it.

## How to Play

1. Click **START GAME**.
2. Enter a whole number from **1 to 100**.
3. Click **GUESS** or press **Enter**.
4. Follow the hint and try to find the secret number within 7 attempts.
5. Choose whether to play another round when prompted.

## What I Learned

While working on this project, I practiced:

- Creating a desktop GUI with Tkinter
- Organizing code with a Python class
- Using methods to separate game actions
- Generating random numbers
- Handling user input and exceptions
- Updating labels and button states
- Tracking game state and attempts
- Responding to button clicks and keyboard events

## Learning Process & Acknowledgements

This is a beginner learning project. I developed it by studying and following several tutorials, experimenting with the code, and using AI assistance to help explain concepts, troubleshoot issues, and support the development process.

The goal of this project was to learn by building a complete, interactive application and to continue improving my Python programming skills.

---

# Zahlen-Ratespiel

Ein kleines Desktop-Zahlenratespiel, das mit **Python** und **Tkinter** entwickelt wurde.

Dieses Projekt ist ein Lernprojekt. Bei der Entwicklung habe ich mehrere Tutorials durchgearbeitet und KI-Unterstützung für Erklärungen, Fehlersuche und Entwicklungsfragen genutzt. Mithilfe dieser Lernressourcen habe ich die verschiedenen Konzepte verstanden und in einer funktionierenden Anwendung zusammengeführt.

## Über das Spiel

Das Spiel wählt zufällig eine geheime Zahl zwischen **1 und 100** aus. Der Spieler hat **7 Versuche**, um die Zahl zu erraten.

Nach jedem gültigen Tipp gibt das Spiel einen Hinweis:
- **Zu niedrig** — die gesuchte Zahl ist größer.
- **Zu hoch** — die gesuchte Zahl ist kleiner.
- **Richtig** — der Spieler gewinnt.

Wenn alle 7 Versuche verbraucht sind, wird die geheime Zahl angezeigt. Anschließend fragt ein Dialog, ob eine weitere Runde gespielt werden soll.

## Funktionen

- Zufällige geheime Zahl in jeder Runde
- 7 Versuche pro Spiel
- Hinweise „höher“ oder „niedriger“ nach jedem Tipp
- Eingabeprüfung für ungültige Zahlen und Werte außerhalb von 1–100
- Versuchsanzeige mit bereits genutzten und verbleibenden Versuchen
- Schaltflächen für Start, Tipp und Zurücksetzen
- Mit **Enter** kann ein Tipp abgeschickt werden
- Möglichkeit, nach Spielende erneut zu spielen
- Einfache grafische Benutzeroberfläche (GUI)

## Verwendete Technologien

- **Python 3**
- **Tkinter** — grafische Benutzeroberfläche
- **random** — Erzeugung der geheimen Zufallszahl

Tkinter ist in den meisten standardmäßigen Python-Installationen enthalten. Daher sind normalerweise keine zusätzlichen Python-Pakete erforderlich.

## Ausführung

### Mit dem Python-Quellcode starten

1. Installiere Python 3, falls es noch nicht installiert ist.
2. Lade dieses Projekt herunter oder klone das Repository.
3. Öffne ein Terminal oder die Eingabeaufforderung im Projektordner.
4. Führe folgenden Befehl aus:

   ```bash
   python gastynums(1).py
   ```

   Falls die Datei einen anderen Namen hat, ersetze den Dateinamen entsprechend.

### Die Windows-Version starten

Wenn du die bereitgestellte Windows-Version verwendest, öffne den Ordner `dist` und starte die ausführbare Spieldatei.

> Die ausführbare Datei ist für Windows vorgesehen. Wenn Windows eine Sicherheitswarnung anzeigt, prüfe vor dem Start, ob die Datei aus einer vertrauenswürdigen Quelle stammt.

## Spielanleitung

1. Klicke auf **START GAME**.
2. Gib eine ganze Zahl zwischen **1 und 100** ein.
3. Klicke auf **GUESS** oder drücke **Enter**.
4. Folge dem Hinweis und versuche, die geheime Zahl innerhalb von 7 Versuchen zu finden.
5. Entscheide im Dialog, ob du eine weitere Runde spielen möchtest.

## Was ich gelernt habe

Während der Entwicklung dieses Projekts habe ich geübt:

- Eine Desktop-GUI mit Tkinter zu erstellen
- Python-Code mit einer Klasse zu strukturieren
- Methoden für einzelne Spielaktionen zu verwenden
- Zufallszahlen zu erzeugen
- Benutzereingaben und Ausnahmen zu behandeln
- Labels und Schaltflächen dynamisch zu aktualisieren
- Spielzustand und Versuche zu verwalten
- Auf Mausklicks und Tastaturereignisse zu reagieren

## Lernprozess & Danksagung

Dies ist ein Anfänger-Lernprojekt. Ich habe es entwickelt, indem ich mehrere Tutorials studiert und nachvollzogen, mit dem Code experimentiert und KI-Unterstützung genutzt habe, um Konzepte besser zu verstehen, Fehler zu beheben und die Entwicklung zu unterstützen.

Das Ziel dieses Projekts war es, durch praktische Umsetzung eine vollständige, interaktive Anwendung zu erstellen und meine Python-Kenntnisse weiterzuentwickeln.
