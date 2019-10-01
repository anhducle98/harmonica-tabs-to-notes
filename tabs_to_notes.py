import sys

def read_notes():
    id = 1;
    notes = {}
    for line in open("tremolo_notes"):
        notes[id] = line.strip()
        id += 1
    return notes

def read_eng_to_vie():
    eng_to_vie = {}
    for line in open("eng_to_vie"):
        temp = line.strip().split('\t')
        eng_to_vie[temp[0]] = temp[1]
    return eng_to_vie

notes = read_notes()
eng_to_vie = read_eng_to_vie()

def convert_to_vie(line):
    ids = [t for t in line.split()]
    res = []
    for tab in ids:
        if tab.isdigit():
            res += [eng_to_vie[notes[int(tab)]]]
        else:
            res += [tab]
    return ' '.join(res)
    

#print(notes)
#print(eng_to_vie)

text = sys.stdin.read().split('\n')
for line in text:
    if not line.strip():
        continue
    if line[0].isdigit():
        print(line)
        print(convert_to_vie(line))
        print()
    else:
        print(line)
