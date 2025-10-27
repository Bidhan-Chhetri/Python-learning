import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def choose(self):
        choice = input(f"{self.name}, choose Rock, Paper, or Scissors: ").lower()
        while choice not in ['rock', 'paper', 'scissors']:
            print("❌ Invalid choice. Try again.")
            choice = input(f"{self.name}, choose Rock, Paper, or Scissors: ").lower()
        return choice

class Game:
    def __init__(self, player):
        self.player = player
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user, computer):
        print(f"🧑 You chose: {user}")
        print(f"🤖 Computer chose: {computer}")
        if user == computer:
            print("😐 It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            print("🎉 You win!")
            self.player.score += 1
        else:
            print("💥 You lose!")

    def play(self):
        while True:
            user_choice = self.player.choose()
            computer_choice = self.get_computer_choice()
            self.decide_winner(user_choice, computer_choice)
            print(f"🏆 Score: {self.player.name} - {self.player.score}")
            again = input("Play again? (y/n): ").lower()
            if again != 'y':
                print("👋 Thanks for playing!")
                break

if __name__ == "__main__":
    name = input("Enter your name: ")
    player = Player(name)
    game = Game(player)
    game.play()