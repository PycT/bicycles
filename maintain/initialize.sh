#nividia driver
sudo apt-add-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt install -y nvidia-drivers-390

#git
sudo apt install -y git

#curl
sudo apt install -y curl

#zsh
sudo apt install -y zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
chsh -s /bin/zsh


#vim
sudo apt install -y vim

#pip3
sudo apt install -y pythin3-pip

#virtualenv
pip3 install virtualenv
mkdir ~/Envs
cd ~/Envs
python3 -m virtualenv ML

#sublime
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt install -y apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-update
sudo apt-install -y sublime-text

#docker
sudo apt install -y ca-certificates \
	gnupg-agent \
	software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io

#openvpn
sudo apt install network-manager-openvpn-gnome

