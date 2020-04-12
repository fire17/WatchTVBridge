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
sleep 3
echo "Installing python3 requirements..."
python3 -m pip install pyyaml
python3 -m pip install pynput
python3 -m pip install pyautogui
python3 -m pip install websocket-client
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
sh check_tv
echo ""
echo "CHECK"
echo ""
echo ""
