doc = input(); srch = input()
count = 0

while len(list(doc)) >= len(list(srch)):
    if list(doc)[:len(srch)] == list(srch):
        count += 1
        doc = list(doc)[len(srch):]
    else:
        doc = list(doc)[1:]
        
print(count)