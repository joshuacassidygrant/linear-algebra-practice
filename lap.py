import sys
import getopt
import MatrixMultGenerator
import numpy as np


def main(argv):
    try:
        optns, args = getopt.getopt(argv, "n", ["number"])
    except getopt.GetoptError:
        print("Args error")

    num_questions = int(args[0])
    num_questions_answered = 0

    gen = MatrixMultGenerator.MatrixMultGenerator()

    while(num_questions > num_questions_answered):
        # TODO: generate these based on difficulty
        rows = 2
        cols = 3
        mid = 4
        gen.generate(rows, cols, mid, True)
        try:
            in_entries = list(map(int, input("Input answer:").split()))
            # TODO: make sure rows/cols match
            in_mat = np.array(in_entries).reshape(rows, cols)
            print(in_mat)
        except:
            print("Input error")
        num_questions_answered += 1
    return


if __name__ == "__main__":
    main(sys.argv[1:])
