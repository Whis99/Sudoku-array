# Étant donné un tableau 2D, de taille 9 × 9, qui représente une solution au puzzle Sudoku,
# la tâche consiste à vérifier si la représentation donnée
# d'un puzzle Sudoku résolu est valide ou non. Retourner True ou False.
# Vous pouvez écrire d'autres fonctions pour vous aider avec la fonction principale qui es "estValidé".

def rowLine(sudo):
    tab = []
    # Check rows
    for i in range(9):
        for j in range(9):
            if sudo[i][j] != '.':
                tab.append(sudo[i][j])
        if len(tab) != len(set(tab)):
            return False
        tab.clear()

    # Check columns
    for i in range(9):
        for j in range(9):
            if sudo[j][i] != '.':
                tab.append(sudo[j][i])
        if len(tab) != len(set(tab)):
            return False
        tab.clear()
    return True


def board2(tab):
    # Check 3x3 grids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            tab[row][col]
            lst = []
            for i in range(3):
                for j in range(3):
                    if tab[row + i][col + j] != '.':
                        lst.append(tab[row + i][col + j])
            if len(lst) != len(set(lst)):
                return False
            lst.clear()
    return True


def estValidé(board):
    if rowLine(board) == True and board2(board) == True:
        return True
    else:
        return False


# True
sudoku1 = [
    [".", ".", ".", "1", "4", ".", ".", "2", "."],
    [".", ".", "6", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "1", ".", ".", ".", ".", ".", "."],
    [".", "6", "7", ".", ".", ".", ".", ".", "9"],
    [".", ".", ".", ".", ".", ".", "8", "1", "."],
    [".", "3", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", "7", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", "7", "."]]

# False
sudoku2 = [
    [".", ".", ".", ".", "2", ".", ".", "9", "."],
    [".", ".", ".", ".", "6", ".", ".", ".", "."],
    ["7", "1", ".", ".", "7", "5", ".", ".", "."],
    [".", "7", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "8", "3", ".", ".", "."],
    [".", ".", "8", ".", ".", "7", ".", "6", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "1", ".", "2", ".", ".", ".", ".", "."],
    [".", "2", ".", ".", "3", ".", ".", ".", "."]]

# False
sudoku3 = [
    [".", ".", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "8", ".", ".", ".", "3", "."],
    [".", "5", ".", ".", "2", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "9"],
    [".", ".", ".", ".", ".", ".", "4", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "7"],
    [".", "1", ".", ".", ".", ".", ".", ".", "."],
    ["2", "4", ".", ".", ".", ".", "9", ".", "."]]


# True
sudoku4 = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "2", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", "7", "1", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", ".", ".", ".", ".", ".", "."],
    [".", "5", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "9", ".", ".", ".", "8"],
    [".", ".", ".", ".", ".", "1", "6", ".", "."],
    [".", ".", ".", ".", "6", ".", ".", ".", "."]]

if __name__ == '__main__':
    print(f'sudoku1:  {estValidé(sudoku1)}')
    print(f'sudoku2:  {estValidé(sudoku2)}')
    print(f'sudoku3:  {estValidé(sudoku3)}')
    print(f'sudoku4:  {estValidé(sudoku4)}')