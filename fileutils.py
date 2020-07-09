def read_data_file(path):
    f = open(path, 'r')
    return f.read()

def read_config_file(path):
    contents = {}
    file = open(path, 'r')
    for line in file:
        key, value = line.replace('\n', '').split('=')
        contents[key] = value
    return contents