import bpy
from ..z_datatypes.dtype import item_enum_dtypes

class MyObjectCustomProperty(bpy.types.PropertyGroup):
    # obj = bpy.context.object
    """Class for creating custom properties to the objects."""
    # str_obj_name: bpy.props.StringProperty(name="@", default='Manuz')
    # item_enum_prop: bpy.props.EnumProperty(name=, items=item_enum1)
    str_obj_val: bpy.props.StringProperty(name="Name", default="@value")
    boo_obj: bpy.props.BoolProperty(name="Select")
    # fl_obj: bpy.props.FloatProperty(name="Float value")
    str_obj_suffix: bpy.props.StringProperty(name="Suffix", default="_")
    data_type_enum: bpy.props.EnumProperty(name="dtypes",items=item_enum_dtypes)


blnd_property_classes = (MyObjectCustomProperty,)


def register():
    for cls in blnd_property_classes:
        bpy.utils.register_class(cls)
    bpy.types.Object.my_obj_prop = bpy.props.PointerProperty(
        type=MyObjectCustomProperty)


def unregister():
    for cls in blnd_property_classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Object.my_obj_prop


if __name__ == '__main__':
    register()
