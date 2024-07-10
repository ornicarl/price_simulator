import json


# Fonction pour initialiser les variables de pricing
def initialize_pricing_variables(model_schema):
    dict_pricing_variables = {}
    for variable in define_variables_order():
        dict_pricing_variables[variable] = model_schema[variable][0]  # Initialisation avec la première option comme placeholder
    return dict_pricing_variables


def get_model_schema(model):

    model_schema = {}

    for variable in model['coefficients']:
        model_schema[variable] = list(model['coefficients'][variable].keys())

    return model_schema

def predict(input_features, model):

    # Initialiser l'intercept
    prediction = model.get('intercept', 0.0)

    # Ajouter les termes de base
    for feature in model['coefficients']:
        prediction *= model['coefficients'][feature][input_features[feature]]

    # Ajouter les termes d'interaction
    for feature1 in model['interactionsCoefficients']:
        for feature2 in model['interactionsCoefficients'][feature1]:
            prediction *= model['interactionsCoefficients'][feature1][feature2][input_features[feature1]][input_features[feature2]]
    
    return prediction

def define_variables_order():
    list_variables = [
        'Package',
        'POL_Antecedent',
        'POL_CRM_MainDriver',
        'POL_CRM_SecondDriver1',
        'PER_TimeB50_MainDriver',
        'PER_AgeWhenPurchasedVehicle',
        'PER_Age_SecondDriver',
        'PER_DurDetVehicle',
        'PER_LicenceAge',
        'REG_CodeINSEE',
        'MRH_PER_BuildingDescription',
        'MRH_PER_Ownership',
        'VEH_Age',
        'VEH_Carrosserie_FOCUS',
        'BEH_TypeGarage',
        'POL_DeclaredAnnualKm',
        'SRA_Alimentation',
        'SRA_Groupe',
        'SRA_PuissanceReelleMaxiCEE',
        'SRA_VitesseMaxi'
        ]
    
    return list_variables

def load_coefficients_from_json(json_file):
    with open(json_file, 'r') as file:
        coefficients = json.load(file)
    return coefficients
