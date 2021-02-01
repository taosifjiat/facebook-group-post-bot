import pyautogui
import time
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = False
time.sleep(3)
groups = ['2937963452976370', '243472270127244', '801019433707081', '958906661210722', 'bcb.science', '210602720346541', 'ScienceIshkool', '4374374182573550', 'BigganShala', 'ongko.net', '878317445610464', '513583919253211',
          '218573638517140', '1807182449393379', '279582312486538', '410309959519558', '334300163750989', '483735418874492', 'BdMOC', '225859118649032', '291099835016145', '295890261798132', '546941835964745', '2588761351387628']
time.sleep(5)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')
for i in range(len(groups)):
    link = 'https://facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')
    print("Waiting for 20 seconds\n")
    time.sleep(20)
    pyautogui.typewrite('p')
    time.sleep(2)
    print("Writing post\n")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(4)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    pyautogui.write(['f6'])
    time.sleep(1)
