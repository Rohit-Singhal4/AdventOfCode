from collections import Counter 

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

def calculate_similarity_score(list1, list2):
    count_list2 = Counter(list2)
    similarity_score = sum(num * count_list2[num] for num in list1)
    return similarity_score

def main():
    filename = 'input.txt'
    list1, list2 = read_lists(filename)
    similarity_score = calculate_similarity_score(list1, list2)
    print("Similarity Score:", similarity_score)

if __name__ == "__main__":
    main()