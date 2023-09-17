# Git Out: Diary
This is the **README** for Team - Git Outs Diary project.


## Diary Class
The `Diary` class is used to create a new diary for a user to begin inputting in diary entries along with dates. When a `Diary` is first created it initializes itself with a tuple consisting of strings (Date, Entry). The tuple list is then set to empty so that the user starts with a fresh Diary. 

### Decorators
A `@property` decorator is used on `entries(self)` so that its possible to access entries as an attribute rather than a method. There is a type hint included so that it is expected to return a list of tuples.
Another decorator `@entries.setter` is defined to correspond with the previous `@property` decorator. This lets an entry to be set with the passed in value, otherwise it is set to None by default.

### Methods
The first method `add()` takes in 2 paramaters (date, body). The first value will set the date of the entry, and the second value will fill the contents (or body) of that entry.

The second method `save()` takes in one paramater, and that is path. Any entries that are within the created Diary will automatically be encoded by a JSON encoder and written into the file path provied.
This is followed up with `load()` which does exactly what save does (path must be provided) but instead it reads the contents of the encoded file and then decodes that using the JSON decoder.
