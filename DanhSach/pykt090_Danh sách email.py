with open('tệp văn bản\Contact.in') as file:
    lines = file.readlines()
ds = []
for i in lines:
    i = i.rstrip().lower()
    ds.append(i)

kq = sorted(set(ds))
for i in kq:
    print(i)