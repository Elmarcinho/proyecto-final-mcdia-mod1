import json
import os

from models import ImageModel


# Storage represents the dictionary (persistency)
class Storage:
    STORAGE = "storage.json"

    def load_storage(self):
        if not os.path.exists(self.STORAGE):
            return []
        with open(self.STORAGE, "r") as storage:
            return json.load(storage)
        
    def save_storage(self, data):
        with open(self.STORAGE, "w") as storage:
            json.dump(data, storage, indent=4)

    def register_image(self, image: ImageModel):
        storage = self.load_storage()
        storage.append({
            "id": image.id,
            "file_name": image.file_name,
            "format": image.format,
            "size": image.size,
            "url": image.url,
            "path": image.path,
            "path2": image.path2
        })

        self.save_storage(storage)

    def remove_image(self, image):
        storage = self.load_storage()
        storage.remove(image)

        self.save_storage(storage)