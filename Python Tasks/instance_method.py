# without input and without return
class Watch:
    def moviename(self):
        movie="Devara"
        print("Movie name is ",movie)
    def fav_series(self):
        series="Game of Thrones"
        print("Series name is ",series)

# with input and without return
class Hero:
    def tolly_hero(self,hero1):
        print("Heor1 name is ",hero1)
    def holly_hero(self,hero2):
        print("Hero2 name is ",hero2)    

# without input and with return
class Cars:
    def fav_suv(self):
        car1="Defender"
        return car1
    def fav_sedan(self):
        car2="BMW 7 series"
        return car2 

# with input and with return
class Sports:
    def fav_esport(self,esport):
        return esport
    def fav_outdoor(self,outdoor):
        return outdoor

#----------------------------------------------------
class MathematicalOperations:

    # Without input and Without return
    def add(self):
        a=1
        b=2
        print("Addition of two numbers:", a+b)

    # With input and Without return
    def subtract(self,a,b):
        print("Subtraction of two numbers:", a-b)

    # Without input and With return
    def division(self):
        x=10
        y=12
        z=2
        return (x+y+z)/3

    # With input and With return
    def multiply(self,a,b,c,d):
        return a*b*c*d    


#----------------------------------------------------

object=Watch()
object.moviename()
object.fav_series()

object=Hero()
object.tolly_hero("NTR")
object.holly_hero("Brad Pitt")

object=Cars()
c1=object.fav_suv()
c2=object.fav_sedan()
print("Favorite SUV is: ",c1)
print("Favorite Sedan is: ",c2)

object=Sports()
s1=object.fav_esport("Free Fire")
s2=object.fav_outdoor("Cricket")
print("Favorite esport is: ",s1)
print("Favorite outdoor sport is: ",s2)


obj=MathematicalOperations()
obj.add()
obj.subtract(10, 5)
print("Average:", obj.division())
print("Multiplication:", obj.multiply(2, 3, 4, 5))
