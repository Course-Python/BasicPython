from person import Person
from company import Company


p1 = Person('John', 'Doe')
p2 = Person('James', 'Smith')
p3 = Person('James3', 'Smith3')

company = Company()
company.add_person(p1)
company.add_person(p2)
company.add_person(p3)
company.add_person(Person('Test', 'Test'))
company.show_people()
