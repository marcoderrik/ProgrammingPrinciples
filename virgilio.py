import os
import json

class Virgilio:

    class CantoNotFoundError(Exception): #eccezione che si attiva se il numero del canto inserito non è corretto
        pass

    def __init__(self, directory):
        self.directory = directory

# es 1 - read_canto_lines per trovare e leggere le righe di un canto
# es 13- se il parametro strip_lines diventa True aggiungi un controllo che toglie tutto ciò che può essere presente all'inizio o alla fine del verso
# es 14- fai inserire in iput num_lines e fa in modo che le linee che vengono date in output siano tante quante num_lines ha chiesto
# es 15- copntrolla che canto_number sia un numero intero

    def read_canto_lines(self, canto_number, strip_lines=False, num_lines=None):
        # controllo se canto_number è parte della classe int, se non lo è segnala l'errore
        if not isinstance(canto_number, int):
            raise TypeError("canto_number must be an integer")
        if not (1 <= canto_number <= 34):
            raise self.CantoNotFoundError("canto_number must be between 1 and 34")

        # riga di codice consigliata per attribiire il giusto percorso file
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        try:
            with open(file_path, "r", encoding="utf-8") as file_path:
                lines = file_path.readlines()
            if strip_lines:
                lines = [line.strip() for line in lines]
            if num_lines is not None:
                lines = lines[:num_lines]
            return lines
        except Exception:
            return [f"error while opening {file_path}: {str(Exception)}"]

# es 2 - conta il numero di versi del canto scelto
    def count_verses(self, canto_number):
        # riutilizzo metodo creato nell'es 1
        lines = self.read_canto_lines(canto_number)
        return len(lines)

# es 3 - conta il numero di terzine del canto scelto
    def count_tercets(self, canto_number):
        # riutilizzo metodo creato nell'es 1
        verses = self.count_verses(canto_number)
        return verses // 3

# es 4 -  (metodo case sensitive)
    def count_word(self, canto_number, word):
        # riutilizzo metodo creato nell'es 1
        lines = self.read_canto_lines(canto_number)
        # join come da suggerimento
        text =",".join(lines)
        return text.count(word)

# es 5 - (metodo case sensitive)
    def get_verse_with_word(self, canto_number, word):
        # riutilizzo metodo creato nell'es 1
        lines = self.read_canto_lines(canto_number)
        # ciclo che controlla ogni riga del canto e trova il primo verso con word
        for line in lines:
            if word in line:
                return line


# es 6 -  (metodo case sensitive)
    def get_verses_with_word(self, canto_number, word):
        # riutilizzo metodo creato nell'es 1
        lines = self.read_canto_lines(canto_number)
        return [line for line in lines if word in line]

# es 7 -
    def get_longest_verse(self, canto_number):
        # riutilizzo metodo creato nell'es 1
        lines = self.read_canto_lines(canto_number)
        #variabile che prende tramite ciclo  for il valore della riga più lunga passata
        longest_line = "Pitone Programmatore"
        for line in lines:
            if len(line) > len(longest_line):
                longest_line = line
        return longest_line

# es 8 - 
    def get_longest_canto(self):
        canto_len = 0
        longest_canto = 0
        # ciclo for che itera ogni canto e in base al numero di versi trova il più lungo
        for canto_number in range(1, 35):
            # riutilizzo metodo creato nell'es 2
            verses = self.count_verses(canto_number)
            if verses > canto_len:
                canto_len = verses
                longest_canto = canto_number
        return {"canto_number": longest_canto, "canto_len": canto_len}

# es 9 - (case sensitive)
    def count_words(self, canto_number, words = ["vita", "dolente", "porta"]):
        # riutilizzo metodo creato nell'es 2
        lines = self.read_canto_lines(canto_number)
        # usando la stessa metodologia dell'esercizio 4 trovo tutte le parole della lista alòl'interno del canto
        text = ",".join(lines)
        word_counts = {}
        for word in words:
            word_counts[word] = text.count(word)
#ES 18 - 
        json_path = os.path.join(self.directory, "word_counts.json")
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(word_counts, json_file)
        
        return word_counts

# es 10 - 
    def get_hell_verses(self):
        # creo una lista che tramite l'iterazione della funzione read_canto_lines (es 1) estende la lista popolandola con tutti i versi di ogni canto
        all_verses = []
        for canto_number in range(1, 35):
            all_verses.extend(self.read_canto_lines(canto_number))
        return all_verses

# es 11 - 
    def count_hell_verses(self):
        '''utilizzata la stessa metodologia dell'es 10 utilizzando invece che i versi letti dalla funzione read_canto_lines (es 1) /
        i versi contati dalla funzione count_verses (es 2)'''
        total_verses = 0
        for canto_number in range(1, 35):
            total_verses += self.count_verses(canto_number)
        return int(total_verses)

# es 12 - 
    def get_hell_verse_mean_len(self):
        # utilizzata la funzione creata nell'es 10 per ottenere tutti i versi
        # calcolata la lunghezza di ogni verso tramite un ciclo for e sommate tutte le lunghezze
        # diviso la lunghezza totale per la quantità di versì per trovare la media, float
        all_verses = self.get_hell_verses()
        total_length = 0
        for verse in all_verses:
            total_length += len(verse.strip())  # rimuove solo spazi inizio/fine verso
        
        return float(total_length / len(all_verses))
