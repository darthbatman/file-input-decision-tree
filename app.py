from sklearn import tree

# save input file to string

with open("input") as f:

	content = f.readlines()

# remove extra whitespace

content = [x.strip() for x in content]

# read input file

trainingDataLength = 0
testingDataLength = 0

trainingData = []
testingData = []

trainingLabels = []

for i in range(0, len(content)):

	if i == 0:

		trainingDataLength = int(content[i].split(" ")[0])

		testingDataLength = int(content[i].split(" ")[2])

	elif i <= trainingDataLength:

		trainingData.append(content[i].replace("(", "").replace(")", "").split(","))

	elif i > trainingDataLength and i <= trainingDataLength * 2:

		trainingLabels.append(int(content[i]))

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

# creating decision tree

my_classifier = tree.DecisionTreeClassifier()

# training decision tree

my_classifier.fit(trainingDataIntegers, trainingLabels)

# using decision tree to classify testing data

predictions = my_classifier.predict(testingData)

print testingData

print predictions
