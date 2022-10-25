bl_info = 
{
    "name": "Smooth Auto",
    "version": (1, 0),
    "blender": (2, 80, 0)
}



import bpy


class SmoothAuto(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.smooth_auto"
    bl_label = "Smooth Auto"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SmoothAuto)


def unregister():
    bpy.utils.unregister_class(SmoothAuto)


if __name__ == "__main__":
    register()

