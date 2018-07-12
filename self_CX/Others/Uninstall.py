import os


def uninstall ():
	print ("start uninstall...")
	for packages in os.popen ("adb shell pm list packages -3").readlines ():
		packageName = packages.split (":") [-1].splitlines () [0]
		if packageName.startswith ('com.yourenkeji'):
			os.popen ("adb uninstall " + packageName)
			print ("uninstall " + packageName + " successed.")


if __name__ == "__main__":
	uninstall ()
	print (" uninstatll all shenghuidai success  ")
