import os
import django
import pandas as pd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nfc.settings")
django.setup()
from nfcalculator.models import Ingredient, IngredientNutritionFact


def load_products_from_file(file_name=None, sheet_name=None):
    """

    :param file_name:
    :param sheet_name:
    :return: returns loaded dataframe - basically data from excel file :)
    """
    file_name = file_name
    sheet_name = sheet_name
    xl = pd.ExcelFile(file_name)
    data_frame = xl.parse(sheet_name)
    return data_frame


def add_to_ingredient(_name, _description):
    """

    :param _name:
    :param _description:
    :return: returns what has been added to sqlite database
    """
    ingredient = Ingredient.objects.get_or_create(
        name=_name,
        description=_description
    )[0]
    ingredient.save()
    return ingredient


def add_to_ingredientnutritionfact(_ingredient_id,
                                   _nutrition_fact_id,
                                   _weight):
    """

    :param ingredient_id:        for example butter - Liptov with      #5
    :param nutrition_fact_id:    for example Lipids with fixed         #1
    :param weight:               Lipds per hundred grams for example   30g
    :return:
    """
    inf = IngredientNutritionFact.objects.get_or_create(
        ingredient_id=_ingredient_id,
        nutrition_fact_id=_nutrition_fact_id,
        weight=_weight
        )[0]
    inf.save()
    return inf


file = "data.xlsx"
sheet = "ingredient"
cwd = os.getcwd()
df = load_products_from_file(file, sheet)
column_names = df.columns.values.tolist()

df = pd.DataFrame(df)

'''

'Názov produktu'
'Výrobca/Distribútor'
'Zloženie'
'Alergény'
'Môže obsahovať'
'Tuky'
'Z toho nasýtené mastné kyseliny'
'Sacharidy'
'Z toho cukry'
'Bielkoviny'
'Soľ'

table: nutritionfact
1	Lipids
2	Saturated
3	Sacharides
4	Sugar
5	Protein
6	Salt

'''

imported_ingredients = {}
for index, row in df.head(10).iterrows():
    # inserting to table: Ingredient
    ingredient_object = add_to_ingredient(row['Názov produktu'], row['Zloženie'])

    Lipids = row['Tuky']
    Saturated = row['Z toho nasýtené mastné kyseliny']
    Sacharides = row['Sacharidy']
    Sugar = row['Z toho cukry']
    Protein = row['Bielkoviny']
    Salt = row['Soľ']

    # inserting to table: IngredientNutritionFact
    #           zip([number identifiers], [actual weights for Lipids, Saturated, ...]):
    for i, j in zip([1, 2, 3, 4, 5, 6], [Lipids, Saturated, Sacharides, Sugar, Protein, Salt]):
        ingredientnutritionfact_object = add_to_ingredientnutritionfact(
            _ingredient_id=ingredient_object.id,
            _nutrition_fact_id=i,
            _weight=float(str(j).replace(',', '.'))
        )








