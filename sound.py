import pygame
pygame.mixer.init(channels=3)
xilofone=[]
guitar=[]
saxo=[]
maracas=[]
    
xilofone.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
xilofone.append(pygame.mixer.Sound(".\\sounds\\xilofone\\A1.ogg"))
xilofone.append(pygame.mixer.Sound(".\\sounds\\xilofone\\B1.ogg"))
xilofone.append(pygame.mixer.Sound(".\\sounds\\xilofone\\C1.ogg"))
xilofone.append(pygame.mixer.Sound(".\\sounds\\xilofone\\D1.ogg"))


guitar.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\130624_095333-[5].wav"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\130624_095823-[4].wav"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\130624_095938-[3].wav"))
guitar.append(pygame.mixer.Sound(".\\sounds\\guitar\\130624_100353-[5].wav"))


saxo.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
saxo.append(pygame.mixer.Sound(".\\sounds\\saxo\\316898__jaz-the-man-2__do.wav"))
saxo.append(pygame.mixer.Sound(".\\sounds\\saxo\\316902__jaz-the-man-2__la.wav"))
saxo.append(pygame.mixer.Sound(".\\sounds\\saxo\\316906__jaz-the-man-2__mi.wav"))
saxo.append(pygame.mixer.Sound(".\\sounds\\saxo\\316908__jaz-the-man-2__re.wav"))


maracas.append(pygame.mixer.Sound(".\\sounds\\silence.ogg"))
maracas.append(pygame.mixer.Sound(".\\sounds\\Maracas\\LPSP_MARACAS_01.wav"))
maracas.append(pygame.mixer.Sound(".\\sounds\\Maracas\\LPSP_MARACAS_02.wav"))
maracas.append(pygame.mixer.Sound(".\\sounds\\Maracas\\LPSP_MARACAS_03.wav"))
maracas.append(pygame.mixer.Sound(".\\sounds\\Maracas\\LPSP_MARACAS_04.wav"))
