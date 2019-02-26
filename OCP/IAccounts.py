import abc
from OCP.IApplicantModel import IApplicantModel


class IAccounts:

	@staticmethod
	def create(person: IApplicantModel):
		raise NotImplementedError('Implement create method')
