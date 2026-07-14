import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

# window rules

class PowerMenu(Gtk.Window):
   def __init__(self):
       super().__init__(title="Power Menu")
       self.set_position(Gtk.WindowPosition.CENTER)
       self.set_modal(True)
       self.set_type_hint(Gdk.WindowTypeHint.DIALOG)
       self.set_decorated(False)
       self.set_keep_above(True)
       self.set_skip_taskbar_hint(True)
       self.set_skip_pager_hint(True)
       self.set_resizable(False)
       self.set_border_width(15)
       self.set_default_size(350, 180)
       
       # Grid       
       
       grid = Gtk.Grid()
       grid.set_row_spacing(10)
       grid.set_column_spacing(10)
       self.add(grid)
       
       # the first button
       
       image1 = Gtk.Image.new_from_icon_name(
           "gnome-shutdown",
          Gtk.IconSize.DIALOG
       )
       
       box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
       
       box1.pack_start(image1, True, True, 0)
       box1.pack_start(Gtk.Label(label="Power Off.."), False, False, 0)
       
       
       self.button1 = Gtk.Button()
       self.button1.add(box1)
       
       
       # the second button
       
       image2 = Gtk.Image.new_from_icon_name(
           "xfce-system-exit",
          Gtk.IconSize.DIALOG
       )
       
       box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
       
       box2.pack_start(image2, True, True,0)
       box2.pack_start(Gtk.Label(label="Restart.."), False, False, 0)             
       
       
       self.button2 = Gtk.Button()
       self.button2.add(box2)
       
       # the third button       
       
       image3 = Gtk.Image.new_from_icon_name(
           "xscreensaver",
          Gtk.IconSize.DIALOG
       )
       
       box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
       
       box3.pack_start(image3, True, True, 0)
       box3.pack_start(Gtk.Label(label="Suspend.."), False, False, 0)       
       
       self.button3 = Gtk.Button()
       self.button3.add(box3)
      
       # the fourth button
       
       image4 = Gtk.Image.new_from_icon_name(
           "system-save-session",
          Gtk.IconSize.DIALOG
       )
       
       box4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
       
       box4.pack_start(image4, True, True, 0)
       box4.pack_start(Gtk.Label(label="Hibernate.."), False, False, 0)
       
       self.button4 = Gtk.Button()
       self.button4.add(box4)
       
       # the fifth button
       
       self.button5 = Gtk.Button(label="Lock Screen..")
       
       # the sixth button
       
       self.button6 = Gtk.Button(label="Switch User..")
       
       self.quit = Gtk.Button(label="Cancel")
                                                
       # the button actions..                                                
                                                
       self.button1.connect("clicked", self.on_button1_clicked)
       self.button2.connect("clicked", self.on_button2_clicked)
       self.button3.connect("clicked", self.on_button3_clicked)
       self.button4.connect("clicked", self.on_button4_clicked)
       self.button5.connect("clicked", self.on_button5_clicked)
       self.button6.connect("clicked", self.on_button6_clicked)
       self.quit.connect("clicked", Gtk.main_quit)

       grid.attach(self.button1, 0, 0, 1, 1)
       grid.attach(self.button2, 1, 0, 1, 1)
       grid.attach(self.button3, 2, 0, 1, 1)
       grid.attach(self.button4, 3, 0, 1, 1)
       grid.attach(self.button5, 0, 1, 2, 1)
       grid.attach(self.button6, 2, 1, 2, 1)
       grid.attach(self.quit,    0, 4, 4, 1)
       
   def on_button1_clicked(self, widget):
   	subprocess.Popen(["systemctl", "poweroff"])
   	
   def on_button2_clicked(self, widget):
   	subprocess.Popen(["systemctl", "reboot"])
   	
   def on_button3_clicked(self, widget):
   	subprocess.Popen(["systemctl", "suspend"])
   	
   def on_button4_clicked(self, widget):
   	subprocess.Popen(["systemctl", "hibernate"])
   
   def on_button5_clicked(self, widget):
   	subprocess.Popen(["xfce4-screensaver-command", "--lock"]) 
   	
   def on_button6_clicked(self, widget):
   	subprocess.Popen(["dm-tool", "switch-to-greeter"])   
     
win = PowerMenu()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()