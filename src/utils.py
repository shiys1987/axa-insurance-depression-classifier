import pickle


def pickle_save(file_path: str, pickle_obj):
    """
    Save pickle objects into local file
    """
    with open(file_path, "wb") as file:
        pickle.dump(pickle_obj, file)


def pickle_load(file_path: str):
    """
    Load saved pickle objects from provided file_path
    """
    with open(file_path, 'rb') as file:  
        pickle_obj = pickle.load(file)
    
    return pickle_obj