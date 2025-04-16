import os
import shutil
from models import ImageModel


class ImageController:
    def __init__(self):
        self.data_set = []
        self.images = []
        self.src_path = "/home/elmarcinho/Final_Project/models/dataset/images/covid_images"
        self.dst_path = "/home/elmarcinho/Final_Project/new_images/covid_images"
        self.src_path2 = "/home/elmarcinho/Final_Project/models/dataset/images/covid_masks"
        self.dst_path2 = "/home/elmarcinho/Final_Project/new_images/covid_masks"
    

    def register_image(self, image_file):

        image_name, extension = os.path.splitext(image_file)
        image_name = image_name.upper() + extension.lower()
        route_image = os.path.join(self.src_path, image_name)
        route_image2 = os.path.join(self.src_path2, image_name)

        if os.path.exists(route_image):
            shutil.copy(route_image, self.dst_path)
            shutil.copy(route_image2, self.dst_path2)
            id_image = len(self.images) + 1
            new_image = ImageModel(id_image, image_name, self.dst_path, self.dst_path2)
            self.images.append(new_image)
            return [self.dst_path, self.dst_path2]
        else:
            return


    def list_images(self):
        if not self.images:
            print("No hay imágenes registradas.")
            return
        for image in self.images:
            print(f"ID: {image.id}, Nombre: {image.name},\n Ruta1: {image.path},\n Ruta2: {image.path2}")
    
    
    def modify_image(self, id_image, image_file):

        image_name, extension = os.path.splitext(image_file)
        image_name = image_name.upper() + extension.lower()
        new_image_path = os.path.join(self.dst_path, image_name)
        new_image_path2 = os.path.join(self.dst_path2, image_name)

        for image in self.images:
            if image.id == id_image:
                current_image_path = os.path.join(image.path, image.name)
                current_image_path2 = os.path.join(image.path2, image.name)
                if os.path.exists(current_image_path):
                    os.rename(current_image_path, new_image_path)
                    os.rename(current_image_path2, new_image_path2)
                    image.name = image_name
                    return True
                else:
                    return False
        return False
    

    def delete_image(self, id_image):
        for image in self.images:
            if image.id == id_image:
                current_image_path = os.path.join(image.path, image.name)
                current_image_path2 = os.path.join(image.path2, image.name)
                if os.path.exists(current_image_path):
                    os.remove(current_image_path)
                    os.remove(current_image_path2)
                    self.images.remove(image)
                    return True
                else:
                    return False
        return False
