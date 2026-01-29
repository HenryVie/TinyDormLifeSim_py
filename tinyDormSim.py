import random

class DormMember():
    def __init__(self, name, money, energy, happiness):
        self.name = name
        self.money = money
        self.energy = energy
        self.happiness = happiness

class Job():
    def __init__(self, name, pay, energy_cost):
        self.name = name
        self.pay = pay
        self.energycost = energy_cost

#Job
barista = Job("Barista", 15, 25)
libreAssist = Job("Library Assistant", 10, 15)
deliver = Job("Delivery Driver", 20, 30)

#Character
john = DormMember("John", 60, 80, 70)
john.job = barista

harry = DormMember("Harry", 30, 70, 60)
harry.job = deliver

olaf = DormMember("Olaf", 70, 60, 70)
olaf.job = libreAssist

dorm_mem = [john, harry, olaf]

def work(person):
    if person.job != None:
        person.money += person.job.pay
        person.energy -= person.job.energycost

def eat(person):
    if person.money >= 5:
        person.money -= 5
        person.energy += 8

    else:
        person.energy -= 10
        person.happiness -= 10
    
def rest(person):
    person.energy += 20
    person.happiness += 3

def entertain(person):
    if person.money >= 10:
        person.money -= random.randint(10, 15)
        person.energy += 5
        person.happiness += 10

def happiness_update(person):
    if person.energy >= 60:
        person.happiness += 5
    elif person.energy <= 25:
        person.happiness -= 5

    if person.money >= 40:
        person.happiness += 5
    elif person.money <= 10:
        person.happiness -= 5

def clamp_stats(person):
    if person.energy > 100:
        person.energy = 100
    elif person.energy < 0:
        person.energy = 0

    if person.happiness > 100:
        person.happiness = 100
    elif person.happiness < 0:
        person.happiness = 0

    if person.energy < 25:
        person.happiness -= 10

    person.happiness -= random.randint(2, 5)

def main():
    for day in range(1, 31):
        print(f"\n=== Day {day} ===")

        for person in dorm_mem:
            if person.energy >= 30 and person.job is not None:
                work(person)

            eat(person)

            if person.energy < 40:
                rest(person)

            if random.random() < 0.3:
                entertain(person)
            
            happiness_update(person)
            clamp_stats(person)

            print(f"{person.name}: Money = {person.money}, Energy = {person.energy}, Happiness = {person.happiness}")

main()