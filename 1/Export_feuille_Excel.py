from win32com import client
from PyPDF2 import PdfReader, PdfWriter , Transformation

app = client.DispatchEx("Excel.Application")
app.Interactive = False 
app.Visible = False

Chemin = input("Veuillez mettre ici le chemin allant vers le fichier Excel (.xlsx) : ")
print("Conversion en PDF, veuillze patienter ...!")
workbook = app.Workbooks.Open(Chemin)
#Imprimer la feuille active
#workbook.ActiveSheet.ExportAsFixedFormat(0,Chemin)
feuille = workbook.Worksheets("Nom de la feuille")  
resultat = feuille.ExportAsFixedFormat(0,Chemin)
workbook.Close()

# Charger le fichier PDF converti
reader = PdfReader(Chemin+".pdf")
page = reader.pages[0]

# Agrandir le contenu 
op = Transformation().scale(sx=1.0, sy=1.0)
page.add_transformation(op)

# Sauvegarder le nouveau fichier PDF
writer = PdfWriter()
writer.add_page(page)
writer.write("output.pdf")
print("Fichier converti en PDF avec succès")


