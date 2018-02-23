import os
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'initial.settings')
import django
django.setup()
from nfcalculator.models import Ingredient, \
                                Product, \
                                ProductIngredient, \
                                IngredientNutritionFact

def load_products_from_file(file_name=None, sheet_name=None):
    file_name = file_name
    sheet_name = sheet_name
    xl = pd.ExcelFile(file_name)
    data_frame = xl.parse(sheet_name)
    return data_frame

file = "data.xlsx"
sheet = "ingredient"
cwd = os.getcwd()
df = load_products_from_file(file, sheet)
column_names = df.head(1).columns.values.tolist()

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
'''

# for index, row in df.head(1).iterrows():
#     print(row['Názov produktu'],
#           row['Výrobca/Distribútor'],
#           row['Zloženie'],
#           row['Alergény'],
#           row['Môže obsahovať'],
#           row['Tuky'],
#           row['Z toho nasýtené mastné kyseliny'],
#           row['Sacharidy'],
#           row['Z toho cukry'],
#           row['Bielkoviny'],
#           row['Soľ'])


def add_to_ingridient():
    ingridient = Ingredient.objects.get_or_create(top_name=random.choice(topics))[0]
    ingridient.save()
    return ingridient




