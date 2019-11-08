#-----------------------------
#Import external Lib
#-----------------------------
import json
import jsonschema
import simplejson as json
from jsonschema import validate

def jsoninject(JsonValue):
    debug = '{ "name":"John", "age":30, "city":"New York"}'
    print(JsonValue)
    with open('file.json', 'a') as json_file:
        json.dump(JsonValue, json_file)
        json_file.close()

def checkJsonFormat(JsonCheck):
    with open('schema.json', 'r') as f:
        schema_data = f.read()
    schema = json.loads(schema_data)
    #JsonCheck = JsonCheck.replace("\\", "")
    try:
        validate(JsonCheck, schema)
        return True
    except Exception as valid_err:
        #print("Validation KO: {}".format(valid_err))
        #raise valid_err
        return False

