import pandas as pd
import math

def validate_input(prompt, validator):
    while True:
        try:
            user_input = validator(input(prompt))
            return user_input
        except ValueError as e:
            print(f"Error: {e}")

def floatint_validator(value):
    try:
        value = float(value)
        if 0 <= value <= 100:
            return value
    except ValueError:
        pass
    raise ValueError("Nieprawidłowa wartość (zakres: 0-100).")

def char_validator(value):
    value = value.upper()
    if value in ('K', 'M'):
        return value
    raise ValueError("Dozwolone wartości: 'K' lub 'M'.")

x = validate_input("Wprowadź wiek początkowy: ", floatint_validator)
n = validate_input("Wprowadź czas trwania: ", floatint_validator)
bPlec = validate_input("Płeć ('K' lub 'M'): ", char_validator)

tablice = 'tablice.xlsx'
df = pd.read_excel(tablice, sheet_name="Kobiety", index_col=0) if bPlec == 'K' else pd.read_excel(tablice, sheet_name="Mezczyzni", index_col=0)

u = 0
y = x + n

if isinstance(x, float):
    u = x - math.floor(x)
    x = math.floor(x)

if isinstance(n, float):
    n = math.floor(n)

lx = df[df['x'] == x]['lx'].values[0]
lxn = df[df['x'] == round(y)]['lx'].values[0]

dx = df[df['x'] == x]['dx'].values[0]
dxn = df[df['x'] == round(y)]['dx'].values[0]

lxu = lx - (u * dx)
lxnu = lxn - (y - round(y)) * dxn 

rate = lxnu/lxu

print("\nParametry:")
print(f'lx: {lx}, lxn: {lxn}, dx: {dx}, dxn: {dxn}, lxu: {lxu}, lxnu: {lxnu}, u: {u}\n')

print(f'Prawdopodobieństwo przeżycia: {round(rate, 4)}')
print(f'Prawdopodobieństwo zgonu: {round(1 - rate, 4)}')