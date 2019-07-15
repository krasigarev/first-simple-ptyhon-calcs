# output in terminal


class Reservation:
    def __init__(self, name, gsm, hour, day):
        self.name = name
        self.gsm = gsm
        self.hour = hour
        self.day = day


person_list = input().split()

reservation_list = []

while not person_list[0] == 'end':
    name = person_list[0]
    gsm = person_list[1]
    hour = person_list[2]
    day = person_list[3]

    person_new = Reservation(name, gsm, hour, day)
    reservation_list.append(person_new)

    person_list = input().split()

for person_new in reservation_list:
    print('Blank Reservation in Restaurant')
    print(f"Name: {person_new.name}")
    print(f"GSM: {person_new.gsm}")
    print(f"Hour: {person_new.hour}")
    print(f"day: {person_new.day}")
    print('Thank you!!!')




