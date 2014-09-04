#!/usr/bin/env python

import os

from skimage._build import cython

base_path = os.path.abspath(os.path.dirname(__file__))


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs

    config = Configuration('WTP', parent_package, top_path)
   # config.add_data_dir('tests')

    cython(['_perform_WTP.pyx'], working_path=base_path)
    WTP_sources = ['_perform_WTP.c', 'perform_WTP_ljmu.c']
    config.add_extension('_perform_WTP', sources=WTP_sources,
                         include_dirs=[get_numpy_include_dirs()])


    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(maintainer='scikit-image Developers',
          author='scikit-image Developers',
          maintainer_email='scikit-image@googlegroups.com',
          description='Restoration',
          url='https://github.com/scikit-image/scikit-image',
          license='SciPy License (BSD Style)',
          **(configuration(top_path='').todict())
          )
