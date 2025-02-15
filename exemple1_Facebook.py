def Initialisation_Driver(p_udid, p_systemPort, p_deviceName, p_version, p_os,p_label_log,lock):
   
   desired_caps = {}
   desired_caps['automationName'] = 'UiAutomator2'
   desired_caps['platformName'] = p_os
   desired_caps['platformVersion'] = p_version
   desired_caps['deviceName'] = p_deviceName
   desired_caps['udid'] = p_udid
   desired_caps['noReset'] = 'true'
   desired_caps['systemPort'] = p_systemPort
   desired_caps['chromeDriverPort'] = p_systemPort
   desired_caps['appWaitDuration'] = 100000
   desired_caps['newCommandTimeout'] = 0
   desired_caps['wdaStartupRetries'] = 4
   desired_caps['wdaStartupRetryInterval'] = 20000
   desired_caps['uiautomator2ServerLaunchTimeout'] = 100000
   desired_caps['uiautomator2ServerInstallTimeout'] = 100000
   desired_caps['remoteAppsCacheLimit'] = 0
   desired_caps['waitForQuiescence'] = 'false'
   desired_caps['appPackage'] = 'com.facebook.katana'
   desired_caps['appActivity'] = 'com.facebook.katana.LoginActivity'
   cpt_appium_start=0
   while True:
       try:
           driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
           time.sleep(random.uniform(3.5, 5.3))
           return driver

       except Exception as ex:
           cpt_appium_start+=1
           logger.critical(f"{p_udid}|||Something went wrong when initializing driver : {ex}")
           logger.critical(
               f"{p_udid}|||We can't open Facebook. Please check if device is connected. Let's try again!")
           if str(ex).find('hang up')!=-1:
               logger.error("PhoneBot caught the issue exception 'hang up' when initializing Driver!")
               proc = subprocess.Popen(
                   f'adb -s {p_udid} uninstall io.appium.uiautomator2.server',
                   shell=True,
                   stdin=None, stdout=None, stderr=None, close_fds=True)

               proc2 = subprocess.Popen(
                   f'adb -s {p_udid} uninstall io.appium.uiautomator2.server.test',
                   shell=True,
                   stdin=None, stdout=None, stderr=None, close_fds=True)
               proc3 = subprocess.Popen(
                   f'adb -s {p_udid} uninstall io.appium.settings',
                   shell=True,
                   stdin=None, stdout=None, stderr=None, close_fds=True)

           elif str(ex).find('Failed to establish a new connection')!=-1:
               logger.critical(f"SMARTPHONE|||{p_udid}||Appium server may not be working. Please contact support@phonebot.co : {ex}")
               logger.critical(
                   f"{p_udid}|||We can't open Facebook. Please check if device is connected. Let's try again!")
               mymodules.DisplayMessageLogUI(p_label_log,
                   f"SMARTPHONE|||{p_udid}||Appium server may not be working. Please contact support@phonebot.co : {ex}")

           if cpt_appium_start > 3:
               mymodules.PopupMessage("Error","PhoneBot couldn't initialize the driver. Please contact support@phonebot.co.")
               mymodules.DisplayMessageLogUI(p_label_log,
                                      "PhoneBot couldn't initialize the driver. Please contact support@phonebot.co.")
               return None

           time.sleep(random.uniform(2.5, 3.3))

