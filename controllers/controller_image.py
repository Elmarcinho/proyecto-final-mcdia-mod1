import os
import shutil
import pandas as pd
from models import ImageModel
from pathlib import Path


class ImageController:
    def __init__(self):
        self.dataset = []
        self.images = []
        base_path = Path(__file__).resolve().parent.parent  # Subes dos niveles a la carpeta del proyecto
       
        self.src_path = base_path / "models" / "dataset" / "images" / "covid_images"
        self.dst_path = base_path / "new_images" / "covid_images"
        self.src_path2 = base_path / "models" / "dataset" / "images" / "covid_masks"
        self.dst_path2 =  base_path / "new_images" / "covid_masks"
        
        #self.src_path = "/home/elmarcinho/Final_Project/models/dataset/images/covid_images"
        #self.dst_path = "/home/elmarcinho/Final_Project/new_images/covid_images"
        #self.src_path2 = "/home/elmarcinho/Final_Project/models/dataset/images/covid_masks"
        #self.dst_path2 = "/home/elmarcinho/Final_Project/new_images/covid_masks"
       
    

    def load_dataset(self):
        base_path = Path(__file__).resolve().parent.parent  # Subes dos niveles a la carpeta del proyecto
        df = pd.read_csv(base_path / "models" / "dataset" / "COVID.metadata.csv", delimiter=";")
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
            self.images.append(new_image)
            print(self.images)
            return [self.dst_path, self.dst_path2]
        else:
            return


    def list_images(self):
        if not self.images:
            print("No hay imágenes registradas.")
            return
        for image in self.images:
            print(f"ID: {image.id}, Nombre: {image.file_name}, Size: {image.size} , Url: {image.url} ,\n Ruta1: {image.path},\n Ruta2: {image.path2}")
    
    
    def modify_image(self, id_image, file_image, size, url):

        image_name, extension = os.path.splitext(file_image)
        image_name = image_name.upper() + extension.lower()
        new_image_path = os.path.join(self.dst_path, image_name)
        new_image_path2 = os.path.join(self.dst_path2, image_name)

        for image in self.images:
            if image.id == id_image:
                current_image_path = os.path.join(image.path, image.file_name)
                current_image_path2 = os.path.join(image.path2, image.file_name)
                if os.path.exists(current_image_path) and os.path.exists(current_image_path2):
                    os.rename(current_image_path, new_image_path)
                    os.rename(current_image_path2, new_image_path2)
                    image.file_name = image_name
                    image.size = size
                    image.url = url
                    return True
                else:
                    return False
        return False
    

    def delete_image(self, id_image):
        for image in self.images:
            if image.id == id_image:
                current_image_path = os.path.join(image.path, image.file_name)
                current_image_path2 = os.path.join(image.path2, image.file_name)
                if os.path.exists(current_image_path):
                    os.remove(current_image_path)
                    os.remove(current_image_path2)
                    self.images.remove(image)
                    return True
                else:
                    return False
        return False
