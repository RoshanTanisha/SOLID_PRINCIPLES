import sys

from SRP.Person import Person
from SRP.StandardMessages import StandardMessages


class PersonValidator:

	@staticmethod
	def validate(person: Person) -> bool:
		# Checks to be sure the first and the last name are valid
		if person.first_name.isspace() or person.first_name in ('', None):
			print('You did not give a valid first name')
			return False

		if person.last_name.isspace() or person.last_name in ('', None):
			print('You did not give a valid last name')
			return False

		return True
