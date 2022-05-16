import bpy
# from .z_dcollections import *
# from ..z_functions.objfunction import data_types
# This module for batch object renaming
from ..z_datatypes.dtype import *


def rename_sel_by_type(context, name, suffix, dtype):
    sel_obj_list = []
    objects = context.selected_objects
    for obj in objects:
        if obj.type == data_types[dtype]:
            sel_obj_list.append(obj)
            # print(sel_obj_list)
            for i, obj in enumerate(sel_obj_list, start=1):
                if obj.type != "EMPTY" and obj.type != "META":
                    obj.name = name + suffix + str(i)
                    obj.data.name = name + suffix + str(i)
                elif obj.type == data_types["E10"]:
                    obj.name = name + suffix + str(i)

                else:
                    print("do nothing!")


# This function is select by type


def select_by_type(context, enum_prop, dtypes):
    print(dtypes[enum_prop])

    bpy.ops.object.select_by_type(type=dtypes[enum_prop])
