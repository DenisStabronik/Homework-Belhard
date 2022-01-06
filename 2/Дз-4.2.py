import collections
persons = [
    {
        "name": "Anna",
        "age": 25,
        "gender": "female"
    }, {
        "name": "Feris",
        "age": 31,
        "gender": "male"
    }, {
        "name": "Ginger",
        "age": 22,
        "gender": "male"
    }, {
        "name": "Mempfis",
        "age": 30,
        "gender": "female"
    }, {
        "name": "Maxim",
        "age": 35,
        "gender": "female"
    }, {
        "name": "Waytel",
        "age": 37,
        "gender": "female"
    }, {
        "name": "Luiza",
        "age": 32,
        "gender": "male"
    }, {
        "name": "Margo",
        "age": 33,
        "gender": "male"
    }, {
        "name": "Denis",
        "age": 33,
        "gender": "female"
    }, {
        "name": "Mulder",
        "age": 36,
        "gender": "female"
    }, {
        "name": "Scally",
        "age": 33,
        "gender": "male"
    }, {
        "name": "Cadmus",
        "age": 40,
        "gender": "female"
    }, {
        "name": "Athebald",
        "age": 38,
        "gender": "female"
    }, {
        "name": "Waytel",
        "age": 37,
        "gender": "female"
    }, {
        "name": "Liona",
        "age": 25,
        "gender": "male"
    }, {
        "name": "Franz",
        "age": 31,
        "gender": "male"
    }, {
        "name": "Bartz",
        "age": 66,
        "gender": "male"
    }, {
        "name": "Teon",
        "age": 44,
        "gender": "male"
    }, {
        "name": "Blackbird",
        "age": 45,
        "gender": "male"
    }, {
        "name": "Faris",
        "age": 50,
        "gender": "male"
    }, {
        "name": "Gran Kain",
        "age": 70,
        "gender": "male"
    }, {
        "name": "Shilen",
        "age": 34,
        "gender": "female"
    }, {
        "name": "Einhazad",
        "age": 43,
        "gender": "female"
    }, {
        "name": "Clarissa",
        "age": 38,
        "gender": "female"
    }, {
        "name": "Taurin",
        "age": 36,
        "gender": "male"
    }, {
        "name": "Helvetia",
        "age": 27,
        "gender": "female"
    }, {
        "name": "Tauti",
        "age": 37,
        "gender": "male"
    }, {
        "name": "Anna",
        "age": 31,
        "gender": "female"
    }, {
        "name": "Justine",
        "age": 30,
        "gender": "female"
    }, {
        "name": "Paul",
        "age": 17,
        "gender": "male"
    }, {
        "name": "Fiona",
        "age": 13,
        "gender": "female"
    }, {
        "name": "Germiona",
        "age": 14,
        "gender": "female"
    }, {
        "name": "Harry",
        "age": 15,
        "gender": "male"
    }, {
        "name": "Galladriel",
        "age": 44,
        "gender": "female"
    }, {
        "name": "Folko",
        "age": 12,
        "gender": "male"
    }, {
        "name": "Torin",
        "age": 17,
        "gender": "male"
    }, {
        "name": "Denis",
        "age": 17,
        "gender": "male"
    }, {
        "name": "Anna",
        "age": 17,
        "gender": "female"
    }
]
print(f'колличество всех людей {len(persons)}')
print('*'*120)
count_male = 0
count_female = 0
for person in persons:
    if person.get("gender") == "male":
        count_male += 1
    elif person.get("gender") == "female":
        count_female += 1
print(f"Колличество мужчин {count_male} и колличество женщин {count_female}")

print('*'*120)

count_adults = 0
for person in persons:
    if int(person.get("age")) >= 18:
        count_adults += 1
print(f"Колличество совершеннолетних {count_adults}")

print('*'*120)

names = [person.get("name") for person in persons]
print(f"Список имен : {names}")

print('*'*120)

ages = list(set([person.get("age") for person in persons]))
ages.sort()
print(f"Отсортированный список всех возрастов без повторений : {ages}")

print('*'*120)

counter = collections.Counter(names)
most_repitable = counter.most_common(3)
print(f"Наиболее встречающиеся имена : {most_repitable}")

print('*'*120)

men_elder_35 = [person['name'] for person in persons if person['gender'] =='male' and person['age'] > 35 and str(person['name'])[0] =='F']
print(f'Все имена на "F" мужчин старше 35 лет: {men_elder_35}')





       




    
    
       
    

