import bpy

# from z_property.protype import MyObjectCustomProperty
from ..z_keymaps.keytype import *
from ..z_functions.objfunction import *
# from ..z_datatypes.dtype import *


class OBJECT_OT_Button_ok(bpy.types.Operator):
    """Operator class for invoke Button"""
    bl_idname = "object.operok"
    bl_label = "Property"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def execute(self, context):
        print('execution complted!')
        return {'FINISHED'}

    def draw(self, context):
        obj = context.object
        layout = self.layout
        box = layout.box()
        box.label(text="Object Props", icon='NODE_MATERIAL')
        box = layout.box()
        box.prop(obj, "name")
        box.prop(obj, "location")
        box.prop(obj, "dimensions")
        # pass

    def invoke(self, context, event):
        wm = context.window_manager
        wm.invoke_props_dialog(self, width=125)
        return {'RUNNING_MODAL'}


class OBJECT_OT_renamepanel(bpy.types.Operator):
    """Rename operator"""

    bl_idname = "object.renameopt"
    bl_label = "Batch Rename"
    bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        obj = context.object
        myprops = obj.my_obj_prop
        # print("Temp operator")
        if myprops.boo_obj == True:
            select_by_type(context, myprops.data_type_enum, data_types)

        else:
            rename_sel_by_type(
                context,
                myprops.str_obj_val,
                myprops.str_obj_suffix,
                myprops.data_type_enum,
            )

        print("Execution completed")
        return {"FINISHED"}


class OBJECT_OT_invokeopt(bpy.types.Operator):
    """Invoke class Operator"""

    bl_idname = "object.invokeopt"
    bl_label = "Invoke Batch Rename"
    bl_options = {"REGISTER", "UNDO"}

    """Adding Class variables"""
    string_value: bpy.props.StringProperty(
        name="Name",
        default="@",
    )
    string_suffix: bpy.props.StringProperty(
        name="suffix",
        default="_",
    )
    dtype_enum: bpy.props.EnumProperty(name="Dtypes", items=item_enum_dtypes)

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):

        rename_sel_by_type(
            context, self.string_value, self.string_suffix, self.dtype_enum
        )

        print("execution complted!")
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


blender_opt_classes = (OBJECT_OT_Button_ok,
                       OBJECT_OT_renamepanel, OBJECT_OT_invokeopt,)


def register():
    for cls in blender_opt_classes:
        bpy.utils.register_class(cls)
    key_map_invoke_operator(
        "object.operok", type="F5", value="PRESS", shift=False, ctrl=False
    )
    key_map_invoke_operator("object.invokeopt", type="F6",
                            value="PRESS", shift=False, ctrl=False)


def unregister():
    for cls in blender_opt_classes:
        bpy.utils.unregister_class(cls)
    key_map_invoke_clear()


if __name__ == '__main__':
    register()
