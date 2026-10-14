import sub_chords as sc
import notes as nt

chord1 = sc.chord("Amaj9", ["a", "c#", "e", "g", "b"]) 

note1 = nt.note("a")

#print(note1.value==9)

#print(note1.transpose(2))  # Transpose A up by 2 semitones (should be B)

print(chord1.transpose_chord(2))  
print(chord1.sub_chords())  # List of sub-chords