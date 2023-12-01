def first_and_last(line):
    left = 0
    right = len(line) - 1

    while True:
        if line[left].isdigit() and line[right].isdigit():
            return (line[left], line[right])
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
        num = str(left) + str(right)
        total += int(num)

    print(total)

if __name__ == '__main__':
    main()
                