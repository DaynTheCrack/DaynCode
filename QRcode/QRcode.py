#######################
import qrcode # import de la lib "qrcode"
#######################

"""Création de l'interface de modification Terminal"""

format = [".jpg",".png"] # liste des formats

def MyQR():
    data = input("Chaine à transformer (entrez 'break' pour quitter) :\n>>>")
    if data == "break":
        return "break"   
    name_file = str(input("Nom de l'image à enregistrer :\n>>>"))
    format_image = input("Choix du format fichier (0 =.jpg,1 = .png) :\n>>>")
    return data, name_file, format_image

while True:
    temp = MyQR() # var qui contient 'data' à convertir, nom du fichier et format
    if type(temp) == str: 
        if temp == "break": # la fonction 'MyQR()' renvoie "break" on stop le programme
            break
    else:
        img = qrcode.make(temp[0]) # convertion string to QRcode
        img.save(temp[1]+format[int(temp[2])]) # enregistrement de l'image image.png'nom + format'