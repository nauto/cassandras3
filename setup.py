from setuptools import setup, find_packages

requires = [req for req in open('requirements.txt').read().splitlines()
            if not req.startswith('git')]

setup(name='cassandras3',
      version='0.0.1',
      description='Cassandra S3 Backup, List and Restore',
      long_description=open('README.md').read(),
      url='https://github.com/deviavir/cassandra-s3-backup-restore',
      author='Chase Sillevis',
      author_email='chase@sillevis.net',
      license='MIT',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=['test']),
      install_requires=requires,
      zip_safe=True)
