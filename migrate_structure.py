import os
import shutil
from pathlib import Path

def create_directories(base_path):
    """Tworzy nową strukturę katalogów"""
    directories = [
        'docs',
        'backend/app/routes',
        'backend/migrations/versions',
        'backend/tests',
        'backend/logs',
        'frontend/public',
        'frontend/src/components/__tests__',
        'frontend/src/pages',
        'frontend/src/services/__tests__',
        'frontend/src/utils',
        'scripts'
    ]
    
    for directory in directories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

def move_files(base_path):
    """Przenosi pliki do nowej struktury z walidacją"""
    # Konsolidacja dokumentacji
    docs_content = []
    for doc_file in ['backend_setup_instructions.md', 
                    'frontend_setup_instructions.md',
                    'testing_setup_instructions.md']:
        src_path = os.path.join(base_path, doc_file)
        if os.path.exists(src_path):
            with open(src_path, 'r') as f:
                docs_content.append(f.read())
            os.remove(src_path)
    
    if docs_content:
        setup_path = os.path.join(base_path, 'docs', 'setup.md')
        with open(setup_path, 'w') as f:
            f.write("# Kompleksowa dokumentacja projektu\n\n")
            f.write("\n\n".join(docs_content))

    # Backend - główna aplikacja
    backend_files = [
        ('zakupy_app/__init__.py', 'backend/app/__init__.py'),
        ('zakupy_app/models.py', 'backend/app/models.py'),
        ('zakupy_app/routes.py', 'backend/app/routes/routes.py'),
        ('zakupy_app/extensions.py', 'backend/app/extensions.py'),
        ('zakupy_app/config.py', 'backend/app/config.py'),
        ('requirements.txt', 'backend/requirements.txt'),
        ('setup.py', 'backend/setup.py'),
        ('logs/zakupy.log', 'backend/logs/zakupy.log')
    ]
    
    for src, dst in backend_files:
        src_path = os.path.join(base_path, src)
        if os.path.exists(src_path):
            shutil.move(src_path, os.path.join(base_path, dst))
        else:
            print(f"Ostrzeżenie: Brak pliku {src} - pomijam")

    # Frontend
    frontend_files = [
        ('zakupy-frontend/public/favicon.ico', 'frontend/public/favicon.ico'),
        ('zakupy-frontend/public/index.html', 'frontend/public/index.html'),
        ('zakupy-frontend/src/App.js', 'frontend/src/App.js'),
        ('zakupy-frontend/src/index.js', 'frontend/src/index.js'),
        ('zakupy-frontend/src/components/Header.js', 'frontend/src/components/Header.js'),
        ('zakupy-frontend/src/components/ParagonForm.js', 'frontend/src/components/ParagonForm.js'),
        ('zakupy-frontend/src/components/__tests__/Header.test.js', 'frontend/src/components/__tests__/Header.test.js'),
        ('zakupy-frontend/src/services/api.js', 'frontend/src/services/api.js'),
        ('zakupy-frontend/src/services/__tests__/api.test.js', 'frontend/src/services/__tests__/api.test.js'),
        ('zakupy-frontend/package.json', 'frontend/package.json'),
        ('zakupy-frontend/package-lock.json', 'frontend/package-lock.json'),
        ('zakupy-frontend/jest.config.js', 'frontend/jest.config.js')
    ]
    
    for src, dst in frontend_files:
        src_path = os.path.join(base_path, src)
        if os.path.exists(src_path):
            shutil.move(src_path, os.path.join(base_path, dst))
        else:
            print(f"Ostrzeżenie: Brak pliku {src} - pomijam")

def cleanup(base_path):
    """Bezpieczne czyszczenie starej struktury"""
    obsolete_dirs = [
        'zakupy_app',
        'zakupy_app.egg-info',
        'zakupy-frontend'
    ]
    
    for directory in obsolete_dirs:
        dir_path = os.path.join(base_path, directory)
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"Usunięto: {dir_path}")

def main():
    base_path = Path(__file__).parent
    create_directories(base_path)
    move_files(base_path)
    cleanup(base_path)
    print("Migracja zakończona!")

if __name__ == "__main__":
    main()