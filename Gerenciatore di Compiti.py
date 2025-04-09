import json
import os

def caricare_compiti():
    if os.path.exists('compiti.json'):
        with open('compiti.json', 'r') as file:
            return json.load(file)
    return []

def salvare_compiti(compiti):
    with open('compiti.json', 'w') as file:
        json.dump(compiti, file, indent=4)

def aggiungere_compito(compiti):
    descrizione = input("Inserisci la descrizione del compito: ")
    compito = {
        'descrizione': descrizione,
        'completato': False
    }
    compiti.append(compito)
    salvare_compiti(compiti)
    print('-'*40)
    print("\033[32mCompito aggiunto con successo!\033[m")
    print('-' * 40)

def elencare_compiti(compiti):
    if not compiti:
        print("\033[31mNon ci sono compiti registrati.\033[m")
    else:
        for index, compito in enumerate(compiti, 1):
            stato = 'Completato' if compito['completato'] else 'In sospeso'
            print(f"{index}. {compito['descrizione']} - {stato}")


def completare_compito(compiti):
    elencare_compiti(compiti)
    try:
        indice = int(input("Inserisci il numero del compito da completare: "))
        if 0 < indice <= len(compiti):
            compiti[indice - 1]['completato'] = True
            salvare_compiti(compiti)
            print("\033[32mCompito marcato come completato!\033[m")
        else:
            print("\033[31mCompito non trovato.\033[m")
    except ValueError:
        print("Per favore, inserisci un numero valido.")


def eliminare_compito(compiti):
    elencare_compiti(compiti)
    try:
        indice = int(input("Inserisci il numero del compito da eliminare: "))
        if 0 < indice <= len(compiti):
            compiti.pop(indice - 1)
            salvare_compiti(compiti)
            print("\033[32mCompito eliminato con successo!\033[m")
        else:
            print("\033[31mCompito non trovato.\033[m")
    except ValueError:
        print("Per favore, inserisci un numero valido.")

# Principale
def gestore_compiti():
    compiti = caricare_compiti()

    while True:
        print('=-'*20)
        print(f'{"GESTORE DI COMPITI":^40}')
        print('=-'*20)
        print("1. Aggiungi Compito")
        print("2. Elenca Compiti")
        print("3. Marcare Compito come Completato")
        print("4. Elimina Compito")
        print("5. Esci")
        print('-' * 40)

        opzione = input("Scegli un'opzione (1/2/3/4/5): ")

        if opzione == '1':
            aggiungere_compito(compiti)
        elif opzione == '2':
            elencare_compiti(compiti)
        elif opzione == '3':
            completare_compito(compiti)
        elif opzione == '4':
            eliminare_compito(compiti)
        elif opzione == '5':
            print("Uscita...")
            break
        else:
            print("\033[31mOpzione non valida! Riprova.\033[m")


if __name__ == "__main__":
    gestore_compiti()



