I have tried several possible methods trying to use setuptools.
None of them was a complete success. I have uploaded only the best I could achieve using a :code:`setup.py` script.
This is shown in the :code:`meson-build` branch of this repository.
In that case, by overriding the setuptool build command (actually the parent distutils command), I managed to make meson work.
Unfortunately the installed files (which are nicely structured in the posix way of doing things):

.. code::
   
   ${PREFIX}
   ├── include
   │   ├── c_custom_pack.h
   │   └── custom_pack.h
   └── lib
       ├── libc_custom_pack.so
       ├── libcustom_pack.so
       └── python3.8
           └── site-packages
                └── custpy
                    ├── cust.py
                    ├── __init__.py
                    └── internal
                        ├── cwrap.py
                        └── __init__.py

are not tracked by the higher level build system (pip using setuptools).
The funny thing though, is that it is easy to import the package and make it work, as long as ${PREFIX}/lib is in your linker search path and ${PREFIX}/lib/pythonX.Y/site-packages is in your python-path.
			
This is when I changed approach. This was a ''success'', meaning that by modifying (massively) the meson build scripts I managed to make it work smoothly.
This is based on :code:`mesonpep517`, following `this link <https://thiblahute.gitlab.io/mesonpep517/>`_

The two main features are

- toml file for configuring the packaging
- the libraries are made static (for the c++ sector) and dynamic (for the c-wrap). In this way when importing the CTypes-using sub-module (`custpy/internal/cwrap.py`_) the system does not have to use the linker to search for shared objects.

This is not the best possible solution but it is working.

Install
=======

Install by either

.. code::
   > meson builddir
   > meson install -C builddir

or

.. code::
   > pip install .

The former assumes the custom boolean build option (defined in `meson_options.txt`_) :code:`full-build` to evalueate :code:`true`.
A ``classic'' installation is performed.
The latter instead sets :code:`full-build=false` (see the toml configuration file) and thus almost everything is built static inside the :code:`internal` sub-package.

Upload to PyPI
==============

First create a distribution: from the root directory run

.. code::
   > python3 -m pep517.build .

This will add a tarball and a sha256 file to the :code:`dist/` sub-directory.

Then use :code:`twine` to publish the package:

.. code::
   > twine upload dist/*

To upload a new release you should first remove the previous one:

.. code::
   > rm dist/* && python3 -m pep517.build && twine upload dist/*


   
