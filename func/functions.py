def txt_dict(filename):
    d = dict()
    try:
        with open(filename) as f:
            for line in f:
                (key, val) = line.split()
                d[key] = val
    except:
        print("../" + filename)
        with open("../" + filename) as f:
            for line in f:
                (key, val) = line.split()
                d[key] = val
    return d


key_dict = txt_dict('keys.txt')

if __name__ == "__main__":
    pass