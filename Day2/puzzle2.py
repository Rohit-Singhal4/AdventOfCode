def is_safe_report(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def can_be_safe(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

def count_safe_reports(filename):
    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_report(report) or can_be_safe(report):
                safe_count += 1
    return safe_count

def main():
    filename = 'input.txt'
    safe_reports = count_safe_reports(filename)
    print("Number of safe reports:", safe_reports)

if __name__ == "__main__":
    main()