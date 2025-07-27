import random
import streamlit as st

# Function to add a background image from a URL
def add_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to add the background image
image_url = "https://th.bing.com/th?id=OIP.igZrVaK6I1n8Nyeq6rrWYAHaIw&w=229&h=271&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2"  # Replace with your image URL
add_bg_from_url(image_url)

# List of words for the game
words = ['noor', 'java', 'fatima', 'iman', 'nida', 'fiza', 'shumail']

def get_word():
    return random.choice(words).lower()

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[tries]

# Initialize the session state
if 'word' not in st.session_state:
    st.session_state.word = get_word()
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.guessed_letters = set()
    st.session_state.tries = 6
    st.session_state.game_over = False
    st.session_state.game_won = False

def reset_game():
    st.session_state.word = get_word()
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.guessed_letters = set()
    st.session_state.tries = 6
    st.session_state.game_over = False
    st.session_state.game_won = False

def make_guess(guess):
    if guess in st.session_state.word_letters:
        st.session_state.guessed_letters.add(guess)
        st.session_state.word_letters.remove(guess)
        if not st.session_state.word_letters:
            st.session_state.game_won = True
            st.session_state.game_over = True
    else:
        st.session_state.tries -= 1
        if st.session_state.tries == 0:
            st.session_state.game_over = True

# Streamlit UI layout
st.title("Hangman Game")

st.text(display_hangman(st.session_state.tries))

word_display = [letter if letter in st.session_state.guessed_letters else '_' for letter in st.session_state.word]
st.text("Word: " + " ".join(word_display))

if st.session_state.game_over:
    if st.session_state.game_won:
        st.success(f"Congratulations! You guessed the word '{st.session_state.word}'.")
    else:
        st.error(f"Game Over! The word was '{st.session_state.word}'.")
    if st.button("Play Again"):
        reset_game()
else:
    guess = st.text_input("Guess a letter:", max_chars=1).lower()
    if st.button("Submit Guess") and guess:
        if guess not in st.session_state.guessed_letters:
            make_guess(guess)
        else:
            st.warning("You already guessed that letter.")

    st.text(f"Guessed letters: {' '.join(sorted(st.session_state.guessed_letters))}")
    st.text(f"Tries remaining: {st.session_state.tries}")
