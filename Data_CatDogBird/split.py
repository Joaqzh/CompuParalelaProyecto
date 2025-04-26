import os

# Definir las rutas de las carpetas
base_dir = '.'  # Directorio base donde está el script
train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')

# Listado de categorías
categories = ['bird', 'dog', 'cat']

# Función para contar imágenes en una carpeta
def count_images_in_folder(folder_path):
    return len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

# Validar el conteo de imágenes en train y test
for category in categories:
    category_train_dir = os.path.join(train_dir, category)
    category_test_dir = os.path.join(test_dir, category)
    
    # Contar imágenes en cada carpeta
    train_count = count_images_in_folder(category_train_dir)
    test_count = count_images_in_folder(category_test_dir)
    
    print(f"Categoría: {category}")
    print(f"  Imágenes en train/{category}: {train_count}")
    print(f"  Imágenes en test/{category}: {test_count}")
    print("-" * 40)
