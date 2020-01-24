# Basic MacOS Setup
OG Guide: https://sourabhbajaj.com/mac-setup/

Remove Siri from touch bar.

1. iTerm2
	- Preferences -> Keys -> Configure Hotkey Window
	  - https://www.typefloundry.com/1-800-iterm-bling.html
	  - Use ^Space

   - Setup MacOS Hotkeys (End of line, End of word)
       - https://stackoverflow.com/questions/6205157/iterm-2-how-to-set-keyboard-shortcuts-to-jump-to-beginning-end-of-line
       - Fix profile for word jump (choose Natural Text Editting)
          - https://stackoverflow.com/questions/29369352/os-x-terminal-shortcut-jump-to-beginning-end-of-line

   
   - Color Schemes: https://github.com/mbadolato/iTerm2-Color-Schemes
   	     - Good ones: Solarized Dark
   	     - Visible One: Argonaut
   	     - Dracula: https://draculatheme.com/iterm/

   	
Macs in Catalina or older use ZSH by default.
	- .zshrc and .zprofile replaces .bashrc and .bash_profile
	- https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh

- zsh is default shell editor. bash is still the dominant scripting language

Guide: https://gist.github.com/kevin-smets/8568070

1. ZSH Setup
	- Use plugins from https://sourabhbajaj.com/mac-setup/iTerm/zsh.html
	- Troubleshooting for autocomplete and syntax highlighting:
	     - https://github.com/ohmyzsh/ohmyzsh/issues/7688

2. ZSH Themes
   - Professional (powerline10k): https://github.com/romkatv/powerlevel10k
   - Old Professional (agnoster) 
   - Simple (dracula): https://draculatheme.com/zsh/

3. Vim Basic Setup
   - Basic version from https://github.com/amix/vimrc

4. VSCode Setup
   - Bookmarks Extension
   - Ruler