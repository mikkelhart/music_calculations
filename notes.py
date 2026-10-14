note_values = {'c': 0,'c#': 1,'db': 1,'d': 2,'d#': 3,'eb': 3,'e': 4,'fb': 4,'e#': 5,'f': 5,'f#': 6,'gb': 6,'g': 7,'g#': 8,'ab': 8,'a': 9,'a#': 10,'bb': 10,'b': 11,'cb': 11,'b#': 0}
note_values_capital = {'C': 0,'C#': 1,'Db': 1,'D': 2,'D#': 3,'Eb': 3,'E': 4,'Fb': 4,'E#': 5,'F': 5,'F#': 6,'Gb': 6,'G': 7,'G#': 8,'Ab': 8,'A': 9,'A#': 10,'Bb': 10,'B': 11,'Cb': 11,'B#': 0}



class note():
    def __init__(self, name):
        self.name = name
        if name in note_values:
            self.value = note_values[name]
        elif name in note_values_capital:
            self.value = note_values_capital[name]
        else:
            print(f"Warning: Note '{name}' is not recognized. Please use a valid note name (e.g., C, D#, Eb, F, G, A, B).")
        
        
    def get_name(self):
        return self.name
   
    def transpose(self, semitones):
        transposed_value = (self.value + semitones) % 12
    

    def relation_of_two_notes(self, other_note, value=1):

        #Returns a string

        print("If you want the relation form to be e.g. 'perfect fifth',\n then change the 'value' parameter to 0 by writing 'value==0'.")
        if self.value == other_note.value:
            return "unison"
        elif (self.value + 1) % 12 == other_note.value:
            return ["minor second","bII"][value]
        elif (self.value + 2) % 12 == other_note.value:
            return ["major second","II"][value]
        elif (self.value + 3) % 12 == other_note.value:
            return ["minor third","bIII"][value]
        elif (self.value + 4) % 12 == other_note.value:
            return ["major third","III"][value]
        elif (self.value + 5) % 12 == other_note.value:
            return ["perfect fourth","IV"][value]
        elif (self.value + 6) % 12 == other_note.value:
            return ["tritone","bV"][value]
        elif (self.value + 7) % 12 == other_note.value:
            return ["perfect fifth","V"][value]
        elif (self.value + 8) % 12 == other_note.value:
            return ["minor sixth","bVI"][value]
        elif (self.value + 9) % 12 == other_note.value:
            return ["major sixth","VI"][value]
        elif (self.value + 10) % 12 == other_note.value:
            return ["minor seventh", "bVII"][value]
        elif (self.value + 11) % 12 == other_note.value:
            return ["major seventh", "VII"][value]
        else:
            return "unknown interval"
    #def relation_w_one_note(self, rel):
        
        
        
        
        
        

