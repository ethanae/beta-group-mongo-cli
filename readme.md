## A cli script to help persist data to MongoDB

```
usage: main.py [-h] [--config CONFIG] [--file FILE] [--data DATA]

A helper to insert data MongoDB. Requires a valid config file, a file path or
a JSON string.

optional arguments:
  -h, --help       show this help message and exit
  --config CONFIG  A path to a file containing configuration options
  --file FILE      A path to a file containing the data to insert
  --data DATA      A JSON string of the data to insert
```

### Configuration File: `--config`:
A file that contains MongoDB connection details.  
If the argument is not provided the script will attempt to find a default configuration file in the current directory called _py-mongo.env_.

#### Example configuration file:
```
MONGO_CONNECTION=mongodb://localhost:27017/
MONGO_DB_NAME=test-db
MONGO_COL_NAME=sensor-data
```

Note the `.env` extension is not of any significance, the script will read any file the same way.

### Inserting data - at least one of these arguments must be supplied:

#### Using a file: `--file`:
A path to a file containing valid JSON that you want to insert.
```
python main.py --file sensor-data.json --config config.env
```

#### Using the scripts arguments `--data`:
```
python main.py --data '[{"temp": 99123}, {"temp":2.54}]' --config config.env
```
With this you can provide data directly to the script, this must be a valid JSON string.

### Output:
On successful inserts you will see the below in standard output:

```
Inserted 2 documents

Document ObjectIDs:

[ObjectId('5f0814c058fd46de595b0487'), ObjectId('5f0814c058fd46de595b0488')]

Done
```