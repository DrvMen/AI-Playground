import streamlit as st
import numpy as np

# Tic-Tac-Toe Game Logic


class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), " ")
        self.current_player = "X"
        self.game_over = False
        self.winner = None

    def make_move(self, row, col):
        if self.board[row, col] == " " and not self.game_over:
            self.board[row, col] = self.current_player
            if self.check_winner():
                self.game_over = True
                self.winner = self.current_player
                return f"Player {self.current_player} wins!"
            elif " " not in self.board:
                self.game_over = True
                return "It's a draw!"

            self.current_player = "O" if self.current_player == "X" else "X"
        return "Invalid move or game over."

    def check_winner(self):
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player) or np.all(self.board[:, i] == self.current_player):
                return True
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] == self.current_player:
            return True
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] == self.current_player:
            return True
        return False

# Streamlit UI for Tic-Tac-Toe


def play_tic_tac_toe():
    st.title("Tic-Tac-Toe")

    # Initialize game state
    if "game" not in st.session_state:
        st.session_state.game = TicTacToe()
    game = st.session_state.game

    result = None

    # Create board layout
    cols = [st.columns(3) for _ in range(3)]
    for row in range(3):
        for col in range(3):
            cell_value = game.board[row, col]
            button_color = "gray" if cell_value == " " else (
                "blue" if cell_value == "X" else "red")
            if cols[row][col].button(cell_value, key=f"{row}{col}", help=f"{cell_value}", use_container_width=True):
                if not game.game_over:
                    result = game.make_move(row, col)
                    st.session_state.game = game
                    st.rerun()
            st.markdown(
                f'<style>div[data-testid="stButton"]:has(button[title="{cell_value}"]) button {{background-color: {button_color}; color: white;}}</style>', unsafe_allow_html=True)

    st.write(f"Current Turn: Player {game.current_player}")

    # Show game result
    if game.game_over:
        st.success(
            f"Game Over! {result if result else f'Player {game.winner} wins!' if game.winner else 'Its a draw!'}")
        if st.button("Restart Game"):
            st.session_state.game = TicTacToe()
            st.rerun()


# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()
