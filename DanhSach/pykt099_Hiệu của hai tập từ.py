def list_tu(path):
    kq = []
    with open(path) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    for i in lines:
        tmp = i.split()
        kq.extend(tmp)
    return set([i.lower() for i in kq])

file1 = "tệp văn bản\DATA1.in"
file2 = "tệp văn bản\DATA2.in"

tu1 = set(list_tu(file1))
tu2 = set(list_tu(file2))

l1 = tu1.difference(tu2)
l2 = tu2.difference(tu1)

dong1 = sorted(list(l1))
dong2 = sorted(list(l2))
print(*dong1)
print(*dong2)