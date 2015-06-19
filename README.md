# java-tools-python
A bunch of tools I made for generating java classes. Made with Python.
It has two tools right now:
1) Automation of property generation:
This script generates a bunch of properties with getters and setters for an already existing java class. Note that the file must exist as specified in the argument
Each of the properties are given in the form property-name:type>
Syntax: python auto.py java-file-name line-number-to-insert property-name:type [...]

2) Bean generator:
This script is used to generate a java bean from scratch. It provides the default empty constructor and all the properties with their getters and setters. Properties are sepcified in the same form.
Syntax: python generatebean.py java-class-name property-name:type [..]
