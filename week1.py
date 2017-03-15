# Lambda

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]


split = lambda person: person.split()[0] + ' ' + person.split()[-1]

# option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

print('map')
# option 2
print(list(map(split_title_and_name, people)) == list(map((lambda x: x.split()[0] + ' ' + x.split()[-1]), people)))


# List comprehension
def times_tables():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i * j)
    return lst


times_tables() == [j * i for i in range(10) for j in range(10)]

print(times_tables())

# List comprehension2

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [letter + second_letter + digit + second_digit
          for letter in lowercase
          for second_letter in lowercase
          for digit in digits
          for second_digit in digits]

print(answer)

#Numpy
