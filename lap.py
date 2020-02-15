import sys
import getopt
import QuizMaster as qm


def main(argv):
    try:
        optns, args = getopt.getopt(argv, "n", ["number"])
    except getopt.GetoptError:
        print("Args error")

    # TODO: get args for difficulty, length
    quiz_master = qm.QuizMaster()
    quiz_master.start()


if __name__ == "__main__":
    main(sys.argv[1:])
