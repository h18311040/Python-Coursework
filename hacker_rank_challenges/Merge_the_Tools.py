def merge_the_tools(string, k):
    # your code goes here
    t = {}
    start = 0
    for x in range(round(len(string) / k)):
        splitter = string[start:start + k]
        t[x] = splitter
        start += k

    for x in range(len(t.keys())):
        print("".join(t.fromkeys(t[x])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)