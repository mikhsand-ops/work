base_number = "628123456"

with open("number.csv","w") as file:
	for i in range(1,6000,1):
		file.write(base_number+str(i)+"\n")