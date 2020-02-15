import sys
import getopt
import MatrixMultGenerator
import numpy as np
import time


def main(argv):
    try:
        optns, args = getopt.getopt(argv, "n", ["number"])
    except getopt.GetoptError:
        print("Args error")

    num_questions = int(args[0])
    num_questions_answered = 0
    num_questions_correct = 0
    start_time = time.time()

    gen = MatrixMultGenerator.MatrixMultGenerator()

    while(num_questions > num_questions_answered):
        # TODO: generate these based on difficulty
        rows = 3
        cols = 1
        mid = 3
        m1, m2, sol = gen.generate(rows, cols, mid, True)
        print(m1)
        print(m2)
        try:
            in_entries = list(map(int, input("Input answer:").split()))
        except:
            print("Input error!")

        if (len(in_entries) != rows * cols):
            print("Incorrect entry count. Matrix shape is " +
                  str(rows) + " x " + str(cols))
            print(str(sol))
        else:
            in_mat = np.array(in_entries).reshape(rows, cols)
            if (np.all(in_mat == sol)):
                num_questions_correct += 1
                print("CORRECT")
            else:
                print("WRONG: \n" + str(sol))

        num_questions_answered += 1

    end_time = time.time()
    total_time = end_time - start_time
    accuracy = float(num_questions_correct) / float(num_questions_answered)
    print("Accuracy: " + str(accuracy))
    print("Time: " + str(total_time))
    return


if __name__ == "__main__":
    main(sys.argv[1:])
