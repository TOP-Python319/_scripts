import random
from stages import STAGES


class WordLoader:
    def __init__(self, words_file="words.txt"):
        self.words = self.load_words(words_file)

    def load_words(self, words_file):
        with open(words_file, "r") as f:
            return [word.strip() for word in f.readlines()]

    def get_random_word(self):
        return random.choice(self.words)


class HangmanState:
    def __init__(self, word, max_attempts):
        self.word = word
        self.max_attempts = max_attempts
        self.attempts = max_attempts
        self.guessed_letters = []

    def guess_letter(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            return True
        elif letter not in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            self.attempts -= 1
            return False
        else:
            return None

    def get_game_state(self):
        word_state = ["_" if letter not in self.guessed_letters else letter for letter in self.word]
        return {
            "word": " ".join(word_state),
            "attempts": self.attempts,
            "guessed_letters": " ".join(sorted(self.guessed_letters)),
        }

    def is_won(self):
        return all([letter in self.guessed_letters for letter in self.word])

    def is_lost(self):
        return self.attempts == 0


class HangmanGraphics:
    stages = STAGES

    @staticmethod
    def display(attempts_left):
        index = max(0, len(HangmanGraphics.stages) - (attempts_left + 1))
        print(HangmanGraphics.stages[index])


class HangmanGame:
    def __init__(self, words_file="words.txt", max_attempts=7):
        self.word_loader = WordLoader(words_file)
        self.max_attempts = max_attempts
        self.reset()

    def reset(self):
        word = self.word_loader.get_random_word()
        self.state = HangmanState(word, self.max_attempts)

    def guess_letter(self, letter):
        return self.state.guess_letter(letter)

    def get_game_state(self):
        return self.state.get_game_state()

    def is_won(self):
        return self.state.is_won()

    def is_lost(self):
        return self.state.is_lost()


class HangmanConsoleUI:
    def __init__(self):
        self.game = HangmanGame()
        self.game_state = self.game.get_game_state()
        self.is_running = True

    def show_game_state(self):
        HangmanGraphics.display(self.game_state['attempts'])
        print(f"Word: {self.game_state['word']}")
        print(f"Attempts left: {self.game_state['attempts']}")
        print(f"Guessed letters: {self.game_state['guessed_letters']}")

    def get_user_input(self):
        letter = input("Enter a letter: ").lower().strip()
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Please enter a single letter.")
            return self.get_user_input()
        return letter

    def update_game_state(self):
        self.game_state = self.game.get_game_state()

    def run(self):
        while self.is_running:
            self.show_game_state()
            letter = self.get_user_input()
            guess_result = self.game.guess_letter(letter)
            if guess_result is None:
                print(f"You have already guessed the letter '{letter}'. Please try again.")
            elif guess_result:
                print(f"You have guessed the letter '{letter}'. Good job!")
                self.update_game_state()
                if self.game.is_won():
                    self.show_game_state()
                    print("Congratulations! You have won the game!")
                    self.is_running = False
            else:
                print(f"You have missed the letter '{letter}'. Try again.")
                self.update_game_state()
                if self.game.is_lost():
                    self.show_game_state()
                    print(f"Sorry, you have lost the game. The word was '{self.game.state.word}'.")
                    self.is_running = False


if __name__ == "__main__":
    ui = HangmanConsoleUI()
    ui.run()
