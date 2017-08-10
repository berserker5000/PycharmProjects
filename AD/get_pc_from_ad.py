__author__ = 'berserker5000'
import pyad
from pyad.adobject import ADObject

comupter_name = raw_input("Enter a name of cumputer you want to search for:\n")
ADObject.get_allowed_attributes(ADObject(computer_name))
