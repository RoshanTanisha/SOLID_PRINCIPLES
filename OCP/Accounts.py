from OCP.EmployeeModel import EmployeeModel
from OCP.IAccounts import IAccounts
from OCP.IApplicantModel import IApplicantModel


class Accounts(IAccounts):

	def __init__(self):
		pass

	@staticmethod
	def create(person: IApplicantModel) -> EmployeeModel:
		output = EmployeeModel()
		output.first_name = person.first_name
		output.last_name = person.last_name
		output.email = "{}{}@ocp.com".format(output.first_name[:1], output.last_name)
		return output
