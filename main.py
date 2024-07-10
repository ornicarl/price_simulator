import streamlit as st
from model import *

# Fonction principale de l'application Streamlit
def main():
    # Chargement des coefficients du modèle et du schéma
    model_coefficients = load_coefficients_from_json('model_Classification_of_REG_CodeINSEE.json')
    model_schema = get_model_schema(model_coefficients)

    # Initialisation des variables de pricing
    dict_pricing_variables = initialize_pricing_variables(model_schema)

    # Affichage initial du prix en grand
    price_display = st.empty()
    update_price_display(dict_pricing_variables, model_coefficients, price_display)

    # Interaction utilisateur avec les select boxes
    interact_with_select_boxes(dict_pricing_variables, model_schema, model_coefficients, price_display)

# Fonction pour mettre à jour l'affichage du prix
def update_price_display(dict_pricing_variables, model_coefficients, price_display):
    price = predict(dict_pricing_variables, model_coefficients)
    price_display.write(f"<div style='text-align: center; font-size: 32px;'>Price = {price}</div>", unsafe_allow_html=True)

# Fonction pour interagir avec les select boxes
def interact_with_select_boxes(dict_pricing_variables, model_schema, model_coefficients, price_display):
    for variable in define_variables_order():
        dict_pricing_variables[variable] = st.selectbox(
            label=variable,
            options=model_schema[variable],
            index=model_schema[variable].index(dict_pricing_variables.get(variable, model_schema[variable][0])),  # Set default index
            key=variable  # Ensure each select box has a unique key for Streamlit to track changes
        )
    update_price_display(dict_pricing_variables, model_coefficients, price_display)
