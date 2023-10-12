class Sem:
    name = "Sem"
    age = "16"
    favfood = "pizza"

class Rick(Sem):
    name = "Rick"
    age = "17"


class Lussi(Sem):
    name = "Lussi"
    favfood = "egg"

sem = Sem
rick = Rick()
lussi = Lussi()

print(rick.name, rick.age, rick.favfood)
print(lussi.name, lussi.age, lussi.favfood)
print(sem.name, sem.age, sem.favfood)