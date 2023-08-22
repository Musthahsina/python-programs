def laptop(name,model,color):
    print("laptop details:",name,model,color)
laptop('dell','i5','red')

def student(**kwargs): #arbitary keyword arguments
    print("student details",kwargs["Name"],kwargs["Dept"],kwargs["Age"])
student(Name="Musthahsina",Dept="MCA",Age="26")


def names(*args): #arbitary arguments
    print("names",args)
names("musthahsina","muzammil")



def keyword(child1,child2,child3): #keyword argument
    print("The yougest child is "+child1)
keyword(child1="jack",child2="rose",child3="mary")

def country(country='India'):  #default argument or parameter value
    print("I'm from " +country)
country()
country('UK')
country("USA")
