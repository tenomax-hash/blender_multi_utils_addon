from ast import ExceptHandler
import bpy


class View3DPanel:
    """Base class for Panel Module"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "New Tool"
    bl_options = {'DEFAULT_CLOSED'}


class VIEW_PT_PanelOne(View3DPanel, bpy.types.Panel):
    """class for panelone"""
    bl_idname = "VIEW_PT_paneltwo"
    bl_label = "Mulit Utils"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='HOLDOUT_OFF')

    def draw(self, context):
        # obj = context.object
        obj = context.object
        obj_prop = obj.my_obj_prop
        layout = self.layout
        box = layout.box()
        box.label(text="Multipupose", icon='OUTLINER_OB_LIGHTPROBE')
        box = box.column(align=True)
        box.prop(obj_prop, "boo_obj", icon='MOD_PARTICLE_INSTANCE')
        # box.prop(obj, "name", icon='CUBE', text="Act_obj")
        box.prop(obj_prop, "str_obj_val", icon='CON_DISTLIMIT')
        box.prop(obj_prop, "str_obj_suffix", icon='CON_DISTLIMIT')
        box.prop(obj_prop, "data_type_enum", )
        box.operator("object.renameopt", text="Batch Rename")


class Panel_PT_Two(View3DPanel, bpy.types.Panel):
    """class for creating pannel for batchrenames"""

    bl_idname = "VIEW_3D_PT_paneltwo"
    bl_label = "Object Props"

    def draw_header(self, context):

        layout = self.layout
        layout.label(text="", icon="HOLDOUT_OFF")

    def draw(self, context):
        """darw function for drawing classes"""
        # scn = context.scene
        # rname_prop = scn.rename_props
        obj = context.object
        # obj_prop = obj.my_obj_prop
        layout = self.layout
        box = layout.box()
        # box.label(text="Object", icon="OUTLINER_OB_LIGHTPROBE")
        # box = layout.box()
        box.label(text="Object Props", icon="MOD_HUE_SATURATION")
        box = box.column(align=True)
        box.operator_menu_enum("object.modifier_add",
                               "type", icon="MODIFIER_OFF")
        box.operator_menu_enum(
            "object.constraint_add",
            "type",
            text="Add Object Constraint",
            icon="CON_KINEMATIC",
        )
        box = box.split()
        box = box.column()
        box.label(text="ViewPort Display", icon="RESTRICT_VIEW_ON")
        box = box.split()
        box = box.column(align=True)
        box.prop(obj, "show_wire")
        box.prop(obj, "show_all_edges")
        box.prop(obj.display, "show_shadows")
        box.prop(obj, "show_in_front")
        # box.prop(obj.data, "use_auto_smooth")

        box.prop(obj, "display_type")
        box.prop(obj, "color")


blender_panel_classes = (VIEW_PT_PanelOne, Panel_PT_Two)


def register():
    for cls in blender_panel_classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in blender_panel_classes:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
