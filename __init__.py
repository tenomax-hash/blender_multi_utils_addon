# import modules directly from package
from .z_operator import otype
from .z_panel import ptype
from .z_property import protype
# from .z_keymaps import keytype
import bpy
bl_info = {
    'name': "Multi Utility Addons",
    'description': "This Addon for Multi Purpose Utility Functions.",
    'author': "Manu Manohar & Devansh Manu",
    'version': (1, 0, 0),
    'blender': (3, 0, 0),
    'location': ' View3D > Manuz',
    'category': 'Object',
}


if 'bpy' in locals():
    import importlib
    importlib.reload(z_operator.otype)
    importlib.reload(z_panel.ptype)
    importlib.reload(z_property.protype)
    # importlib.reload(z_keymaps.keytype)
else:
    #import bpy
    # from z_operator.otype import z_operator.otype
    from .z_operator import otype
    from .z_panel import ptype
    from .z_property import protype
    # from .z_keymaps import keytype


def register():
    otype.register()
    ptype.register()
    protype.register()


def unregister():
    otype.unregister()
    ptype.unregister()
    protype.unregister()


if __name__ == '__main__':
    register()

