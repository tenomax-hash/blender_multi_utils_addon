import bpy

addon_keymaps = []

# bl_idname passes into idname in key_map_invoke_operator


def key_map_invoke_operator(idname, **kwargs):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new(
            idname,
            type=kwargs["type"],
            value=kwargs["value"],
            shift=kwargs["shift"],
            ctrl=kwargs["ctrl"],
        )
        addon_keymaps.append((km, kmi))


def key_map_invoke_clear():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
