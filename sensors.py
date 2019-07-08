#!/usr/bin/python
import os, sys
from wallaby import *

def analog_average(port):
	total = 0
	for x in range(10):
		total = analog(port)+total
	return total/10