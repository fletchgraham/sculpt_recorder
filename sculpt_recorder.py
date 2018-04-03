
import bpy
import bmesh
from bpy_extras import object_utils

def record(context):
    
    # go to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    ob = bpy.context.object
    
    # add decimate mod
    #bpy.ops.object.modifier_add(type='DECIMATE')
    #ob.modifiers["Decimate"].ratio = 0.3

    # duplicate object
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
    
    # remove the decimate mod for the current guy
    #bpy.ops.object.modifier_remove(modifier="Decimate")

    # hide the object
    bpy.context.object.hide_render = True
    bpy.context.object.hide = True

    # keyframe visibility
    bpy.context.object.keyframe_insert(data_path='hide_render')
    bpy.context.object.keyframe_insert(data_path='hide')

    # advance to the next frame
    bpy.context.scene.frame_current += 1

    # show object
    bpy.context.object.hide_render = False
    bpy.context.object.hide = False

    # keyframe vizibility
    bpy.context.object.keyframe_insert(data_path='hide_render')
    bpy.context.object.keyframe_insert(data_path='hide')

    # advance to next frame
    bpy.context.scene.frame_current += 1

    # hide object 
    bpy.context.object.hide_render = True
    bpy.context.object.hide = True

    # keyframe viz
    bpy.context.object.keyframe_insert(data_path='hide_render')
    bpy.context.object.keyframe_insert(data_path='hide')

    # go back a frame
    bpy.context.scene.frame_current -= 1
    
    # show object
    bpy.context.object.hide_render = False
    bpy.context.object.hide = False

    # back to sculpt mode
    bpy.ops.object.mode_set(mode='SCULPT')


    # in the end I want to end up on a new frame with a new object that is
    # keyframed to be hidden on all frames but the one I'm on
    
class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.record"
    bl_label = "Record Frame"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        record(context)
        return {'FINISHED'}

# make a ui panel for this sculpt recorder
class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Sculpt Recorder"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Big render button
        row = layout.row()
        row.scale_y = 5.0
        row.operator("object.record")



def register():
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(SimpleOperator)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(SimpleOperator)


if __name__ == "__main__":
    register()