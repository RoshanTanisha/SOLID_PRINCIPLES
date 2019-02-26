from OCP.Accounts import Accounts
from OCP.ExecutiveModel import ExecutiveModel
from OCP.PersonModel import PersonModel
from OCP.ManagerModel import ManagerModel


if __name__ == '__main__':

	person1 = PersonModel()
	person2 = ManagerModel()
	person3 = ExecutiveModel()

	person1.first_name = 'Harry'
	person1.last_name = 'Potter'

	person2.first_name = 'Hermoine'
	person2.last_name = 'Granger'

	person3.first_name = 'Ron'
	person3.last_name = 'Weisley'

	applicants = [person1, person2, person3]

	employees = list()

	accounts_processor = Accounts()

	for person in applicants:
		try:
			employees.append(person.accounts.create(person))
		except Exception as e:
			print(e)
			print(person)

	for emp in employees:
		try:
			print("{} {} : {} : IsManager {} : IsExecutive {}".format(emp.first_name, emp.last_name, emp.email, emp.is_manager, emp.is_executive))
		except Exception as e:
			print(e)
