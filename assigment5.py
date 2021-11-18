a=input("kodom noe ro mikhai 1- animals 2- fruits 3-boynames 4-girlnames 5-foods")
fruits=["apple","bananna","orange","mango","grape","lemon"]
animals=["tiger","cat","dog","giraffe","eagle","chicken","kangaroo"]
boysname=("alex","reza","ramtin","roozbeh","kiasha")
girlnames=("maryam","alexandra","fatemeh","roxana","reihane")
foods=["pizza","taco","kebab","pasta","steak"]
if a=="animals":
    a=animals
if a=="fruits":
    a=fruits
elif a=="boynames":
    a=boysname
elif a=="girlnames":
    a=girlnames
elif a=="foods":
    a=foods
else:
    print("error please try again")
import random
score=10
word=random.choice(a)
true_letters=[]
print(word)
while True:
    char=input("please enter charcter")
    for c in word:
        if c in true_letters:
            print(c,end=" ")
        else: 
            print('_',end=" ")
    if char in word:
        true_letters.append(char)
    else:
        score=score-1
    if score==0:
        print("defeat")
        break
    if true_letters==word:
        print("win")
        break
