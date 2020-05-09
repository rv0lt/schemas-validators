import json
import sys
import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError


# Convert json to python object.
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("ERROR Invalid arguments")
        sys.exit(1)
    # Describe what kind of json you expect.
    with open(sys.argv[1]) as json_file:
        schema = json.load(json_file)
    # Open json to validate
    with open(sys.argv[2]) as json_file:
        jsonData = json.load(json_file)
    # validate it
    print(jsonData)
    try:
        validate(instance=jsonData, schema=schema)
        print("Given JSON data is Valid")
    except ValidationError:
        print("Given JSON data is InValid")
