import numpy as np
import pandas 

def load_and_split(path):

    df = pandas.read_csv(path)
    dataset = df['pixels'].apply(lambda x: np.fromstring(x, sep=' ', dtype=int)).values
    dataset = np.stack(dataset).reshape(-1, 48, 48, 1)
    dataset_labels = df.drop(['pixels', 'usage'], axis=1)
    dataset_labels = dataset_labels.to_numpy()

    train_indices = df[df['usage'] == 'train'].index
    val_indices = df[df['usage'] == 'val'].index
    test_indices = df[df['usage'] == 'test'].index

    x_train = dataset[train_indices]
    y_train = dataset_labels[train_indices]
    x_val = dataset[val_indices]
    y_val = dataset_labels[val_indices]
    x_test = dataset[test_indices]
    y_test = dataset_labels[test_indices]

    return (x_train,y_train),(x_val,y_val),(x_test,y_test)