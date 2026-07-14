#!/bin/sh

echo installing Piz...

# apt related


 sudo apt install sxhkd compiz-core compiz-plugins-main compiz-plugins-extra mate-polkit-bin mate-polkit emerald network-manager-applet
 sudo apt purge emerald-themes
 echo core components installed.
 echo installing extras...
 (sleep 1; sudo apt install compizconfig-settings-manager xfce4-panel xfce4-clipman xfce4-screenshooter  xfce4-clipman-plugin plank xfce4-pulseaudio-plugin mate-notification-daemon)
 echo extras installed.

# the scripts and .desktops used for display managers like lightdm

echo moving startup scripts...
(sleep 1; sudo  cp -r main/startpiz /usr/local/bin)
(sleep 1; sudo chmod +x /usr/local/bin/startpiz)
sudo cp -r custom/ppower /usr/local/bin
sudo cp -r custom/PpowerMenu.py /opt
echo moved session startup script.
(sleep 1; sudo cp -r main/piz.desktop /usr/share/xsessions/)
echo moved session desktop entry.

# configs used by most of each of the core and extra components

echo moving configuration files...
cp -r configs/compiz ~/.config
echo moved compiz config.
cp -r configs/.pizwall.jpg /opt
echo moved compiz wallpaper.
cp -r configs/xsettingsd ~/.config
echo moved xsettings config.
cp -r configs/xfce4 ~/.config
echo moved xfce4 related configs.
cp -r configs/sxhkd ~/.config
moved sxhkd config.
cp -r configs/Thunar ~/.config
echo moved thunar config.
cp -r configs/.emerald ~/
echo moved emerald config.
(sleep 1; echo moved all configurations.)

# themes gtk used in the previews, etc

(sleep 1; echo moving gtk themes...)
mkdir ~/.themes
mkdir ~/.icons
unzip themes.zip
cp -r themes/Reactium ~/.themes
cp -r themes/oxylite ~/.icons
cp -r themes/Moga-Dark ~/.icons
echo Piz installation finished. have fun :D!
