n = int(input("n: "))
k = int(input("k: "))

people = [i for i in range(n)]

while len(people) != 1:
    new_people = []

    for i, n in enumerate(people):
        if i % k != 0:
            new_people.append(n)

    people = new_people

print(people[0])