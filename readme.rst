This is based on :code:`mesonpep517`, following `this link <https://thiblahute.gitlab.io/mesonpep517/>`_

Install
=======

Install by either

.. code::
   > meson builddir
   > meson install -C builddir

or

.. code::
   > pip install .

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


   
