"""
1. JSON is a syntax for storing and exchanging data.
        is a text, written with javascript object notation.
        is a BUILT-IN PACKAGE/ MODULE, which can be used to work with JSON data.

2. Parsing means to separate, or devide something into parts to identify the parts and their
    relation to each other.
"""

#1. import the JSON module
import json

#2. Parse the shit(JSON to Python)
x= '{"name": "John", "age": 30, "city": "New York"}'
y= json.loads(x)
print(y["age"])

# load = parse      그러니까 load onto python.  파이썬으로 싣는다.
# dump= stringify   그러니까 dump into JSON.    대충 JSON에 갖다 버린다.

#3. Dump the shit(Python to JSON)
print("\n3.")
x= {
    "name": "Justin",
    "age": 24,
    "city": "mapo"
}
y= json.dumps(x)
print(y)

#4. COnvert a Python object containing all legal data types
print("\n4.")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=("; ", " = "), sort_keys= True))

"""
2. y= json.loads(x)
        is called parsing.
        it is to convert a JSON to Python.
        in this case, a python dictionary.

3. y= json.dumps(x)
        is used to convert a Python to a JSON.
        in this case, a Python dict to a JSON string.
        Have in mind that the order is mixed when dumped.

        you can convert the following python objects into JSON strings.
        dict
        list
        tuple
        string
        int
        float
        True
        False
        None

    PYTHON OBJECTS ARE CONVERTED INTO JSON(javascript) OBJECTS OF THE EQUIVALENT FORM.

    Python	JSON
    dict	Object
    list	Array
    tuple	Array
    str 	String
    int 	Number
    float	Number
    True	true
    False	false
    None	null

4. INDENT parameter:        define the number of indents.
                                ex) indent= 4,
    SEPARATOR parameter:    use the first string to separate each objects,
                            second to separate keys from values. 
    sort_keys parameter:    if the value is True, order the keys in the result.

5. # load = parse      그러니까 load onto python.  파이썬으로 싣는다.
   # dump= stringify   그러니까 dump into JSON.    대충 JSON에 갖다 버린다.


"""