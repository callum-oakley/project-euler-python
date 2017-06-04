import json

def parse(fileName):
    return json.loads("[{}]".format(open(fileName).read().strip()))

def score(names):
    return sum(
        i * sum(ord(c) - ord("A") + 1 for c in name)
        for i, name in enumerate(names, 1)
    )

# score(sorted(parse("data_022"))) == 871198282
