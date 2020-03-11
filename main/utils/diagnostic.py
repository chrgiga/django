class Diagnostic:
    diagnostic_symptoms = []
    covid = False
    neumonia = False
    gripe = False

    def get_diagnostic(self, symptoms):
        for symptom in symptoms:
            self.diagnostic_symptoms.append(symptom.symptom_name)
        if ('fever' in self.diagnostic_symptoms and
                'cough' in self.diagnostic_symptoms and
                'fatigue' in self.diagnostic_symptoms):
            self.neumonia = 'mucus' in self.diagnostic_symptoms
            self.covid = 'mucus' not in self.diagnostic_symptoms
        else:
            self.gripe = True

        if self.covid:
            return 'You have the current symptoms of COVID-19.'
        if self.neumonia:
            return 'You have the current symptoms of neumonia.'
        else:
            return 'You have the current symptoms of gripe.'
