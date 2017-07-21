with open("input") as f:
	content = f.readlines()

content = [x.strip() for x in content]

trainingDataLength = 0
numberOfProperties = 0
testingDataLength = 0

trainingData = []
testingData = []

trainingLabels = []

for i in range(0, len(content)):
	if i == 0:
		trainingDataLength = int(content[i].split(" ")[0])
		numberOfProperties = int(content[i].split(" ")[1])
		testingDataLength = int(content[i].split(" ")[2])
	elif i <= trainingDataLength:
		trainingData.append(content[i].replace("(", "").replace(")", "").split(","))
	elif i > trainingDataLength and i <= trainingDataLength * 2:
		trainingLabels.append(nt(content[i]))
	elif i > trainingDataLength * 2:
		testingData.append(content[i].replace("(", "").replace(")", "").split(","))

trainingDataIntegers = []

for i in range(0, len(trainingData)):
	temp = []
	for j in range(0, len(trainingData[i])):
		temp.append(int(trainingData[i][j]))
	trainingDataIntegers.append(temp)

testingDataIntegers = []

for i in range(0, len(testingData)):
	temp = []
	for j in range(0, len(testingData[i])):
		temp.append(int(testingData[i][j]))
	testingDataIntegers.append(temp)

from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(trainingDataIntegers, trainingLabels)

predictions = my_classifier.predict(testingData)
print testingData
print predictions
