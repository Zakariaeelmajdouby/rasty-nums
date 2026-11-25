import tkinter as tk
from tkinter import messagebox
import random
 
# Constants (change here only)
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7
 
 
class RastyNums:
    def __init__(self, root):
        self.root = root
        self.root.title("RastyNums")
        self.root.geometry("480x360")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.number = 0
        self.attempts = 0
        self.max_attempts = MAX_ATTEMPTS
        self.guesses = []
        self.game_started = False
        
        # Title
        self.title_label = tk.Label(
            root, 
            text="🎮 RastyNums", 
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        self.title_label.pack(pady=15)
        
        # Instructions
        self.instruction_label = tk.Label(
            root,
            text=f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}\n(You have {MAX_ATTEMPTS} attempts)",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666"
        )
        self.instruction_label.pack(pady=10)
        
        # Input field
        self.input_frame = tk.Frame(root, bg="#f0f0f0")
        self.input_frame.pack(pady=10)
        
        self.input_label = tk.Label(
            self.input_frame,
            text="Enter your guess:",
            font=("Arial", 10),
            bg="#f0f0f0"
        )
        self.input_label.grid(row=0, column=0, padx=5)
        
        self.input_entry = tk.Entry(
            self.input_frame,
            font=("Arial", 12),
            width=15,
            state="disabled"
        )
        self.input_entry.grid(row=0, column=1, padx=5)
        self.input_entry.bind("<Return>", lambda e: self.guess())
        
        # Message display
        self.message_label = tk.Label(
            root,
            text="",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#0066cc",
            wraplength=350
        )
        self.message_label.pack(pady=10)
        
        # Attempts display
        self.attempts_label = tk.Label(
            root,
            text="",
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="#ff6600"
        )
        self.attempts_label.pack(pady=5)
        
        # Buttons frame
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=15)
        
        # New Game button (replaces START and RESET)
        self.new_game_button = self.make_button("NEW GAME", "#4CAF50", self.start_game)
        self.new_game_button.grid(row=0, column=0, padx=5)
        
        # Guess button
        self.guess_button = self.make_button("GUESS", "#2196F3", self.guess, state="disabled")
        self.guess_button.grid(row=0, column=1, padx=5)
    
    def make_button(self, text, color, command, state="normal"):
        """Create a button with the shared style"""
        return tk.Button(
            self.button_frame,
            text=text,
            font=("Arial", 11, "bold"),
            bg=color,
            fg="white",
            padx=20,
            pady=8,
            command=command,
            state=state,
            cursor="hand2"
        )
    
    def start_game(self):
        """Start a new game (also used to restart)"""
        self.number = random.randint(MIN_NUMBER, MAX_NUMBER)
        self.attempts = 0
        self.max_attempts = MAX_ATTEMPTS
        self.guesses = []
        self.game_started = True
        
        self.input_entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        
        self.message_label.config(text="Game started! Enter your first guess.", fg="#0066cc")
        self.update_attempts_display()
    
    def guess(self):
        """Process the player's guess"""
        if not self.game_started:
            messagebox.showwarning("Warning", "Please start the game first!")
            return
        
        # Only int() is inside the try
        try:
            guess = int(self.input_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return
        
        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            messagebox.showerror("Error", f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}!")
            return
        
        # Duplicate guess: do not count it as an attempt
        if guess in self.guesses:
            messagebox.showinfo("Info", f"You already tried {guess}!")
            return
        
        self.guesses.append(guess)
        self.attempts += 1
        self.input_entry.delete(0, tk.END)
        
        if guess == self.number:
            word = "attempt" if self.attempts == 1 else "attempts"
            self.message_label.config(
                text=f"🎉 Congratulations!\nYou guessed the number {self.number}\nin {self.attempts} {word}!",
                fg="#4CAF50"
            )
            self.update_attempts_display()
            self.end_game()
            self.show_play_again()
        elif guess < self.number:
            self.message_label.config(
                text=f"📈 Too low! The number is greater than {guess}",
                fg="#ff6600"
            )
            self.update_attempts_display()
        else:
            self.message_label.config(
                text=f"📉 Too high! The number is less than {guess}",
                fg="#ff6600"
            )
            self.update_attempts_display()
        
        # Check if out of attempts
        if self.attempts >= self.max_attempts and guess != self.number:
            self.message_label.config(
                text=f"💔 Game Over!\nThe correct number was: {self.number}",
                fg="#f44336"
            )
            self.end_game()
            self.show_play_again()
    
    def update_attempts_display(self):
        """Update the attempts counter display"""
        remaining = self.max_attempts - self.attempts
        self.attempts_label.config(
            text=f"Attempts: {self.attempts}/{self.max_attempts} (Remaining: {remaining})"
        )
    
    def end_game(self):
        """End the current game"""
        self.game_started = False
        self.input_entry.config(state="disabled")
        self.guess_button.config(state="disabled")
        self.new_game_button.config(state="normal")
    
    def show_play_again(self):
        """Show play again dialog"""
        result = messagebox.askyesno("Game Over", "Do you want to play again?")
        if result:
            self.start_game()
 
 
if __name__ == "__main__":
    root = tk.Tk()
    app = RastyNums(root)
    root.mainloop()
 
