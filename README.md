# Piz
A work in process standalone session of the Compiz window manager

# Preview
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/c1503879-14d3-472d-a070-6f05ed2e132f" />

Piz (pronounced PEZ like the candy) is a standalone session of Compiz. a x11 compositing window manager.

currently, Piz is just a mash up of xfce and MATE components but will hopefully evolve into its own thing of sorts.

# Installation

# Disclaimer:
Piz is not in a perfect state, some features are missing and not avaliable as of now. suggesting improvements are welcome.

To install Piz. Clone this repository and run `installpiz.sh`.
(Note: the installer script currently only works on debian, support for other distros will be made later on.)

 **Manual Installation**
 this part is for manual installation if you use debian just use the script as stated above.
 
 first you will need the core components of Piz
 
 * `compiz-core`
 * `compiz-plugins-main`
 * `compiz-plugins-extra`
 * `emerald`
 * `xsettingsd`
 * `sxhkd`

 * after installing those clone this repository and go to  `/main` there will be two files. `startpiz` and `piz.desktop`.
 * put `startpiz` in `/usr/local/bin` and `piz.desktop` in `/usr/share/xsessions`. or make both manually to customize them to your desire.

 Technically you should be good to go and configure the rest yourself.

 **recommended programs**
 * these packages arent required (the debate is up to you if it is) but i personally recommend them.

 * `xfce4-panel`
 * `plank`
 * `compizconfig-settings-manager`
 * `menulibre`
 * `nm-applet`

* # hopeful roadmap for Piz
* Make it fully independent from any other desktop environment.
* custom applications designed for it.
* an ecosystem of sorts.

* # Special thanks to
* [0stormy](https://git.0stormy.xyz/stormy/Reactium) for Reactium. the current default theme of Piz
* [mx-2](https://github.com/mx-2/oxylite-icon-theme/) for oxylite. the current icon pack used by Piz.
* the [xfce4](https://xfce4.org) and [MATE](https://mate-desktop.org) developers for some of the software used by Piz.
* and you. for trying it out.
