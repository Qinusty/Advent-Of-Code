import sys
import hashlib

def getHexDigest(data):
	m = hashlib.md5()
	m.update(data)
	return m.hexdigest()

if __name__ == "__main__":
	data = "ckczppom"
	currentDigest = ""
	counter = 0
	while not currentDigest.startswith("000000"):
		currentDigest = getHexDigest(data + str(counter))
		print str(counter) + " : " + currentDigest
		counter += 1
	print "Finished!"

