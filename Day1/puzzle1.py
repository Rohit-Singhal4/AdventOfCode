def read_lists(filename):
    list1 = []
    list2 = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                num1, num2 = map(int, line.split())
                list1.append(num1)
                list2.append(num2)
    print("List1:", list1)
    print("List2:", list2)
    return list1, list2

def calculate_total_distance(list1, list2):
    list1.sort()
    list2.sort()
    total_distance = sum(abs(a - b) for a, b in zip(list1, list2))
    return total_distance

def main():
    filename = 'input.txt'
    list1, list2 = read_lists(filename)
    total_distance = calculate_total_distance(list1, list2)
    print("Total Distance:", total_distance)

if __name__ == "__main__":
    main()