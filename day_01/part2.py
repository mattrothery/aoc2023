number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find_left(line, word):
    return line.find(word)

def find_right(line, word):
    return line.rfind(word)

def first_and_last(line):
    left = 0
    right = len(line) - 1

    while True:
        if line[left].isdigit() and line[right].isdigit():
            return (left, right)
        else:
            if not line[left].isdigit():
                left += 1
            if not line[right].isdigit():
                right -= 1

def main():
    # read each line of input file
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        (left, right) = first_and_last(line)
        left_word, right_word = "", ""

        for word in number_words:
            idx = find_left(line, word)
            if idx != -1 and idx < int(left):
                left = idx
                left_word = word

            idx = find_right(line, word)
            if idx != -1 and idx > int(right):
                right = idx
                right_word = word

        left, right = line[left], line[right]

        if left_word != "":
            left = str(number_words.index(left_word) + 1)
        
        if right_word != "":
            right = str(number_words.index(right_word) + 1)

        
        num = str(left) + str(right)
        total += int(num)

    print(total)

if __name__ == '__main__':
    main()
