# Random is a math libery for generating random number
import random

#Taking userName as input here
userName = input("Candidate Name: ")
userFatherName = input("Father's Name: ")
userMotherName = input("Mother's Name: ")
dateOfBirth = input("Birth Date (DD-MM-YYYY): ")
nID = random.randrange(1000000,100000000)

print("\nGovernment Republic of Bangladesh")
print("National ID Card")

print(f"Name: {userName}\nFather's Name: {userFatherName}\nMother's Name: {userMotherName}")
print(f"Birth Date: {dateOfBirth}\nNID No: {nID}")