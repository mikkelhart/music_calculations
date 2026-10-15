import numpy as np
import notes as nt    

class chord():
    def __init__(self, name, notes):
        self.name = name #string
        
        self.notes = []
        for note in notes:
            actual_note = nt.note(note) #convert string to note class
            self.notes.append(actual_note) #append the actual note object

    def __str__(self):
        return f"{self.name}: {self.notes}"

    def __repr__(self):
        return f"chord({self.name}, {self.notes})"
    

    #Lowest priority
    def transpose_chord(self, semitones):
        
        transposed_notes = []
        for note in self.notes:
            transposed_note = note.transpose(semitones)
            transposed_notes.append(transposed_note.name)
        return chord(self.name, transposed_notes) #self.name needs to change

    

    def sub_chords(self):
        sub_chords_list = []
        
        for i in range(len(self.notes)):
            
            #string of root note name that leads into
            #string explaining the relation in Roman numerals

            relation = self.notes[0].relation_of_two_notes(self.notes[i]) 
                    
            note_num_i = self.notes[i].value #int value of note w.r.t. C
            note_name_i = self.notes[i].name #string name of note

            for j in range(i, len(self.notes)):

                #We check for minor thirds/triads, and they are followed by either 
                #the perfect fifth or the diminished fifth. 
                
                note_num_j = self.notes[j].value #int
                note_name_j = self.notes[j].name #string name of note

                if np.abs(note_num_i-note_num_j) == 3:
                    for k in range(j, len(self.notes)):

                        note_num_k = self.notes[k].value #int
                        note_name_k = self.notes[k].name #string name of note

                        if np.abs(note_num_j-note_num_k) == 4:
                            
                            #We test for the perfect fifth
                            sub_chord = chord(f"{relation}m", [note_name_i, note_name_j, note_name_k])
                            sub_chords_list.append([sub_chord.name, sub_chord.notes])
                        elif np.abs(note_num_j-note_num_k) == 3:
                            
                            #We test for the diminished
                            sub_chord = chord(f"{relation}dim", [note_name_i, note_name_j, note_name_k])
                            sub_chords_list.append([sub_chord.name, sub_chord.notes])
                        
                        else:

                            #We only have the first two notes, no fifth
                            continue
                            #sub_chord = chord(f"{relation} minor without fifth", [note_name_i, note_name_j])
                            #sub_chords_list.append([sub_chord.name, sub_chord.notes])
                
                
                #Here we check for major triads, which are followed by either 
                #the perfect fifth or the augmented fifth.
                elif np.abs(note_num_i-note_num_j) == 4:

                    note_num_k = self.notes[k].value #int

                    for k in range(j, len(self.notes)):
                        if np.abs(note_num_j-note_num_k) == 3:
                            
                            #We test for the perfect fifth
                            sub_chord = chord(f"{relation} major", [note_name_i, note_name_j, note_name_k])
                            sub_chords_list.append([sub_chord.name, sub_chord.notes])
                        elif np.abs(note_num_j-note_num_k) == 4:
                            
                            #We test for the augmented fifth
                            sub_chord = chord(f"{relation}aug", [note_name_i, note_name_j, note_name_k])
                            sub_chords_list.append([sub_chord.name, sub_chord.notes])
                        else:
                            
                            #If there is no fifth and we only have the first two notes
                            continue
                            #sub_chord = chord(f"{relation} major without fifth", [note_name_i, note_name_j])
                            #sub_chords_list.append([sub_chord.name, sub_chord.notes])

        
        print(len(sub_chords_list), sub_chords_list)
        
        #for sub_chord in sub_chords_list:
         #   print(f"Sub-chord: {sub_chord.get_name()}, Notes: {[note.get_name() for note in sub_chord.get_notes()]}")
