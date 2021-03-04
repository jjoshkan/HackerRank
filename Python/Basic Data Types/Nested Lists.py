if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_highest = sorted(list(set([marks for name, marks in records])))[1]
    print('\n'.join([a for a,b in sorted(records) if b == second_highest]))