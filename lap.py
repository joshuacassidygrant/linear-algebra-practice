import sys
import getopt
import MatrixMultGenerator


def main(argv):
    try:
        optns, args = getopt.getopt(argv, "n", ["number"])
    except getopt.GetoptError:
        print("Args error")

    num_questions = int(args[0])
    num_questions_answered = 0

    gen = MatrixMultGenerator.MatrixMultGenerator()

    while(num_questions > num_questions_answered):
        gen.generate(2, 3, 4, True)
        inv = input("Input answer:")
        num_questions_answered += 1
    return


if __name__ == "__main__":
    main(sys.argv[1:])
