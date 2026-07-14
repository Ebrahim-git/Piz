#/bin/sh

echo updating Piz...

sudo cp -r custom/PpowerMenu.py /opt
sudo cp -r configs/.pizwall.jpg /opt
sudo cp -r custom/ppower /usr/local/bin
rm -r ~/.config/compiz 
rm -r ~/.config/xfce4
cp -r configs/compiz ~/.config
cp -r configs/xfce4 ~/.config

echo update completed.