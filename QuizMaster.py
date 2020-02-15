import MatrixMultGenerator as mmg
import numpy as np
import time


class QuizMaster:

    num_questions = 5
    difficult = 2
    gen = mmg.MatrixMultGenerator
    start_time = time.time()

    def QuizMaster(self, num_questions, difficulty):
        self.num_questions = num_questions
        self.difficulty = difficulty

    def start(self):
        self.num_questions_answered = 0
        self.num_questions_correct = 0
        self.start_time = time.time()

        self.gen = mmg.MatrixMultGenerator()

        while(self.num_questions > self.num_questions_answered):
            self.loop()

        self.end()

    def loop(self):
        # TODO: generate these based on difficulty
        rows = 3
        cols = 1
        mid = 3
        m1, m2, sol = self.gen.generate(rows, cols, mid, True)
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
                self.num_questions_correct += 1
                print("CORRECT")
            else:
                print("WRONG: \n" + str(sol))

        self.num_questions_answered += 1

    def end(self):
        end_time = time.time()
        total_time = end_time - self.start_time
        accuracy = float(self.num_questions_correct) / \
            float(self.num_questions_answered)
        print("Accuracy: " + str(accuracy))
        print("Time: " + str(total_time))
        # TODO: return stats for recording
