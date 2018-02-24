import os
import django
import pandas as pd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nfc.settings")
django.setup()
from nfcalculator.models import (Ingredient,
                                 IngredientNutritionFact,
                                 Allergen
                                 )


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


def add_to_allergen(_allergen_list):
    """
    This function is supposed to be run just once
    so I will call this function by hand in ypython
    in the following fashion:

    file = "data.xlsx"
    sheet = "ingredient"
    cwd = os.getcwd()
    df = load_products_from_file(file, sheet)
    column_names = df.columns.values.tolist()

    df = pd.DataFrame(df)
    allergen = [",".join([str(i) for i in [row['Alergény'] for index, row in df.iterrows()]])][0]
    allergen = set([x.strip() for x in allergen.split(',') if x != 'nan'])

    add_to_allergen(allergen)

    :param _name:
    :return:
    """

    for i in list(_allergen_list):
        allergen = Allergen.objects.get_or_create(
            name=i
        )[0]
        allergen.save()
    return allergen


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
allergen = [",".join([str(i) for i in [row['Alergény'] for index, row in df.iterrows()]])][0]
allergen = set([x.strip() for x in allergen.split(',') if x != 'nan'])

'''

Allergens:
----------
1	oxid siričitý (v koncentrácii vyšších než 10 mg/kg)
2	raž
3	orechy
4	arašidy
5	horčica
6	mlieko
7	srvátka
8	cmar
9	sezam
10	lepok
11	pšenica
12	vajce
13	zeler
14	špalda
15	jačmeň
16	ovos
17	horčicové semeno
18	strúhanka

table: nutritionfact
--------------------
1	Lipids
2	Saturated
3	Sacharides
4	Sugar
5	Protein
6	Salt


Excel sheet data:
-----------------
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


'''

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



"""
>>> from blog.models import Blog, Entry
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog
>>> entry.save()
"""

# Allergen.objects.get(name="orechy").id
# main.nfcalculator_ingredient_allergens
#
#
# from django.db.models import get_app, get_models
# app = get_app(app_name)
# for model in get_models(app, include_auto_created=True):
#     print model._meta.db_table