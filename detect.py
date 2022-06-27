import pyautogui
import cv2
import time
import asyncio


# def check():
#     capture = pyautogui.locateCenterOnScreen('user_icon.png',confidence=0.9)
#     if str(capture) == "None":
#         print("0")
#         time.sleep(2)
#     else:
#         print("get it")
#         print(capture)
#         time.sleep(2)

# i = 0
# for i in range (0,20):
#     # pyautogui.scroll(-500)
#     print("tried" + str(i))
#     check()
async def main():
    print(f"started at {time.strftime('%X')}")
    capture = pyautogui.locateCenterOnScreen('main.png',confidence=0.9)
    print(capture)
    await asyncio.sleep(2)
    pyautogui.moveTo(capture)

    print(f"finshed at {time.strftime('%X')}")

asyncio.run(main())
