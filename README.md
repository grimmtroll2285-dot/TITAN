<p align="center"><img src="https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix6/titan-avatar.jpg" width="128" height="128" alt="TITAN CORE · SirenaGoloviy"></p>

# TITAN CORE · SirenaGoloviy

**[Скачать FIX6 ELF / Download FIX6 ELF](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix6/TITAN-CORE-SirenaGoloviy-fix6.elf)** · **[Релиз 1.0.4 / Release](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/tag/fix6)**

[Полные исходники / Full source](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix6/TITAN-CORE-SirenaGoloviy-fix6-source.zip) · [SHA-256](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix6/SHA256SUMS.txt) · [Авторы / Credits](CREDITS.md) · [GPL-3.0](LICENSE)

# FIX6 · 1.0.4 · PlayGo + обновления на консоли

**PLAY NO LIMIT by SirenaGoloviy**

Обычный релиз FIX6: объединены PlayGo из предыдущего pre-release и обновлятор TITAN с выбором версии.

## Что добавлено

- Встроен оригинальный PlayGo Stub 0.6 от drakmor. Он сообщает играм о готовности частей установки; реальные данные читает AMPR. Включён по умолчанию при inject_ampr, есть общий переключатель и исключения по Title ID в расширенных настройках.
- Ручной libScePlayGo.sprx в /data/titan-core/ampr имеет приоритет. Выключение PlayGo или исключение игры отключает общую подмену без удаления ручного файла. Меняется только fakelib, оригиналы PKG остаются на месте. Игры-образы ShadowMount сохраняют прежнюю политику библиотек.
- На самой консоли: проверка выпусков через 20 секунд после старта и затем каждые 30 минут, даже с закрытой веб-страницей. Автоматической установки нет.
- В окне «Обновления» доступны стабильные и предварительные выпуски, выбор версии, скачивание на консоль, обновление, даунгрейд и повторная установка. Для старых выпусков без номера версии показывается тег.
- Скачивание проверяет размер, SHA-256 и структуру ELF. Сервер берёт адрес и контрольную сумму из выбранного выпуска нашего репозитория; произвольные адреса от браузера не принимает. Файл скачивается потоково на внутренний диск.
- Предыдущий сохранённый ELF остаётся как /data/titan-core/titan-core.previous.elf. Запущенные игры и установка PKG блокируют подготовку обновления. Служебный YouTube/Y2JB не считается игрой и не блокирует обновлятор.
- Сохранены компоненты Fix5: Kraken Mount 0.2.1, AMPR 0.4.1, ShadowMountPlus 1.7beta12-titan-isolated4 и kstuff-lite 1.11.

## Первый запуск FIX6

1. Скачайте **TITAN-CORE-SirenaGoloviy-fix6.elf**. Закройте игры, полностью перезагрузите PS5 и запустите его через Payload Manager.
2. Для объединённой сборки отключите отдельный автозапуск Kraken/ShadowMount. Существующий jailbreak/elfldr оставьте.
3. Откройте http://IP_ПС5:8097 и дождитесь готовности. Не запускайте игру во время подготовки или пересборки кэша.
4. Откройте «Обновления», выберите выпуск и нажмите «Скачать на консоль» либо кнопку установки/обновления/отката.
5. Установка только подготавливает /data/titan-core/titan-core.elf. Для применения полностью перезапустите консоль, затем запустите TITAN через его сохранённую плитку. Текущий процесс и службы не заменяются на ходу.

**Старый ELF в Payload Manager или автозагрузке может перезаписать подготовленную версию. Обновите этот источник отдельно.** После отката на выпуск без обновлятора его интерфейс тоже исчезнет; для возвращения на FIX6 загрузите новый ELF обычным способом. Резервный ELF — ручной способ восстановления через рабочий загрузчик, не автоматический откат при сбое загрузки.

Каталог с аватаркой для Payload Manager: [payloads.json](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix6/payloads.json). Добавьте адрес через Settings → Manage Sources → Add Source.

## Проверки и пределы

Пройдены **72 теста Rust, 8 тестов PKG и 11 тестов JavaScript**. Проверены типы PS5, локализация и синтаксис встроенного интерфейса. Обе стадии ELF собраны; результаты проверки структуры, вложенных компонентов и SHA-256 находятся в validation.json.

**Обновлятор, его перезапуск и именно этот объединённый ELF ещё не проверены на реальной PS5.** Метка обычного релиза выбрана владельцем сборки и не заменяет проверку на консоли. Совместимость большинства игр, исправление 007/MGS 4/Yōtei и производительность не подтверждены. PlayGo не восстанавливает лицензии. Ранее отмеченная гонка запуска игры во время пересборки кэша остаётся открытой. Не запускайте игру до завершения подготовки.

Для нативного движка нужны поддерживаемые PS5 debug/plaintext PKG. PS4, retail/encrypted, AES-XTS и отдельные LIH-патчи им не поддерживаются. Внешний диск с оригиналом должен оставаться подключённым; внутреннему кэшу всё ещё нужно место. Защита YouTube сохранена, но ранее изменённые иконки или удалённые файлы автоматически не восстанавливаются.

Подробное устройство и ограничения обновлятора: CONSOLE-UPDATER.md. Полные соответствующие исходники — **TITAN-CORE-SirenaGoloviy-fix6-source.zip** в Assets. Автоматический GitHub Source code содержит страницу распространения, а не полный исходный код ELF. Лицензии и авторство upstream сохранены. Предыдущие [Fix5](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/tag/fix5) и [PlayGo pre-release](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/tag/fix6-playgo-pre1) доступны для отката.

## English

FIX6 1.0.4 combines the previous PlayGo integration with an on-console version selector and updater. Stable and pre-release builds are shown by default. Metadata checks run after startup and every 30 minutes even with the UI closed. Downloads and installation are manual; upgrading, downgrading and reinstalling are supported.

Close games, choose a release in Updates, and download or install it. The updater validates the repository asset, size, SHA-256 and ELF structure, keeps the previous saved ELF, and prepares the saved TITAN launch file. Fully reboot and launch the saved TITAN tile to activate it. Resident services are never hot-swapped. An old Payload Manager/autoload ELF can overwrite that saved file: update its source separately. Downgrading to a version without this updater removes its UI until a newer ELF is loaded again. The previous ELF is a manual recovery file, not automatic boot rollback.

Unmodified drakmor PlayGo Stub 0.6 is enabled for native titles when inject_ampr is enabled, with a global switch and per-title exclusions. Manual PlayGo overrides take precedence. No original PKG or save is removed. ShadowMount-owned images retain their existing runtime policy. Fix5 service binaries are unchanged.

**72 Rust + 8 PKG + 11 JavaScript tests passed; both ELF stages built, PS5 types, localization, embedded artifacts and SHA-256 were checked. This combined ELF and the console updater/reboot flow have not been tested on a real PS5.** Specific games, licenses, crash fixes and performance are not guaranteed. The existing mid-build launch race remains open; wait for preparation to finish before starting games.

Use the separately named source ZIP in Assets for complete matching sources, not GitHub's automatic Source code archive. Original authorship, GPL PlayGo source and RustCrypto dependency sources/licenses are included.
