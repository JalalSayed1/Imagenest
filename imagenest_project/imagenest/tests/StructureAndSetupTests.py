import os
from django.test import TestCase

class StructureAndSetupTests(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.imagenest_app_dir = os.path.join(self.project_base_dir, 'imagenest')
        self.imagenest_project_dir = os.path.join(self.project_base_dir, 'imagenest_project')
        self.imagenest_static_dir = os.path.join(self.project_base_dir, 'static')
        self.imagenest_templates_dir = os.path.join(self.project_base_dir, 'templates', 'imagenest')

    
    def test_directories(self):
        imagenest_directory_exists = os.path.isdir(self.imagenest_app_dir)
        imagenest_project_directory_exists = os.path.isdir(self.imagenest_project_dir)
        static_directory_exists = os.path.isdir(self.imagenest_static_dir)
        templates_directory_exists = os.path.isdir(self.imagenest_templates_dir)

        self.assertTrue(imagenest_directory_exists)
        self.assertTrue(imagenest_directory_exists)
        self.assertTrue(imagenest_directory_exists)
        self.assertTrue(imagenest_directory_exists)


    def test_imagenest_project_directory(self):
        init_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, '__init__.py'))
        manage_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, 'manage.py'))
        settings_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, 'settings.py'))
        urls_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, 'urls.py'))
        wsgi_module_exists = os.path.isfile(os.path.join(self.imagenest_project_dir, 'wsgi.py'))

        self.assertTrue(init_module_exists, "The __init__.py file is missing from the imagenest_project directory.")
        self.assertTrue(manage_module_exists, "The manage.py file is missing from the imagenest_project directory.")
        self.assertTrue(settings_module_exists, "The settings.py file is missing from the imagenest_project directory.")
        self.assertTrue(urls_module_exists, "The urls.py file is missing from the imagenest_project directory.")
        self.assertTrue(wsgi_module_exists, "The wsgi.py file is missing from the imagenest_project directory.")

    def test_imagenest_directory(self):
       init_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, '__init__.py'))
       admin_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'admin.py'))
       apps_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'apps.py'))
       forms_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'forms.py'))
       models_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'models.py'))
       urls_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'urls.py'))
       views_module_exists = os.path.isfile(os.path.join(self.imagenest_app_dir, 'views.py'))

       self.assertTrue(init_module_exists, "The __init__.py file is missing from the imagenest directory.")
       self.assertTrue(admin_module_exists, "The admin.py file is missing from the imagenest directory.")
       self.assertTrue(apps_module_exists, "The apps.py file is missing from the imagenest directory.")
       self.assertTrue(forms_module_exists, "The forms.py file is missing from the imagenest directory.")
       self.assertTrue(models_module_exists, "The models.py file is missing from the imagenest directory.")
       self.assertTrue(urls_module_exists, "The urls.py file is missing from the imagenest directory.")
       self.assertTrue(views_module_exists, "The views.py file is missing from the imagenest directory.")

    def test_templates_directory(self):
       base_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'base.html'))
       first_page_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'first_page.html'))
       profile_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'profile.html'))
       home_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'home.html'))
       login_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'login.html'))
       logout_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'logout.html'))
       menu_pages_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'menu_pages_template.html'))
       register_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'register.html'))
       search_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'search.html'))
       top_images_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'top_images.html'))
       upload_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'upload.html'))

       self.assertTrue(base_template_exists, "The base.html template is missing from the templates directory.")
       self.assertTrue(first_page_template_exists, "The first_page.html template is missing from the templates directory.")
       self.assertTrue(profile_template_exists, "The profile.html template is missing from the templates directory.")
       self.assertTrue(home_template_exists, "The home.html template is missing from the templates directory.")
       self.assertTrue(login_template_exists, "The login.html template is missing from the templates directory.")
       self.assertTrue(logout_template_exists, "The logout.html template is missing from the templates directory.")
       self.assertTrue(menu_pages_template_exists, "The menu_pages_template.html template is missing from the templates directory.")
       self.assertTrue(register_template_exists, "The register.html template is missing from the templates directory.")
       self.assertTrue(search_template_exists, "The search.html template is missing from the templates directory.")
       self.assertTrue(top_images_template_exists, "The top_images.html template is missing from the templates directory.")
       self.assertTrue(upload_template_exists, "The upload.html template is missing from the templates directory.")

    def test_forms_exist(self):
        import imagenest.forms
        self.assertTrue('LoginForm' in dir(imagenest.forms), "The LoginForm class could not be found in forms.py")
        self.assertTrue('ImageUploadForm' in dir(imagenest.forms), "The ImageUploadForm class could not be found in forms.py")
        self.assertTrue('SearchForm' in dir(imagenest.forms), "The SearchForm class could not be found in forms.py")
