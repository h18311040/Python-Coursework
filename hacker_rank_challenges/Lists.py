if __name__ == '__main__':
    N = int(input())

    final = []
    for i in range(0, N):
        ip = input().split()
        if ip[0] == "print":
            print(final)
        elif ip[0] == "insert":
            final.insert(int(ip[1]), int(ip[2]))
        elif ip[0] == "remove":
            final.remove(int(ip[1]))
        elif ip[0] == "pop":
            final.pop()
        elif ip[0] == "append":
            final.append(int(ip[1]))
        elif ip[0] == "sort":
            final.sort()
        else:
            final.reverse()