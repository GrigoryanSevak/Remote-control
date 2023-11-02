import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((input('Введите ip-address: '), 6286))
print(
    f"\n\n\n youtube (текст)\n",
    f"merojax (открытие этого сайта)\n",
    f"vk (открытие этого сайта)\n",
    f"message (заголовок, сообщение 'если не набрать текст будет встроенное сообщение')\n",
    f"audio (текст 'если не набрать текст будет встроенный звук')\n",
    f"поиск (текст)\n",
    f"mouse (время)\n",
    f"close (закрыть все окна)\n",
    f"exit (выход)\n",
    f"shutdown (выключить компьютер)\n\n\n"
)

while True:
    function = input("Выберите функцию (или 'exit' для выхода): ")
    client.send(function.encode('cp1251'))
    if function == 'exit':
        break