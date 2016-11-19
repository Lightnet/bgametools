"""
	Prototype builds...
"""

bl_info = {
    "name": "bgametools",
    "author": "Darknet",
    "version": (1, 0, 0),
    "blender": (2, 7, 7),
    "location": "View3D > Tools > bgametools",
    "description": "Simple Tool test.",
    "warning": "",
    'wiki_url': "",
    "category": "testing"
}

import bpy
import os
import json
#from bpy_extras.io_utils import ExportHelper, ImportHelper
#from bpy.app.handlers import persistent
#import time
#import logging

class OBJECT_OT_animationclear(bpy.types.Operator):
	bl_idname = "bgamemytools.animationclear"
	bl_label = "Animation Clear Data"
	bl_description = ''
	#bl_context = 'objectmode'
	def execute(self, context):
		#print("test");
		return {'FINISHED'}

class OBJECT_OT_actionlist(bpy.types.Operator):
	bl_idname = "bgamemytools.actionlist"
	bl_label = "Action List"
	bl_description = ''
	#bl_context = 'objectmode'
	def execute(self, context):
		#print("test");
		return {'FINISHED'}

class OBJECT_OT_exportbabylonjs(bpy.types.Operator):
	bl_idname = "bgamemytools.exportbabylonjs"
	bl_label = "Export Babylonjs"
	bl_description = ''
	#bl_context = 'objectmode'
	def execute(self, context):
		#print("test");
		return {'FINISHED'}

class OBJECT_OT_exportobjjson(bpy.types.Operator):
	bl_idname = "bgamemytools.exportobjjson"
	bl_label = "Export Obj Json"
	bl_description = ''
	#bl_context = 'objectmode'
	def execute(self, context):
		#print("test");
		return {'FINISHED'}

class MytoolsPanel(bpy.types.Panel):
	bl_label = "bgametools"
	bl_idname = "OBJECT_PT_bgametools"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	#bl_context = 'objectmode'
	bl_category = "testing"

	def draw(self, context):
		#print("test")
		scn = bpy.context.scene
		box = self.layout.box()
		box.label("Animation Data")
		box.operator('bgamemytools.animationclear')
		box.operator('bgamemytools.actionlist')

		box = self.layout.box()
		box.label("Export?")
		box.operator('bgamemytools.exportbabylonjs')
		box.operator('bgamemytools.exportobjjson')
		#box.operator('bgamemytools.animationclear')

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
