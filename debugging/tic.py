#!/usr/bin/python3

def print_board(board):
    """Imprime el tablero con separadores claros."""
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))


def check_winner(board):
    """Devuelve True si existe línea ganadora en filas, columnas o diagonales."""
    size = len(board)
    # Filas
    for row in board:
        if row[0] != " " and all(cell == row[0] for cell in row):
            return True
    # Columnas
    for col in range(size):
        col_vals = [board[row][col] for row in range(size)]
        if col_vals[0] != " " and all(cell == col_vals[0] for cell in col_vals):
            return True
    # Diagonales
    diag1 = [board[i][i] for i in range(size)]
    diag2 = [board[i][size - 1 - i] for i in range(size)]
    if diag1[0] != " " and all(cell == diag1[0] for cell in diag1):
        return True
    if diag2[0] != " " and all(cell == diag2[0] for cell in diag2):
        return True

    return False


def tic_tac_toe():
    """Loop principal del juego, cambiando turnos, validando entradas y detectando fin."""
    size = 3
    board = [[" " for _ in range(size)] for _ in range(size)]
    player = "X"
    moves = 0
    max_moves = size * size

    while True:
        print_board(board)

        # Pedir fila y columna con validación robusta
        while True:
            try:
                raw = input(f"Player {player}, enter row and column (e.g. '1 2'): ").strip().split()
                if len(raw) != 2:
                    raise ValueError("Debes ingresar dos números separados por espacio.")
                row, col = map(int, raw)
                if not (0 <= row < size and 0 <= col < size):
                    raise IndexError("Fuera de rango. Usa valores entre 0 y 2.")
                if board[row][col] != " ":
                    raise RuntimeError("La celda ya está ocupada.")
                break
            except ValueError as ve:
                print("Error de entrada:", ve)
            except IndexError as ie:
                print("Error de rango:", ie)
            except RuntimeError as re:
                print("Error de celda:", re)

        # Marcar jugada
        board[row][col] = player
        moves += 1

        # Verificar si hay ganador
        if check_winner(board):
            print_board(board)
            print(f"🎉 ¡Player {player} wins!")
            return

        # Verificar empate
        if moves == max_moves:
            print_board(board)
            print("🤝 It's a draw!")
            return

        # Cambiar turno
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    try:
        tic_tac_toe()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
