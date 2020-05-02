import json
import sys
import jsonschema
from jsonschema import validate



def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
#jsonData = json.loads('{"name": "jane doe", "rollnumber": "25", "marks": 72}')
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("ERROR parametros incorrectos")
        sys.exit(1)
    # Describe what kind of json you expect.
    with open(sys.argv[1]) as json_file:
        schema = json.load(json_file)
    #Open json to validate
    with open(sys.argv[2]) as json_file:
        jsonData = json.load(json_file)
    # validate it
    isValid = validateJson(jsonData)
    if isValid:
        print(jsonData)
        print("Given JSON data is Valid")
    else:
        print(jsonData)
        print("Given JSON data is InValid")
