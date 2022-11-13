import json


if __name__ == '__main__':
    f = open('labels.json')
    labels = json.load(f)
    print(labels[3])
    f.close()