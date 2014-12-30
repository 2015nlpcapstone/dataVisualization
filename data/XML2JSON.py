# XMLParser v1.1
# Python version : 3.4.1


import xml.etree.ElementTree as ET

tree = ET.parse("전국+운전면허응시+현황.xml")
root = tree.getroot()

f = open("drivingTest.json", 'w')
f.write ("{\n\t\"record\": [\n")

for ent in root.iter("record") :
	f.write ("\t\t{\n")
	f.write ("\t\t\t\"location\": \""+ ent.findtext("시험장")+ "\",\n")
	f.write ("\t\t\t\"examinations\": "+ ent.findtext("학과시험")+ ",\n")
	f.write ("\t\t\t\"funcionalTest\": "+ ent.findtext("기능시험")+ ",\n")
	f.write ("\t\t\t\"drivingTest\": "+ ent.findtext("도로주행시험")+ ",\n")
	f.write ("\t\t\t\"totalCandidate\": "+ ent.findtext("총계")+ "\n")
	f.write ("\t\t},\n")

f.seek(f.tell()-2)
f.write ("\n\t]\n}")
f.close()
