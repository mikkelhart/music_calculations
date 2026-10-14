import numpy as np

test_array = np.array([1,2,3,4,5])

import notes as nts    

print("a" + "c")


print(test_array+1)

class chord():
    def __init__(self, name, notes):
        self.name = name #string
        self.notes = notes #string list with note class as entries (see notes.py)
        if for note in notes:
            if not isinstance(note, nts.note):
                raise ValueError(f"All elements in 'notes' must be instances of the 'note' class. Found {type(note)} instead.")

    def __str__(self):
        return f"{self.name}: {self.notes}"

    def __repr__(self):
        return f"chord({self.name}, {self.notes})"
    
    def get_notes(self):
        return self.notes

    def get_name(self):
        return self.name


    #Lowest priority
    def transpose(self, semitones):
        transposed_notes = [(note.value + semitones) % 12 for note in self.notes] #fixed for typeerror
        return chord(self.name, transposed_notes) #self.name needs to change

    

    def sub_chords(self):
        sub_chords_list = []
        for i in range(len(self.notes)):
            
            #string of root note name that leads into
            #string explaining the relation in Roman numerals

            rel = self.notes[0].relation_of_two_notes(self.notes[i]) 
                    
            note_num_i = self.notes[i].value #int value of note w.r.t. C

            for j in range(i+1, len(self.notes)):

                #We check for minor thirds/triads, and they are followed by either 
                #the perfect fifth or the diminished fifth. 
                
                note_num_j = self.notes[j].value #int

                if np.abs(note_num_i-note_num_j) == 3:
                    for k in range(j+1, len(self.notes)):

                        note_num_k = self.notes[k].value #int

                        if np.abs(note_num_j-note_num_k) == 4:
                            
                            #We test for the perfect fifth
                            sub_chord = chord(f"{rel}m", [self.notes[i], self.notes[j], self.notes[k]])
                            sub_chords_list.append(sub_chord)
                        elif np.abs(note_num_j-note_num_k) == 3:
                            
                            #We test for the diminished
                            sub_chord = chord(f"{rel}dim", [self.notes[i], self.notes[j], self.notes[k]])
                            sub_chords_list.append(sub_chord)
                        
                        else:

                            #We only have the first two notes, no fifth
                            sub_chord = chord(f"{rel} minor without fifth", [self.notes[i], self.notes[j]])
                            sub_chords_list.append(sub_chord)
                #Here we check for major triads, which are followed by either 
                #the perfect fifth or the augmented fifth.
                elif np.abs(note_num_i-note_num_j) == 4:

                    note_num_k = self.notes[k].value #int

                    for k in range(j+1, len(self.notes)):
                        if np.abs(note_num_j-note_num_k) == 3:
                            
                            #We test for the perfect fifth
                            sub_chord = chord(f"{rel} major", [self.notes[i], self.notes[j], self.notes[k]])
                            sub_chords_list.append(sub_chord)
                        elif np.abs(note_num_j-note_num_k) == 4:
                            
                            #We test for the augmented fifth
                            sub_chord = chord(f"{rel}aug", [self.notes[i], self.notes[j], self.notes[k]])
                            sub_chords_list.append(sub_chord)
                        else:
                            
                            #If there is no fifth and we only have the first two notes

                            sub_chord = chord(f"{rel} major without fifth", [self.notes[i], self.notes[j]])
                            sub_chords_list.append(sub_chord)
                
        return sub_chords_list


chord1 = chord("Amaj", ["a", "c#", "e"])  # A major chord (A, C#, E)
print(chord1.transpose(2))  # A major chord (A, C#, E)
print(chord1.sub_chords())  # List of sub-chords