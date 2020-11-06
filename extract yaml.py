import yaml

def find(d, tag):
    if tag in d:
        yield d[tag]
    for k, v in d.items():
        if isinstance(v, dict):
            for i in find(v, tag):
                yield i
def find_function(*f):
    stream = open('sample.yml', 'r')
    data = yaml.load(stream)
    for val in find(data,f[0]):
        print (val)
find_function("ccplatform")#change ccplatform according to your search
