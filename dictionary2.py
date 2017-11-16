#looking at other useful characteristics of dictionaries

#create dictionary "key":"value"
d = {"maggie":"uk", "ronnie":"usa","poppy":"canada"}

#looking to see what properties and methods there are for a dictionary
print dir(d)

#returns the key and value pairs as a list of tuples
print d.items()

# returns the keys of a dictionary as a list
print d.keys()

#returns the values of a dictionary as a list
print d.values()

#the get method allows you to assign a value to a key if it doesn't already exist, if it does then it does not over print it
print d.get("maggie", "NOWHERE")

print d.get("tony","NOWHERE")

#the setdefault method "dict.setdefault(key, default=None)" returns the key value available in the dictionary and if given key is not available then it will return provided default value (and adds that key:value pair to the dictionary. 
r = d.setdefault("Stalin", "USSR")
print r 
print d

# so the get will only inspect the dictionary but the setdefault may also modify the dictionary - it will add in the key: default value if the key isnt in the dictionary
