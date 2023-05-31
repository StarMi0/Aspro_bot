# INSTALLATION
Для установки достаточно скачать репозиторий через команду:
```shell
git clone https://github.com/User/ASPRO_bot
```
После установки необходимо создать в родительском каталоге 3 файла:
- [run.sh](./run.sh)
- [keys.txt](./keys.txt)
1. Файл [run.sh](./run.sh) служит для автоматизации запуска и имеет следующий вид:
```shell
#!/bin/bash

pkill python

git pull origin master

source env/bin/activate

pip install -r req.txt

python3.8 main.py &
```
2. Файл [keys.txt](./keys.txt) хранит ключи и ссылки к проекту, о нем сказано в разделе [Other](#Other:)

# UPDATING
Обновление происходит автоматически при перезагрузке, это прописано в файле [run.sh](./run.sh), при запуске которого происходит обновление кода из репозитория и обновление всех установленных библиотек, а так же перезапуск приложения.

