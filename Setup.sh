### INSTALL SCRIPT
# tell application "Terminal" do script "xcode-select --install; git --version ; git clone https://github.com/fire17/WatchTVBridge ~/WatchTVBridge; cd ~/WatchTVBridge ; git pull ; sh Setup.sh" end tell
# INSTALL
# MAC : osascript -e 'tell app "Terminal" to do script "xcode-select --install; git --version; git clone https://github.com/fire17/WatchTVBridge ~/WatchTVBridge; cd ~/WatchTVBridge ; git pull ; sh Setup.sh"'
# TER: xcode-select --install; git --version; git clone https://github.com/fire17/WatchTVBridge ~/WatchTVBridge; cd ~/WatchTVBridge ; git pull ; sh Setup.sh
# RUN
# MAC : osascript -e 'tell application "Terminal" to do script "cd ~/WatchTVBridge; sh start"'
# TER : cd ~/WatchTVBridge; sh start

# DEPS:
# sudo apt install curl
# brew install curl
# no ensurepip

# xcode-select --install

echo " "
echo " "
echo "  ##########################################################"
echo "  ##########################################################"
echo "  ##########################################################"
echo "  #######                                              #####"
echo "  #######                                              #####"
echo "  #######           Welcome to Magicho's               #####"
echo "  #######                                              #####"
echo "  #######              WatchTV Bridge                  #####"
echo "  #######                                              #####"
echo "  #######               Installation                   #####"
echo "  #######                                              #####"
echo "  #######                                              #####"
echo "  ##########################################################"
echo "  ##########################################################"
echo "  ##########################################################"
echo ""
sleep 1
### CHECK FOR PYTHON3
echo "Installing python3 requirements..."
python3 -m ensurepip --upgrade
python3 -m pip install pyyaml --user
#sudo apt install curl
python3 -m pip install pynput --user
python3 -m pip install pyautogui --user
python3 -m pip install websocket-client --user
python3 -m pip install pymsgbox --user
echo ""
echo "CHECK"
echo ""
echo ""
sleep 1
# echo "Installing brew"
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
# echo ""
# echo "CHECK"
# echo ""
echo "SKIPPING PC SETUP"
echo ""
echo "CHECK"
echo ""
echo ""
echo "TV SETUP..."
sleep 1
rm -rf ~/Desktop/WatchTVBridge.app
rm -rf ~/Desktop/WatchTVBridge.zip
cp ~/WatchTVBridge/WatchTVBridge.zip ~/Desktop/WatchTVBridge.zip
echo "  ############################################"
echo "  ############################################"
echo "  #######                                #####"
echo "  #######   Please Enter TV's IP ADRESS  #####"
echo "  #######       in the prompt box        #####"
echo "  #######                                #####"
echo "  #######           find it in           #####"
echo "  #######  TV Settigns > Networks Status #####"
echo "  #######                                #####"
echo "  ############################################"
echo "  ############################################"
echo ""
#unzip -o ~/Desktop/WatchTVBridgeApp.zip ;
#rm -rf ~/Desktop/__MACOSX
# echo "................................."
sh check_tv
echo ""
echo "CHECK"
echo ""
echo ""
echo "  ############################################"
echo "  ############################################"
echo "  #######                                #####"
echo "  #######  WatchTV Bridge App Installed  #####"
echo "  #######         successfully           #####"
echo "  #######                                #####"
echo "  #######     check your desktop         #####"
echo "  #######         & unzip to relaunch    #####"
echo "  #######                                #####"
echo "  ############################################"
echo "  ############################################"
echo ""
sleep 1
echo "  LAUNCHING APP"
echo ""
echo ""
sh start
