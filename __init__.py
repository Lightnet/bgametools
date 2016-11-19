



bl_info = {
    "name": "bgametools",
    "author": "Darknet",
    "version": (1, 0, 0),
    "blender": (2, 7, 7),
    "location": "View3D > Tools > bgametools",
    "description": "Simple Tool test.",
    "warning": "",
    'wiki_url': "",
    "category": "testing"}
	
import bpy
import os
import json
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.app.handlers import persistent
import time
import logging


class MytoolsPanel(bpy.types.Panel):
	bl_label = "bgametools"
	bl_idname = "OBJECT_PT_bgametools"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	#bl_context = 'objectmode'
	bl_category = "testing"

	def draw(self, context):
		print("test")
		scn = bpy.context.scene
		box = self.layout.box()
		box.label("Testing label")


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()