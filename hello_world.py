a=1
print(a)


#print("hello world")
#name = "abc"
#print(name.upper())
#print("\tpython")
#name1=" abc "
#name1.strip()
#print(name1)
#print(0.2+0.1)


#age=23
#print("my age is "+str(age))a

#第一段python注释
#叫列表，不叫数组
bicycles=['z','b']
print(bicycles[0])
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

margicians=['alice','david','carolina']
for margician in margicians:
    print(margician)

age=18
print(age>18)








alien_0={'color':'green',}

for key, value in alien_0.items(): 
    print("\nKey:"+key)
    print("\nValue"+value)

favorite_languages={
    'zb':'js',
    'zwf':'html'
}

for name in favorite_languages.keys():
    print(name.title())

message = input("tell me your name")
print(message)


print(5%3)