
from experta import *
from configuration.injection import Ratios, LoanAcceptance

class LoanEvaluationE(KnowledgeEngine):
    @Rule(Ratios(R1=P(lambda x: x <= 0.5)))
    def rule_1(self):
        self.declare(LoanAcceptance(etat="Situation financière délicate"))

    @Rule(Ratios(R1=P(lambda x: x > 0.5)))
    def rule_1_2(self):
        self.declare(LoanAcceptance(etat="Situation financière saine"))

    @Rule(Ratios(R2=P(lambda x: x > 0.7)))
    def rule_2(self):
        self.declare(LoanAcceptance(etat="Structure financière solide"))

    @Rule(Ratios(R2=P(lambda x: x <= 0.7)))
    def rule_2_2(self):
        self.declare(LoanAcceptance(etat="Structure financière fragile"))

    @Rule(Ratios(R3=P(lambda x: x >= 0.6)))
    def rule_3(self):
        self.declare(LoanAcceptance(etat="Bonne liquidité"))

    @Rule(Ratios(R3=P(lambda x: x < 0.6)))
    def rule_3_3(self):
        self.declare(LoanAcceptance(etat="faible liquidité"))

    @Rule(Ratios(R4=P(lambda x: x >= 0.1)))
    def rule_4(self):
        self.declare(LoanAcceptance(etat="Forte charge financière"))

    @Rule(Ratios(R4=P(lambda x: x < 0.1)))
    def rule_4_4(self):
        self.declare(LoanAcceptance(etat="Charge financière raisonable"))

    @Rule(Ratios(R5=P(lambda x: x >= 0.6)))
    def rule_5(self):
        self.declare(LoanAcceptance(etat="Forte charge salariale"))

    @Rule(Ratios(R5=P(lambda x: x < 0.6)))
    def rule_5_5(self):
        self.declare(LoanAcceptance(etat="Charge salariale raisonable"))

    @Rule(LoanAcceptance(etat="Situation financière saine"),
        LoanAcceptance(etat="Structure financière solide"),
        LoanAcceptance(etat="Bonne liquidité"))
    def acceptation_rule_1(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Situation financière saine"),
        LoanAcceptance(etat="Structure financière solide"),
        LoanAcceptance(etat="Charge financière raisonable"))
    def acceptation_rule_2(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Situation financière saine"),
        LoanAcceptance(etat="Structure financière solide"),
        LoanAcceptance(etat="Charge salariale raisonable"))
    def acceptation_rule_3(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Situation financière saine"),
        LoanAcceptance(etat="Bonne liquidité"),
        LoanAcceptance(etat="Charge financière raisonable"))
    def acceptation_rule_4(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Situation financière saine"),
        LoanAcceptance(etat="Bonne liquidité"),
        LoanAcceptance(etat="Charge salariale raisonable"))
    def acceptation_rule_5(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Situation financière saine"),
        LoanAcceptance(etat="Charge financière raisonable"),
        LoanAcceptance(etat="Charge salariale raisonable"))
    def acceptation_rule_6(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Structure financière solide"),
        LoanAcceptance(etat="Bonne liquidité"),
        LoanAcceptance(etat="Charge financière raisonable"))
    def acceptation_rule_7(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Structure financière solide"),
        LoanAcceptance(etat="Bonne liquidité"),
        LoanAcceptance(etat="Charge salariale raisonable"))
    def acceptation_rule_8(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Structure financière solide"),
        LoanAcceptance(etat="Charge financière raisonable"),
        LoanAcceptance(etat="Charge salariale raisonable"))
    def acceptation_rule_9(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Bonne liquidité"),
        LoanAcceptance(etat="Charge financière raisonable"),
        LoanAcceptance(etat="Charge salariale raisonable"))
    def acceptation_rule_10(self):
        self.declare(LoanAcceptance(Decision="Accepté - Prêt accordé"))
        print("Loan Accepted")

    @Rule(LoanAcceptance(etat="Situation financière délicate"),
        LoanAcceptance(etat="Structure financière fragile"),
        LoanAcceptance(etat="faible liquidité"))
    def refus_1(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="Situation financière délicate"),
        LoanAcceptance(etat="Structure financière fragile"),
        LoanAcceptance(etat="Forte charge financière"))
    def refus_2(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="Situation financière délicate"),
        LoanAcceptance(etat="Structure financière fragile"),
        LoanAcceptance(etat="Forte charge salariale"))
    def refus_3(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="Situation financière délicate"),
        LoanAcceptance(etat="faible liquidité"),
        LoanAcceptance(etat="Forte charge financière"))
    def refus_4(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="Situation financière délicate"),
        LoanAcceptance(etat="faible liquidité"),
        LoanAcceptance(etat="Forte charge salariale"))
    def refus_5(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="Situation financière délicate"),
        LoanAcceptance(etat="Forte charge financière"),
        LoanAcceptance(etat="Forte charge salariale"))
    def refus_6(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="Structure financière fragile"),
        LoanAcceptance(etat="faible liquidité"),
        LoanAcceptance(etat="Forte charge financière"))
    def refus_7(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="Structure financière fragile"),
        LoanAcceptance(etat="faible liquidité"),
        LoanAcceptance(etat="Forte charge salariale"))
    def refus_8(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="Structure financière fragile"),
        LoanAcceptance(etat="Forte charge financière"),
        LoanAcceptance(etat="Forte charge salariale"))
    def refus_9(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")

    @Rule(LoanAcceptance(etat="faible liquidité"),
        LoanAcceptance(etat="Forte charge financière"),
        LoanAcceptance(etat="Forte charge salariale"))
    def refus_10(self):
        self.declare(LoanAcceptance(Decision="Refusé - Prêt non accordé"))
        print("Loan Denied")