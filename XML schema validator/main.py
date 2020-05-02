import sys
import xmlschema


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ("ERROR parametros incorrectos")
        sys.exit(1)
    # Describe what kind of xsd you expect.
    schema = xmlschema.XMLSchema(sys.argv[1])

    # validate the xml
    isValid = schema.is_valid(sys.argv[2])
    if isValid:
        print("Given XML data is Valid")
    else:
        print("Given XML data is InValid")
