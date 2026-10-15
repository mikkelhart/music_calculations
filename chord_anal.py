import sub_chords as sc
import notes as nt

chord1 = sc.chord("Amaj13", ["a", "c#", "e", "g", "b", "d", "f#"]) 

note1 = nt.note("a")

#print(note1.value==9)

#print(note1.transpose(2))  # Transpose A up by 2 semitones (should be B)


print(chord1.sub_chords())  # List of sub-chords