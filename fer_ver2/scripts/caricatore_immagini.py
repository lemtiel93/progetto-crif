import os
import pandas as pd
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt

class ImageLoader:
    def __init__(self, image_dir, csv_path):
        self.image_dir = image_dir
        self.csv_path = csv_path
    
    def load_image(self, image_path): # Funzione che apre immagine e la normalizza
        image = Image.open(image_path)
        image_array = img_to_array(image)
        #image_array /= 255
        return image_array
        
    def load_data(self):
        """Carica le immagini e le etichette dal CSV."""
        labels_df = pd.read_csv(self.csv_path)
        
        num_samples = labels_df.shape[0]
        images = np.empty((num_samples, 48, 48, 1), dtype=np.float32)  
        labels = np.empty((num_samples, labels_df.shape[1] - 3), dtype=np.float32)


        for index, row in labels_df.iterrows(): # Iterows restituisce index e ogni riga come series
            image_name = row['Image name']  # Nome dell'immagine nel csv
            image_path = os.path.join(self.image_dir, image_name) # Crea percorso immagine

            # Carica l'immagine
            images[index] = self.load_image(image_path)

            # Carica la distribuzione delle etichette
            # Normalizzo i valori della distrubuzione senno funzione perdita esplode
            labels[index] = row[2:11].values/10 # # Ignora la colonna 'image name' e 'dimensioni'
        # Converti le immagini e le etichette in array NumPy
        self.images = images
        self.labels = labels
        

        return self.images, self.labels
    
    def random_image(self, num_images=9):
        random_indices = np.random.choice(self.images.shape[0], num_images, replace=False)

        plt.figure(figsize=(5, 5))
        
        for i, idx in enumerate(random_indices):
            plt.subplot(1, num_images, i + 1)
            plt.imshow(self.images[idx].reshape(48, 48), cmap='gray')  # Rimuovi il canale dei colori se in scala di grigi
            plt.title(f'Label: {np.argmax(self.labels[idx])}')  # Mostra l'argmax dell'etichetta corrispondente
            plt.axis('off')

        plt.tight_layout()
        plt.show()
