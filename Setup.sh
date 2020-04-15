##############################################################################
### osascript install
# tell application "Terminal" do script "xcode-select --install; git --version ; git clone https://github.com/fire17/WatchTVBridge ~/WatchTVBridge; cd ~/WatchTVBridge ; git pull ; sh Setup.sh" end tell

### INSTALL SCRIPT
# MAC : osascript -e 'tell app "Terminal" to do script "xcode-select --install; git --version; git clone https://github.com/fire17/WatchTVBridge ~/WatchTVBridge; cd ~/WatchTVBridge ; git pull ; sh Setup.sh"'
# TER: xcode-select --install; git --version; git clone https://github.com/fire17/WatchTVBridge ~/WatchTVBridge; cd ~/WatchTVBridge ; git pull ; sh Setup.sh

### RUN SCRIPT
# MAC : osascript -e 'tell application "Terminal" to do script "cd ~/WatchTVBridge; sh start"'
# TER : cd ~/WatchTVBridge; sh start

##############################################################################

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
python3 -m ensurepip --upgrade ; echo '1/7 CHECK' ; echo ''
python3 -m pip install pyyaml --user ; echo '2/7 CHECK' ; echo ''
python3 -m pip install pynput --user ; echo '3/7 CHECK' ; echo ''
python3 -m pip install pyautogui --user ; echo '4/7 CHECK' ; echo ''
python3 -m pip install websocket-client --user ; echo '5/7 CHECK' ; echo ''
python3 -m pip install pymsgbox --user ; echo '6/7 CHECK' ; echo ''
### curl for linux
sudo apt install curl  ; echo '7/7 CHECK' ; echo ''
# echo "Installing brew"
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo ""
echo "CHECK"
echo ""
echo ""
sleep 1
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
unzip -o ~/Desktop/WatchTVBridgeApp.zip ;
rm -rf ~/Desktop/__MACOSX
echo ''
echo ''
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
