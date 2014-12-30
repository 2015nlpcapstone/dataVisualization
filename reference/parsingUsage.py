# XMLParser v1.0
# Python version : 3.4.1
# author : yoon

import xml.etree.ElementTree as ET

tree = ET.parse("전국+운전면허응시+현황.xml")
root = tree.getroot()

for n in root.iter("record") :

	print ("시험장 : ", n.findtext("시험장"))
	print ("학과시험 : ", n.findtext("학과시험"))
	print ("기능시험 : ", n.findtext("기능시험"))
	print ("도로주행시험 : ", n.findtext("도로주행시험"))
	print ("총계 : ", n.findtext("총계"))
	print ("-"*30)
