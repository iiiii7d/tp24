from setuptools import setup
import tp24

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'tp24',
  packages = ['tp24'],
  version = tp24.__version__+"",
  license ='gpl-3.0',
  description = 'Leaflet.js streetmap tile renderer',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = '7d',
  author_email = 'i.third.7d@protonmail.com',
  url = 'https://github.com/iiiii7d/tp24',
  download_url = f'https://github.com/iiiii7d/tp24/archive/refs/tags/v{tp24.__version__}.tar.gz',
  keywords = ['leaflet', 'leaflet.js', 'leafletjs', 'map', 'tiles', 'renderer', 'tile-renderer', 'mapping'],
  python_requires='',
  package_data={
    'tp24': ['model/*'],
  },
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Utilities'
  ],
)