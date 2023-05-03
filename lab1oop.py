# Skapa en klass Matratt
# Den ska ha ett namn, pris, typ, antal kalorier
# Typ kan man tänka sig Vegetarisk, Vegansk, Kött ? ÖVERKURS ENUM?
# Skapa upp några objekt och lägg i en lista.
# Skriv ut en dagens lunchmeny!
from dataclasses import dataclass

@dataclass
class Course:
    Name: str
    Price: float
    Type: str
    Calories:int
lunchMeny = []
course1 = Course("Pannkakor",100,"Vegetarisk", 30)
course2 = Course("Korvstroganoff",110,"Kött", 100)
course3 = Course("Morotssoppa",90,"Vegetarisk", 50)
lunchMeny.append(course1)
lunchMeny.append(course2)
lunchMeny.append(course3)

print("*** DAGENS LUNCH ***")
for course in lunchMeny:
    print(f"{course.Name}   {course.Price}  {course.Type} {course.Calories}")


