# djapa_6_decembre

## Documents administratifs

https://matthieu-falce.notion.site/DJAPA-06-12-2022-de6a796ec9d540018ca0dbaa0abb8e62

## Installation VSCode

https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions

```
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'

dnf check-update
sudo dnf install code
```
