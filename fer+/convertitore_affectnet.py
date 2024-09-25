import os
from PIL import Image

# Percorso alla cartella principale che contiene le 8 cartelle delle categorie
input_root_dir = r'C:\Users\aless\Desktop\affectnet'  # Percorso aggiornato

# Percorso alla cartella dove salvare le immagini convertite
output_root_dir = r'C:\Users\aless\Desktop\affectnet_converted'  # Puoi cambiare il nome della cartella di output se preferisci

# Lista delle categorie (nomi delle cartelle)
categories = ['Neutral', 'Happy', 'Sad', 'Surprise', 'Fear', 'Disgust', 'Anger', 'Contempt']

# Crea la cartella di output se non esiste
if not os.path.exists(output_root_dir):
    os.makedirs(output_root_dir)

for category in categories:
    input_dir = os.path.join(input_root_dir, category)
    output_dir = os.path.join(output_root_dir, category)
    
    # Crea la cartella per la categoria se non esiste
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Lista di tutti i file nella cartella della categoria
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        
        # Verifica che il file sia un'immagine supportata
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            try:
                # Apri l'immagine
                img = Image.open(input_path)
                
                # Converti in scala di grigi
                img = img.convert('L')
                
                # Ridimensiona a 48x48 usando Image.LANCZOS al posto di Image.ANTIALIAS
                img = img.resize((48, 48), Image.LANCZOS)
                
                # Percorso completo del file di output
                base_filename = os.path.splitext(filename)[0]
                output_filename = base_filename + '.png'
                output_path = os.path.join(output_dir, output_filename)
                
                # Salva l'immagine in formato PNG
                img.save(output_path, 'PNG')
                
            except Exception as e:
                print(f"Errore nel processare {input_path}: {e}")
        else:
            print(f"File {input_path} non è un'immagine supportata, saltato.")
