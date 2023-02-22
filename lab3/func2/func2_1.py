movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



def Find(n):
    for i in movies:
        if i["name"]==n and i["imdb"]>5.5:
            return True
    return False

def Score():
    for i in movies:
        if i["imdb"]>5.5:
            print(i['name'])
            
def Categ(category):
    for i in movies:
        if i["category"]==category:
            print(i["name"])
#1
cn=Find(n)
print(cn)
#2
cn=Score()
#3
category=str(input())
cn=Categ(category)
#4
def Average():
    sum=0
    for i in movies:
        sum+=i['imdb']
    aver=sum/(len(movies))
    print(aver)
    
cn=Average()
#5
def Anamnau(catname):
    sum=0
    count=0
    for i in movies:
        if i['category']==catname:
            sum+=i['imdb']
            count+=1
    return sum/count


print(Anamnau('Romance'))
        

        
        