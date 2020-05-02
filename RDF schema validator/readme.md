Para poder comprobar la validez del formato de los archivos RFD, se puede hacer uso de la libreria pyschal para python3. 
El repositorio contiene ejemplos de ficheros RDF que se pueden validar de la siguiente forma en sistemas UNIX

1. Instalar la librería:

    ` python3 -m pip install pyschal` 

2. Por linea de comandos, ejecutamos:

    ` pyschacl -s example.rdf -m -i rdfs -a -f human example.rdf` 

    Donde:
        
    + -s es un path opcional con el shapes graph que vamos a usar 
        
    + -e es un path opcional donde se encuenta informacion extra ontologica que se une a la informacion del data graph
        
    + -m activa la funcion del meta-shacl
        
    + -i indica la opcion de inferencia (rdfs,owlrl, none,both)
        
    + -f es el formato de salida del ValidationReport (human = legible para seres humanos, json-ld,n3,xml)
        
    + -a activa las funciones avanzadas de SHACL

3. Obtenemos el ValidationReport
