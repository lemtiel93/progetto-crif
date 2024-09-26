import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf

# Funzione per caricare, convertire e preprocessare le immagini
def preprocess_images(image_folder, target_size=(48, 48)):
    images = []
    file_names = []
    
    # Scorri tutti i file nella cartella
    for file_name in os.listdir(image_folder):
        if file_name.endswith(('.png', '.jpg', '.jpeg', '.bmp')):  # Controllo per vari formati di immagine
            img_path = os.path.join(image_folder, file_name)
            img = Image.open(img_path).convert('L')  # Converte l'immagine in scala di grigi
            img = img.resize(target_size)  # Ridimensiona a 48x48
            img_array = img_to_array(img)  
            images.append(img_array)
            file_names.append(file_name)
    
    images = np.array(images)
    images = np.expand_dims(images, -1)  
    
    return images, file_names

# Funzione per predire e stampare le immagini con le predizioni
def predict_and_display(model, images, file_names, class_labels):
    predictions = model.predict(images)
    pred_classes = np.argmax(predictions, axis=1)  # Prendi la classe predetta con la probabilità più alta

    # Visualizzazione delle immagini con le predizioni
    plt.figure(figsize=(12, 12))
    
    for i in range(len(images)):
        plt.subplot(4, 4, i + 1)  # Cambia il numero di immagini da visualizzare a seconda delle necessità
        plt.imshow(images[i].reshape(48, 48), cmap='gray')
        pred_label = class_labels[pred_classes[i]]
        plt.title(f'Pred: {pred_label}')
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Configurazione del percorso delle immagini e delle classi
image_folder = 'foto-mie'  # Sostituisci con il percorso della cartella che contiene le immagini
class_labels = ['Neutral', 'Happiness', 'Surprise', 'Sadness', 'Anger', 'Disgust', 'Fear', 'Contempt', 'Unknown']  # Le etichette delle classi

# Caricamento delle immagini
images, file_names = preprocess_images(image_folder)


model = tf.keras.models.load_model('trained_bestmodel.keras')  

# Predizione e visualizzazione
predict_and_display(model, images, file_names, class_labels)