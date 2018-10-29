import argparse
import sys


class Chess:
    # Chessboard notation box dictionary : Variable initialise
    CHESS_ROW = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    # I made this simple to get direct alpha notation from dictionary
    CHESS_COL_ALPHA = {1: "a", 2: "b", 3: "c",4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
    ALL_POSITION = []

    def setPosition(self, piece, position):
        col_position = self.CHESS_ROW[position[0]]
        row_position = position[1]
        col = int(col_position)
        row = int(row_position)
        return col, row


class Knight(Chess):
    def findPossiblePosition(self, piece, position):
        (col, row) = self.setPosition(piece, position)
        all_position = []
        # We can place KNIGHT at 8 position in 4 direction

        # Down Left
        if (row - 2) > 0 and (col - 1) > 0:
            all_position.append(self.CHESS_COL_ALPHA[col - 1] + str((row - 2)))

        # Down Right
        if (row - 2) > 0 and (col + 1) <= 8:
            all_position.append(self.CHESS_COL_ALPHA[col + 1] + str((row - 2)))

        # Left Down
        if (col - 2) > 0 and (row - 1) > 0:
            all_position.append(self.CHESS_COL_ALPHA[col - 2] + str((row - 1)))

        # Right Down
        if (col + 2) <= 8 and (row - 1) > 0:
            all_position.append(self.CHESS_COL_ALPHA[col + 2] + str((row - 1)))

        # Left Up
        if (col - 2) > 0 and (row + 1) <= 8:
            all_position.append(self.CHESS_COL_ALPHA[col - 2] + str((row + 1)))

        # Right Up
        if (col+2) <= 8 and (row+1) <= 8:
            all_position.append(self.CHESS_COL_ALPHA[col+2] + str((row+1)))

        # UP Left
        if (row+2) <= 8 and (col-1) > 0:
            all_position.append(self.CHESS_COL_ALPHA[col-1]+str((row+2)))

        # Down Right
        if (row+2) <= 8 and (col+1) <= 8:
            all_position.append(self.CHESS_COL_ALPHA[col+1] + str((row+2)))
        return all_position


class Rook(Chess):
    def findPossiblePosition(self,piece, position):
        (col, row) = self.setPosition(piece,position)
        all_position = []
        # We can also do this via two loop But as per your mention output in PDF
        # It is look like you want to traverse from  A1, A2...B1,B2... (Row)
        # That's why implementing logic like this
        # we can place ROOK at 4 position in 4 direction

        # All Down Position from 0 to ROOK
        for i in range(1, row):
            all_position.append(self.CHESS_COL_ALPHA[col] + str(i))

        # All Left Position from 0 to ROOK
        for i in range(1, col):
            all_position.append(self.CHESS_COL_ALPHA[i] + str(row))

        # All Right Position from ROOK to 8
        for i in range(col+1, 9):
            all_position.append(self.CHESS_COL_ALPHA[i] + str(row))

        # All Top Position from ROOK to 8
        for i in range(row+1, 9):
            all_position.append(self.CHESS_COL_ALPHA[col] + str(i))
        return all_position


class Queen(Chess):
    def findPossiblePosition(self,piece, position):
        (col, row) = self.setPosition(piece,position)
        all_position = []
        for row_number in range(1, 9):
            # first we have to print ROW then column
            if row == row_number:
                # All Left Position from 0 to QUEEN
                for i in range(1, col):
                    all_position.append(self.CHESS_COL_ALPHA[i] + str(row))
                # All Right Position from QUEEN to 8
                for i in range(col + 1, 9):
                    all_position.append(self.CHESS_COL_ALPHA[i] + str(row))
            else:
                # we need else condition because now back row will be first
                # if we need output in row ascending order
                # python chessercise.py -piece queen -position d3
                # check order of c4 and e4, if you don't add if else condition
                # output:      b1,f1,c2,e2,a3,b3,c3,e3,f3,g3,h3,c4,e4,b5,f5,a6,g6,h7
                # otherwise : b1,f1,c2,e2,a3,b3,c3,e3,f3,g3,h3,e4,c4,f5,b5,g6,a6,h7

                # Below code for diagonal placement
                if row_number < row:
                    if 0 < (col - row + row_number) < 9:
                        all_position.append(self.CHESS_COL_ALPHA[col - row + row_number] + str(row_number))
                    # place QUEEN for Bottom to Top one by one
                    all_position.append(self.CHESS_COL_ALPHA[col] + str(row_number))
                    if 0 < (col+row-row_number) < 9:
                        all_position.append(self.CHESS_COL_ALPHA[col+row-row_number] + str(row_number))
                else:
                    if 0 < (col+row-row_number) < 9:
                        all_position.append(self.CHESS_COL_ALPHA[col+row-row_number] + str(row_number))
                    # place QUEEN for Bottom to Top one by one
                    all_position.append(self.CHESS_COL_ALPHA[col] + str(row_number))
                    if 0 < (col - row + row_number) < 9:
                        all_position.append(self.CHESS_COL_ALPHA[col - row + row_number] + str(row_number))
        return all_position


def Factory(class_name):
    classes = dict(KNIGHT=Knight, QUEEN=Queen, ROOK=Rook)
    return classes[class_name]


def main():
    try:
        piece_help = "Piece name[KNIGHT, QUEEN, ROOK]"
        position_help = "Alpha Numeric Notation for chess board ex:[d2]"
        parser = argparse.ArgumentParser()
        parser.add_argument('-piece',  help=piece_help, type=str, default= '')
        parser.add_argument('-position',  help=position_help, type=str, default= '')
        args = parser.parse_args()
        # To remove input ambiguity, convert string into upper case
        # KNIGHT, QUEEN, ROOK
        _piece = args.piece.upper()
        # D3, d2 , e4
        _position = args.position.upper()
        if _piece == '' and _position == "":
            print("Please enter valid piece and position")
        elif _piece == '':
            print("Please enter valid piece")
        elif _position == '':
            print("Please enter  position")
        elif _piece not in ['KNIGHT', 'ROOK', 'QUEEN']:
            print("We only support KNIGHT, ROOK, QUEEN")
        elif len(_position) != 2:
            print("Invalid position")
        elif str(_position[0].lower()) not in Chess.CHESS_COL_ALPHA.values():
            print("Invalid position")
        elif int(_position[1]) not in Chess.CHESS_ROW.values():
            print("Invalid position number")
        else:
            obj = Factory(_piece)()
            # print(_piece)
            notation_str = obj.findPossiblePosition(_piece, _position)
            print(",".join(notation_str))
    except argparse.ArgumentError:
        print("Something went wrong, Please try again")
    except Exception as e:
        print(e)
        raise


if __name__== "__main__":
    main()







