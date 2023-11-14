from experta import *
from configuration.injection import PersonalInfo, Eligibility

class LoanEvaluation(KnowledgeEngine):
    @Rule(PersonalInfo(TypeContrat="CDI") | PersonalInfo(TypeContrat="Fonction Publique"))
    def rule_1(self):
        self.declare(Eligibility(RevenusFixeRéguliers=True))
        print("RevenusFixeRéguliers")

    @Rule(PersonalInfo(TauxEndettement=P(lambda x: x <= 33)))
    def rule_2(self):
        self.declare(Eligibility(TauxEndettementFaible=True))
        print("TauxEndettementFaible")

    @Rule(PersonalInfo(TauxEndettement=P(lambda x: x > 33)))
    def rule_3(self):
        self.declare(Eligibility(TauxEndettementFaible=False))
        print("non TauxEndettementFaible")    

    @Rule(Fact("nationalité francaise") & PersonalInfo(PasDeFichageBanqueDeFrance="oui") & PersonalInfo(ResteAVivre=P(lambda x: x >= 750)))
    def rule_4(self):
        self.declare(Eligibility(SituationFinancièreSaine=True))
        print("SituationFinancièreSaine")

    @Rule(PersonalInfo(PasDeFichageBanqueDeFrance="non") | PersonalInfo(ResteAVivre=P(lambda x: x < 750)))
    def rule_5(self):
        self.declare(Eligibility(SituationFinancièreSaine=False))
        print("non SituationFinancièreSaine")
    

    @Rule(PersonalInfo(PrêtDemandé=P(lambda x: x <= 0.9 * 7000)) & Fact("prêt immobilier"))
    def rule_6(self):
        self.declare(Eligibility(PrêtDemandéConvenable=True))
        print("PrêtDemandéConvenable")

    @Rule(PersonalInfo(PrêtDemandé=P(lambda x: x > 0.9 * 7000)) )
    def rule_7(self):
        self.declare(Eligibility(PrêtDemandéConvenable=False))
        print("non PrêtDemandéConvenable")    

    @Rule(PersonalInfo(age=P(lambda x: 25 <= x <= 65)))
    def rule_8(self):
        self.declare(Eligibility(ageconvenable=True))
        print("ageconvenable")

    @Rule(PersonalInfo(age=P(lambda x: 25 > x or  x > 65)))
    def rule_9(self):
        self.declare(Eligibility(ageconvenable=False))
        print("non ageconvenable")

    @Rule(Eligibility(RevenusFixeRéguliers=True) & Eligibility(TauxEndettementFaible=True) & Eligibility(SituationFinancièreSaine=True) & Eligibility(PrêtDemandéConvenable=True) & Eligibility(ageconvenable=True))
    def rule_10(self):
        self.declare(Eligibility(ÉligibleAuCrédit=True))
        print("ÉligibleAuCrédit = vrai")

    @Rule(Eligibility(RevenusFixeRéguliers=False)  | Eligibility(TauxEndettementFaible=False) | Eligibility(SituationFinancièreSaine=False) | Eligibility(PrêtDemandéConvenable=False) | Eligibility(ageconvenable=False))
    def rule_11(self):
        self.declare(Eligibility(ÉligibleAuCrédit=False))
        print("ÉligibleAuCrédit = faux")
    

    @Rule(PersonalInfo(TypeContrat="CDD"))
    def rule_12(self):
        self.declare(Eligibility(ÉligibleAuCrédit=False))
        print("ÉligibleAuCrédit = faux")

    @Rule(Eligibility(ÉligibleAuCrédit=False))
    def acceptance(self):
        print("loan refused")

    @Rule(Eligibility(ÉligibleAuCrédit=True))
    def refused(self):
        print("loan accepted")