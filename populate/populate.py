import os
import django
import pandas as pd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nfc.settings")
django.setup()
from nfcalculator.models import (Ingredient,
                                 IngredientNutritionFact,
                                 Allergen,
                                 Extra
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


def add_to_ingredient(_name, _description, _allergen, _may_contain):
    """
    <database models.py>
    ...
    class Ingredient(models.Model):
        name = models.CharField(max_length=255, null=False, blank=False)
        description = models.TextField(null=True, blank=False)
        allergens = models.ManyToManyField(Allergen)
        may_contain = models.ManyToManyField(Extra)
    ...
    </database models.py>

    :param _name:
    :param _description:
    :param _allergen:      this is actual "excel cell" from column 'Alergény' when iterating
                           through particular excel rows (pandas data_frame respectively)

    :return:

    """

    allergen_set_object = set(str(_allergen).split(','))
    allergen_set_object = set([i.strip() for i in allergen_set_object])

    may_contain_set_object = set(str(_may_contain).split(','))
    may_contain_set_object = set([i.strip() for i in may_contain_set_object])

    print("allergen_set_object: {}".format(allergen_set_object))

    '''
    Example: allergen_set_object
    ----------------------------
    ...
    {'mlieko'}
    {'vajce'}
    {'pšenica'}
    {'nan'}
    {'jačmeň', 'pšenica', 'vajce', 'horčica'}
    ...
    '''
    ingredient = Ingredient.objects.get_or_create(
        name=_name,
        description=_description
    )[0]

    # Allergens section
    for i in allergen_set_object:
        try:
            record = Allergen.objects.get(name=i).id
            ingredient.allergens.add(record)
        except Exception as ale:
            print("allergen Error: {}".format(ale))

    # May contain extra section
    for i in may_contain_set_object:
        try:
            record = Extra.objects.get(name=i).id
            ingredient.may_contain.add(record)
        except Exception as mc:
            print("may_contain Error: {}".format(mc))

    ingredient.save()
    return ingredient


def add_to_allergen(_allergen_list):
    """
    This function is supposed to be run just once
    so I will call this function by hand in ypython
    in the following fashion:

    <code>
    file = "data.xlsx"
    sheet = "ingredient"
    cwd = os.getcwd()
    df = load_products_from_file(file, sheet)
    column_names = df.columns.values.tolist()

    df = pd.DataFrame(df)
    allergen = [",".join([str(i) for i in [row['Alergény'] for index, row in df.iterrows()]])][0]
    allergen_list = set([x.strip() for x in allergen.split(',') if x != 'nan'])

    add_to_allergen(allergen_list)
    </code>

    :param _name:
    :return:
    """

    for i in list(_allergen_list):
        allergen = Allergen.objects.get_or_create(
            name=i
        )[0]
        allergen.save()
    return allergen


def add_to_extra(_extra_list):
    """
    This function is supposed to be run just once
    so I will call this function by hand in ypython
    in the following fashion:

    <code>
    file = "data.xlsx"
    sheet = "ingredient"
    cwd = os.getcwd()
    df = load_products_from_file(file, sheet)
    column_names = df.columns.values.tolist()

    df = pd.DataFrame(df)
    extra = [",".join([str(i) for i in [row['Môže obsahovať'] for index, row in df.iterrows()]])][0]
    extra_list = set([x.strip() for x in extra.split(',') if x != 'nan'])

    add_to_extra(extra_list)
    </code>

    :param _name:
    :return:
    """

    for i in list(_extra_list):
        extra = Extra.objects.get_or_create(
            name=i
        )[0]
        extra.save()
    return extra


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
allergen_list = set([x.strip() for x in allergen.split(',') if x != 'nan'])


extra = [",".join([str(i) for i in [row['Môže obsahovať'] for index, row in df.iterrows()]])][0]
extra_list = set([x.strip() for x in extra.split(',') if x != 'nan'])


'''

table: Allergens:
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

table: Extra
------------
1	siričitany
2	sójové bôby
3	sezam
4	vajce
5	horčica
6	mlieko
7	sôja
8	arašidy
9	glutén
10	orechy
11	sezamové semeno
12	zeler


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

for index, row in df.iterrows():
    # inserting to table: Ingredient
    print('processing: {}'.format(row['Názov produktu']))
    ingredient_object = add_to_ingredient(row['Názov produktu'],
                                          row['Zloženie'],
                                          row['Alergény'],
                                          row['Môže obsahovať'])

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











