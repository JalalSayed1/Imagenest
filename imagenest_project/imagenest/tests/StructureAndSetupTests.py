import os
from django.test import TestCase

class StructureAndSetupTests(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.imagenest_app_dir = os.path.join(self.project_base_dir, 'imagenest')
        self.imagenest_project_dir = os.path.join(self.project_base_dir, 'imagenest_project')
        self.imagenest_static_dir = os.path.join(self.project_base_dir, 'static')
        self.imagenest_templates_dir = os.path.join(self.project_base_dir, 'templates', 'imagenest')

    ## test each directory exists

    def test_imagenest_directory(self):
        imagenest_directory_exists = os.path.isdir(self.imagenest_app_dir)#
        self.assertTrue(imagenest_directory_exists, "The imagenest directory does not exist.")
    
    def test_imagenest_project_directory(self):
        imagenest_project_directory_exists = os.path.isdir(self.imagenest_project_dir)
        self.assertTrue(imagenest_project_directory_exists, "The imagenest project directory does not exist.")

    def test_static_directory(self):
        static_directory_exists = os.path.isdir(self.imagenest_static_dir)
        self.assertTrue(static_directory_exists, "The static directory does not exist.")
    
    def test_templates_directory(self):
        templates_directory_exists = os.path.isdir(self.imagenest_templates_dir)        
        self.assertTrue(templates_directory_exists, "The templates directory does not exist.")

    
    ## test imagenest project and app directory contain the correct files

    def test_init_module_in_project_dir(self):
        init_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, '__init__.py'))
        self.assertTrue(init_module_exists, "The __init__.py file is missing from the imagenest_project directory.")

    def test_settings_module_in_project_dir(self):
        settings_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, 'settings.py'))
        self.assertTrue(settings_module_exists, "The settings.py file is missing from the imagenest_project directory.")

    def test_urls_module_in_project_dir(self):
        urls_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, 'urls.py'))
        self.assertTrue(urls_module_exists, "The urls.py file is missing from the imagenest_project directory.")

    def test_wsgi_module_in_project_dir(self):
        wsgi_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, 'wsgi.py'))
        self.assertTrue(wsgi_module_exists, "The wsgi.py file is missing from the imagenest_project directory.")

    
    def test_init_module_in_app_dir(self):
        init_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, '__init__.py'))
        self.assertTrue(init_module_exists, "The __init__.py file is missing from the imagenest directory.")
    
    def test_init_module_in_app_dir(self):
        admin_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'admin.py'))
        self.assertTrue(admin_module_exists, "The admin.py file is missing from the imagenest directory.")
    
    def test_init_module_in_app_dir(self):
        apps_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'apps.py'))
        self.assertTrue(apps_module_exists, "The apps.py file is missing from the imagenest directory.")

    def test_init_module_in_app_dir(self):
        forms_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'forms.py'))
        self.assertTrue(forms_module_exists, "The forms.py file is missing from the imagenest directory.")
    
    def test_models_module_in_app_dir(self):
        models_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'models.py'))
        self.assertTrue(models_module_exists, "The models.py file is missing from the imagenest directory.")

    def test_init_module_in_app_dir(self):
        urls_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'urls.py'))
        self.assertTrue(urls_module_exists, "The urls.py file is missing from the imagenest directory.")

    def test_init_module_in_app_dir(self):
        views_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'views.py'))
        self.assertTrue(views_module_exists, "The views.py file is missing from the imagenest directory.")
