import re
import sys

def is_key_word(buffer):

    flag = False
    key_words = [
        "funcion_principal", "fin_principal", "booleano", "caracter", "entero", "real", "cadena",
        "leer", "imprimir", "si", "si_no", "fin_si", "entonces", "mientras","fin_mientras", "hacer",
        "para", "fin_para", "seleccionar", "fin_seleccionar", "romper", "defecto", "estructura",
        "fin_estructura", "funcion", "fin_funcion", "retornar", "verdadero", "falso"
    ]
    if buffer in key_words:

        flag = True
    return flag

tokens = {
        "+": "tk_mas",
        "-": "tk_menos",
        "*": "tk_mult",
        "/": "tk_div",
        "%": "tk_mod",
        "=": "tk_asig",
        "<": "tk_menor",
        ">": "tk_mayor",
        "<=": "tk_menor_igual",
        ">=": "tk_mayor_igual",
        "==": "tk_igual",
        "&&": "tk_y",
        "||": "tk_o",
        "!=": "tk_dif",
        "!": "tk_neg",
        ":": "tk_dosp",
        "‘": "tk_comilla_sen",
        "“": "tk_comilla_dob",
        ";": "tk_pyc",
        ",": "tk_coma",
        ".": "tk_punto",
        "(": "tk_par_izq",
        ")": "tk_par_der"
    }

states = [
    "INITIAL", "LINEBREAK", "WHITESPACE", "IDENTIFIER","STRING","LEXICALERROR",
    "COMMENTARY", "SPECIALCHAR"
]

def statesHandler(states, entry):
    row = 0
    column = 0
    if is_key_word(entry):
        print("<"+str(entry)+","+str(row)+","+str(column)+">")


buffercito = "funcion"
# Imprimir palabra reservada
print("\n"+"Palabra reservada = <"+"keyWord"+",numero linea"+",columna"+">"+"\n")

# Imprimir identificador
print("Identificador = <"+"id"+",lexema"+",fila"+",columna"+">"+"\n")

# Imprimir Simbolos
print("Simbolos = <"+"token"+",fila"+",columna"+">"+"\n")

# Imprimir Error
print("Error lexico = Error lexico ("+"fila"+",columna"+")"+"\n")


Str = input()

statesHandler(states, Str)
