Porting
=======

**Porting existing PIL2-based code to Pillow2**

Pillow2 is a functional drop-in replacement for the Python Imaging Library. To
run your existing PIL2-compatible code with Pillow2, it needs to be modified to
import the ``Image`` module from the ``PIL2`` namespace *instead* of the
global namespace. Change this::

    import Image

to this::

    from PIL2 import Image

The :py:mod:`_imaging` module has been moved. You can now import it like this::

    from PIL2.Image import core as _imaging

The image plugin loading mechanism has changed. Pillow2 no longer
automatically imports any file in the Python path with a name ending
in :file:`ImagePlugin.py`. You will need to import your image plugin
manually.

Pillow2 will raise an exception if the core extension can't be loaded
for any reason, including a version mismatch between the Python and
extension code. Previously PIL2 allowed Python only code to run if the
core extension was not available.
