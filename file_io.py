"""
Program: file_io_using_tuples_assignment
Author: Ryan Blankenship
Last Date Modified: 10/9/2019


"""


def write_to_file(info_file):
    # open the file
    f = open('student_info.txt', 'a')
    # write to file
    f.write(str(info_file))
    # close the file
    f.close()


def get_student_info(**scores):
    # prompt the user by name
    for key, value in scores.items():
        print(value)
    # while sentinel value not met (user still has input)
    score = 0
    sentinel = -1
    info_file = [scores]
    # prompt user for next score
    while score >= 0:
        try:
            score = int(input("Please enter your score or enter -1 to quit: "))
        except ValueError:
            print("Please enter numbers only for scores.")
        else:
            if score == sentinel:
                break
            # add to a list
            else:
                info_file.append(score)
    # write_to_file(# sent keyword arg with list)
    write_to_file(info_file)


def read_from_file():
    # open the file
    f = open('student_info.txt', 'r')
    # read from file (while loop to read entire file)
    line = f.readline()
    # print the line
    print(line)
    # close the file
    f.close()


if __name__ == '__main__':
    get_student_info(name='ryan')
    get_student_info(name='jamie')
    get_student_info(name='abi')
    get_student_info(name='bella')
    read_from_file()
