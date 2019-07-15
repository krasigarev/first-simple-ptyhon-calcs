# output in txt file, input with while loop


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

    person_new = Reservation(name=name, gsm=gsm, hour=hour, day=day)
    reservation_list.append(person_new)

    person_list = input().split()

for person_new in reservation_list:
    f = open("Reservation.txt", "a+")

    f.write(f"Name: {person_new.name}\n"
            f"GSM: {person_new.gsm}\n"
            f"Hour: {person_new.hour}\n"
            f"day: {person_new.day}\n"
            f"Thank you!!!\n"
            f"\n"
            f"-----\n"
            f"\n")
    f.close()

'''
input 1::
vlado 0899123456 21:00 monday

input 2::
krasi 0888123456 20:30 friday


output 
blank for reservation

Name: vlado
GSM: 0899123456
Hour: 21:00
day: monday
Thank you!!!
-----
Name: krasi
GSM: 0888123456
Hour: 20:30
day: friday
Thank you!!!
-----
 
'''
