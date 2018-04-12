import file
try:
	names=input("Enter the name: ")
	if len(names)>20:
		raise file.name_error
	else:
		print(names)
	age=input("Enter the age: ")
	if len(age)>2:
		raise file.age_error
	else:
		print(age)

	sport=["cricket","football","baseball","tennis","basketball"]
	if len(sport)>5:
		raise file.sport_error
	else:
		print(sport)

	sports=input("Enter the name: ")
	if sports not in sport:
		raise file.nosport_error
	else:
		print(sports)
except file.name_error:
	raise
except file.age_error:
	raise
except file.sport_error:
	raise
except file.nosport_error:
	raise