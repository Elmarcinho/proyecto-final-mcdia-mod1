from models.model_image import ImageModel


class ImageController:
    def __init__(self):
        self.images = []
    
    def add_image(self, name, path):
        id_image = len(self.images) + 1
        new_image = ImageModel(id_image, name, path)
        self.images.append(new_image)

    def list_images(self):
        if not self.images:
            print("No hay imágenes registradas.")
            return
        for image in self.images:
            print(f"ID: {image.id}, Nombre: {image.name}, Ruta: {image.path}")
    
    def modify_image(self, id_image, new_name):
        for image in self.images:
            if image.id == id_image:
                image.name = new_name
                return True
        return False
    
    def delete_image(self, id_image):
        for image in self.images:
            if image.id == id_image:
                self.images.remove(image)
                return True
        return False
