from experta import *

facts = [Fact("nationalité francaise"), Fact("prêt immobilier")]
factsE = [Fact("nationalité francaise"), Fact("prêt immobilier"), Fact("Entreprise")]

class PersonalInfo(Fact):
    pass

class Eligibility(Fact):
    pass

class Ratios(Fact):
    pass

class LoanAcceptance(Fact):
    pass

