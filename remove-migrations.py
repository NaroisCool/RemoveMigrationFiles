import os

for root, dirs, files in os.walk('C:/Users/Naro/Desktop/project/yc_court'):
    if 'migrations' in dirs and 'venv' not in root:
        migrations = os.path.join(root, 'migrations')
        for file in os.listdir(migrations):
            migration = os.path.join(migrations, file)
            if os.path.isfile(migration) and file != '__init__.py':
                os.remove(migration)
