import pygame
pygame.mixer.init(channels=3)

bass = []
musicBox = []
bell = []
flute = []
guitar = []
synthesizer = []
violin = []
voice = []
bamboo = []
triangles = []

bass.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
bass.append(pygame.mixer.Sound(".\\sounds\\bass\\bass1.ogg"))
bass.append(pygame.mixer.Sound(".\\sounds\\bass\\bass2.ogg"))
bass.append(pygame.mixer.Sound(".\\sounds\\bass\\bass3.ogg"))
bass.append(pygame.mixer.Sound(".\\sounds\\bass\\bass4.ogg"))
bass.append(pygame.mixer.Sound(".\\sounds\\bass\\bass5.ogg"))
bass.append(pygame.mixer.Sound(".\\sounds\\bass\\bass6.ogg"))
bass.append(pygame.mixer.Sound(".\\sounds\\bass\\bass7.ogg"))

musicBox.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
musicBox.append(pygame.mixer.Sound(".\\sounds\\musicBox\\musicBox1.ogg"))
musicBox.append(pygame.mixer.Sound(".\\sounds\\musicBox\\musicBox2.ogg"))
musicBox.append(pygame.mixer.Sound(".\\sounds\\musicBox\\musicBox3.ogg"))
musicBox.append(pygame.mixer.Sound(".\\sounds\\musicBox\\musicBox4.ogg"))
musicBox.append(pygame.mixer.Sound(".\\sounds\\musicBox\\musicBox5.ogg"))
musicBox.append(pygame.mixer.Sound(".\\sounds\\musicBox\\musicBox6.ogg"))
musicBox.append(pygame.mixer.Sound(".\\sounds\\musicBox\\musicBox7.ogg"))

bell.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
bell.append(pygame.mixer.Sound(".\\sounds\\bell\\bell1.ogg"))
bell.append(pygame.mixer.Sound(".\\sounds\\bell\\bell2.ogg"))
bell.append(pygame.mixer.Sound(".\\sounds\\bell\\bell3.ogg"))
bell.append(pygame.mixer.Sound(".\\sounds\\bell\\bell4.ogg"))
bell.append(pygame.mixer.Sound(".\\sounds\\bell\\bell5.ogg"))
bell.append(pygame.mixer.Sound(".\\sounds\\bell\\bell6.ogg"))
bell.append(pygame.mixer.Sound(".\\sounds\\bell\\bell7.ogg"))

flute.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
flute.append(pygame.mixer.Sound(".\\sounds\\flute\\flute1.ogg"))
flute.append(pygame.mixer.Sound(".\\sounds\\flute\\flute2.ogg"))
flute.append(pygame.mixer.Sound(".\\sounds\\flute\\flute3.ogg"))
flute.append(pygame.mixer.Sound(".\\sounds\\flute\\flute4.ogg"))
flute.append(pygame.mixer.Sound(".\\sounds\\flute\\flute5.ogg"))
flute.append(pygame.mixer.Sound(".\\sounds\\flute\\flute6.ogg"))
flute.append(pygame.mixer.Sound(".\\sounds\\flute\\flute7.ogg"))

guitar.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\guitar1.ogg"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\guitar2.ogg"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\guitar3.ogg"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\guitar4.ogg"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\guitar5.ogg"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\guitar6.ogg"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\guitar7.ogg"))

synthesizer.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
synthesizer.append(pygame.mixer.Sound(".\\sounds\\synthesizer\\synthesizer1.ogg"))
synthesizer.append(pygame.mixer.Sound(".\\sounds\\synthesizer\\synthesizer2.ogg"))
synthesizer.append(pygame.mixer.Sound(".\\sounds\\synthesizer\\synthesizer3.ogg"))
synthesizer.append(pygame.mixer.Sound(".\\sounds\\synthesizer\\synthesizer4.ogg"))
synthesizer.append(pygame.mixer.Sound(".\\sounds\\synthesizer\\synthesizer5.ogg"))
synthesizer.append(pygame.mixer.Sound(".\\sounds\\synthesizer\\synthesizer6.ogg"))
synthesizer.append(pygame.mixer.Sound(".\\sounds\\synthesizer\\synthesizer7.ogg"))

violin.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
violin.append(pygame.mixer.Sound(".\\sounds\\violin\\violin1.ogg"))
violin.append(pygame.mixer.Sound(".\\sounds\\violin\\violin2.ogg"))
violin.append(pygame.mixer.Sound(".\\sounds\\violin\\violin3.ogg"))
violin.append(pygame.mixer.Sound(".\\sounds\\violin\\violin4.ogg"))
violin.append(pygame.mixer.Sound(".\\sounds\\violin\\violin5.ogg"))
violin.append(pygame.mixer.Sound(".\\sounds\\violin\\violin6.ogg"))
violin.append(pygame.mixer.Sound(".\\sounds\\violin\\violin7.ogg"))

voice.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
voice.append(pygame.mixer.Sound(".\\sounds\\voice\\voice1.ogg"))
voice.append(pygame.mixer.Sound(".\\sounds\\voice\\voice2.ogg"))
voice.append(pygame.mixer.Sound(".\\sounds\\voice\\voice3.ogg"))
voice.append(pygame.mixer.Sound(".\\sounds\\voice\\voice4.ogg"))
voice.append(pygame.mixer.Sound(".\\sounds\\voice\\voice5.ogg"))
voice.append(pygame.mixer.Sound(".\\sounds\\voice\\voice6.ogg"))
voice.append(pygame.mixer.Sound(".\\sounds\\voice\\voice7.ogg"))

bamboo.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
bamboo.append(pygame.mixer.Sound(".\\sounds\\bamboo\\bamboo1.ogg"))
bamboo.append(pygame.mixer.Sound(".\\sounds\\bamboo\\bamboo2.ogg"))
bamboo.append(pygame.mixer.Sound(".\\sounds\\bamboo\\bamboo3.ogg"))
bamboo.append(pygame.mixer.Sound(".\\sounds\\bamboo\\bamboo4.ogg"))
bamboo.append(pygame.mixer.Sound(".\\sounds\\bamboo\\bamboo5.ogg"))
bamboo.append(pygame.mixer.Sound(".\\sounds\\bamboo\\bamboo6.ogg"))
bamboo.append(pygame.mixer.Sound(".\\sounds\\bamboo\\bamboo7.ogg"))

triangles.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
triangles.append(pygame.mixer.Sound(".\\sounds\\triangles\\triangles1.ogg"))
triangles.append(pygame.mixer.Sound(".\\sounds\\triangles\\triangles2.ogg"))
triangles.append(pygame.mixer.Sound(".\\sounds\\triangles\\triangles3.ogg"))
triangles.append(pygame.mixer.Sound(".\\sounds\\triangles\\triangles4.ogg"))
triangles.append(pygame.mixer.Sound(".\\sounds\\triangles\\triangles5.ogg"))
triangles.append(pygame.mixer.Sound(".\\sounds\\triangles\\triangles6.ogg"))
triangles.append(pygame.mixer.Sound(".\\sounds\\triangles\\triangles7.ogg"))
