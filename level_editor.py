import bpy
bl_info = {
    "name": "レベルエディタ",
    "author": "rikuri isobe",
    "version": (1,0),
    "blender": (3,3,21),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object",
}
    
#トップバーの拡張メニュー
class TOPBAR_MT_my_menu(bpy.types.Menu):
    bl_idname = "TOPBAR_MT_my_menu"
    bl_label = "MyMenu"
    bl_description = "拡張メニュー by " + bl_info["author"]
    
    #サブメニューの描画
    def draw(self,context):
        self.layout.operator("wm.url_open_preset",
        text="Manual",icon='HELP')
        
    def submenu(self,context):
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)
    
#Blanderに登録するクラス
classes = (TOPBAR_MT_my_menu,)
    
def draw_meau_manual(self,context):
    self.layout.operator("wm.url_open_preset",text="Manual",icon='HELP')
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    print("レベルエディタが有効化されました。")

def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    print("レベルエディタが無効化されました。")
        
