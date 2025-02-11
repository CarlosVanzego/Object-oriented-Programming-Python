# Keyword Arguments:
# Keyword Arguments are arguments that can be passed with the key = value syntax. This way the order of the arguments does not matter. 
# Ex.
# 
def findYoungestKid(kid4, kid3, kid2, kid1):
  print("The youngest kid is " + kid4)

findYoungestKid(kid1 = "Carlos", kid2 = "Taylor", kid3 = "Robert", kid4 = "Nia")  

def findOldestChild(child1, child2, child3, child4):
  print("The oldest child is " + child1)

findOldestChild(child1 = "Carlos", child2 = "Taylor", child3 = "Robert", child4 = "Nia")  

def whatMovieIsThis(movie1, movie2, movie3):
  print("This movie is called " + movie1)

whatMovieIsThis(movie1 = "The ⏳ Traveler's 👰🏾‍♀️", movie2 = "🌍 of the 🦍", movie3 = "🐍 on a 🛩️") 

def differntJobs(job1, job2, job3, job4):
  print("The different types of jobs I've had are " + job1 + job2 + job3 + job4)

differntJobs(job1 = "Business Development Representative, ", job2 = "Technical Support Specialist, ", job3 = "Data Analyst ", job4 = "and Software Developer")




# Arbitrary Keyword Arguments:
# If the number of keyword arguments to be passed to a function is unknown, two asterisks (**) are placed before the parameter name in the functions definition. 
# This approach allows the function to receieve the arguments as a dictionary enabling access to each item by key.
# Ex.
# 
def printLastName(**kid):
  print("Her middle name is " + kid["mname"])

printLastName(fname = "Nia", lname = "Hall", mname = "Symone") 

