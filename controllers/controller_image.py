import os
import shutil
import pandas as pd
from models import ImageModel
from data import Storage

storage = Storage()

class ImageController:
    def __init__(self):
        self.images = storage.load_storage()
        self.src_path = "/home/elmarcinho/Final_Project/images/covid_images"
        self.dst_path = "/home/elmarcinho/Final_Project/images/new_images/covid_images"
        self.src_path2 = "/home/elmarcinho/Final_Project/images/covid_masks"
        self.dst_path2 = "/home/elmarcinho/Final_Project/images/new_images/covid_masks"
        self.dataset = []
    

    def load_dataset(self):
        df = pd.read_csv("/home/elmarcinho/Final_Project/models/dataset/COVID.metadata.csv", delimiter=";")
        self.dataset = df.to_dict("records")


    def search_image(self, file_name):
        if self.dataset == []:
            self.load_dataset()

        for image in self.dataset:
            if image["FILE NAME"] == file_name:
                return True
        return False
    
    def register_image(self, file_image, size, url):

        image_name, extension = os.path.splitext(file_image)
        image_format = extension[1:].upper()

        exists_image = self.search_image(image_name.upper())

        image_name = image_name.upper() + extension.lower()
        route_image = os.path.join(self.src_path, image_name)
        route_image2 = os.path.join(self.src_path2, image_name)

        if os.path.exists(route_image) and exists_image:
            shutil.copy(route_image, self.dst_path)
            shutil.copy(route_image2, self.dst_path2)
            id_image = len(self.images) + 1
            new_image = ImageModel(id_image, image_name, image_format, size, url, self.dst_path, self.dst_path2)
            
            storage.register_image(new_image)
            
            return [self.dst_path, self.dst_path2]
        else:
            return


    def list_images(self):
        self.images = storage.load_storage()

        if not self.images:
            print("No hay imágenes registradas.")
            return
        
        for image in self.images:
            print(f"ID: {image['id']}, Nombre: {image['file_name']}, Size: {image['size']} , Url: {image['url']} ,\n Ruta1: {image['path']},\n Ruta2: {image['path2']}")
    
    
    def modify_image(self, id_image, file_image, size, url):

        image_name, extension = os.path.splitext(file_image)
        image_name = image_name.upper() + extension.lower()
        new_image_path = os.path.join(self.dst_path, image_name)
        new_image_path2 = os.path.join(self.dst_path2, image_name)

        self.images = storage.load_storage()

        for image in self.images:
            if image['id'] == int(id_image):
                current_image_path = os.path.join(image['path'], image['file_name'])
                current_image_path2 = os.path.join(image['path2'], image['file_name'])
                if os.path.exists(current_image_path) and os.path.exists(current_image_path2):
                    os.rename(current_image_path, new_image_path)
                    os.rename(current_image_path2, new_image_path2)
                    image['file_name'] = image_name
                    image['size'] = size
                    image['url'] = url

                    storage.save_storage(self.images)

                    return True
                else:
                    return False
        return False
    

    def delete_image(self, id_image):
        for image in self.images:
            if image['id'] == int(id_image):
                current_image_path = os.path.join(image['path'], image['file_name'])
                current_image_path2 = os.path.join(image['path2'], image['file_name'])
                if os.path.exists(current_image_path):
                    os.remove(current_image_path)
                    os.remove(current_image_path2)
                    
                    storage.remove_image(image)

                    return True
                else:
                    return False
        return False
