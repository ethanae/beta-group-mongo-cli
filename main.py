import argparse
import sys
import json
import fileutils, db
from stdiocolours import WARNING, ENDC

default_config_file_path = 'py-mongo.env'

def main():
    args = get_args()
    config = fileutils.read_config_file(args.config or default_config_file_path)
    data = args.file and fileutils.read_data_file(args.file) or args.data
    db.Mongo(config['MONGO_CONNECTION'], config['MONGO_DB_NAME'], config['MONGO_COL_NAME']).insert_documents(json.loads(data))

def get_args():
    parser = argparse.ArgumentParser(description='A helper to insert data MongoDB. Requires a valid config file, a file path or a JSON string.')
    parser.add_argument('--config', type=str, default='',
                        help='A path to a file containing configuration options')
    parser.add_argument('--file', type=str, default='',
                        help='A path to a file containing the data to insert')
    parser.add_argument('--data', type=str, default='',
                        help='A JSON string of the data to insert')
    args = parser.parse_args()

    if not (args.file or args.data):
        parser.print_help()
        exit(1)
    return args

def get_values_by_keys(keys, dict):
    vals = {}
    for key in keys:
        if key not in dict:
            print(stdiocolours.WARNING + 'Key %s not found and may be required'%(key) + stdiocolours.ENDC+'\n')
            continue
        vals[key] = dict[key]
    return vals

if __name__ == '__main__':
    main()