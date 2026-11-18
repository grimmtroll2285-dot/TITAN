<p align="center"><img src="https://github.com/grimmtroll2285-dot/TITAN/releases/download/fix7/titan-avatar.jpg" width="128" height="128" alt="TITAN · SirenaGoloviy"></p>

# TITAN · SirenaGoloviy

**[Скачать FIX7 ELF](https://github.com/grimmtroll2285-dot/TITAN/releases/download/fix7/TITAN-SirenaGoloviy-fix7.elf)** · **[Релиз 1.0.5](https://github.com/grimmtroll2285-dot/TITAN/releases/tag/fix7)**

[Полные исходники](https://github.com/grimmtroll2285-dot/TITAN/releases/download/fix7/TITAN-SirenaGoloviy-fix7-source.zip) · [SHA-256](https://github.com/grimmtroll2285-dot/TITAN/releases/download/fix7/SHA256SUMS.txt) · [Авторы](CREDITS.md) · [GPL-3.0](LICENSE)

# TITAN · FIX7 · 1.0.5 · SirenaGoloviy

PLAY NO LIMIT by SirenaGoloviy

donate: 2200700949917206 💳

TITAN CORE переименован в TITAN. В этой версии собраны вкладка бэкпортов и выбор PlayGo по списку игр поверх FIX6.

## Что изменилось

- Название интерфейса, плитки и уведомлений: TITAN. Новый адрес репозитория: https://github.com/grimmtroll2285-dot/TITAN. Внутренние пути /data/titan-core, кэши, настройки и идентификаторы движков сохранены для совместимости.
- Настройки → PlayGo: отдельный видимый блок, поиск и галочки напротив игр. Включённая галочка разрешает PlayGo от TITAN; выключенная оставляет библиотеку игры. Вводить Title ID больше не нужно. Существующие исключения, включая игры на отключённых дисках, сохраняются. Выбор общий для одного Title ID. Для новых игр PlayGo разрешён по умолчанию; общий переключатель PlayGo и inject_ampr сохраняют приоритет.
- Вкладка «Бэкпорты» показывает библиотеку и подбирает патчи для родного движка TITAN по Title ID, точной версии, диапазону прошивки, формату и модели PS5/Slim или Pro. Поддерживаются PS5 PKG и папки; установка патчей для образов ShadowMount пока недоступна.
- Скачивание патча запускает пользователь. Проверяются размер и SHA-256 каждого файла, безопасные пути и совпадение идентификатора/версии в param.json. Оригинальные PKG, игры и сохранения не перезаписываются.
- Скачанные файлы хранятся отдельно. Применение и возврат предыдущего выбора требуют полной перезагрузки PS5; простой перезапуск TITAN недостаточен. Есть отключение и отмена ожидающего изменения. Повреждённый новый комплект не заменяет предыдущий выбор.
- Собственный каталог TITAN подключён по умолчанию: https://raw.githubusercontent.com/grimmtroll2285-dot/TITAN/main/backports/catalog.json. Автоматическая проверка через 35 секунд после старта и каждые 30 минут; установки без нажатия кнопки нет. Можно добавить свои каталоги GitHub или импортировать JSON. В исходниках есть упаковщик папки/ZIP в каталог с SHA-256.
- Добавлены справочные ссылки на BackPork, PS5 Backport Toolkit и PS5 Game Updater. Это инструменты и информация, а не совместимые каталоги автоматической установки. На 18.11.2026 публичный verified-seed.json Game Updater пуст; BackPork публикует BPS-патчи, требующие исходных библиотек.

**Каталог TITAN пока пуст: готовых проверенных игровых бэкпортов в FIX7 нет.** Подбор и загрузка появятся для игры после добавления подходящего комплекта в подключённый каталог. Совместимость каждого бэкпорта требует отдельной проверки. Вкладка не генерирует патчи и не скачивает целые игры.

## Переход с FIX6 после переименования репозитория

1. Загрузите TITAN-SirenaGoloviy-fix7.elf из Assets вручную. Старый обновлятор FIX6 жёстко проверяет адреса прежнего репозитория и может перестать видеть выпуски после переименования. Автоматический переход с FIX6 не обещается.
2. Закройте игры, полностью перезагрузите PS5 и запустите новый ELF через Payload Manager. Обновите также старый файл в автозагрузке/локальном источнике Payload Manager, иначе он может снова сохранить старую сборку.
3. Откройте http://IP_ПС5:8097 и дождитесь готовности. Для объединённой сборки отдельный автозапуск Kraken/ShadowMount не нужен. Существующий jailbreak/elfldr оставьте.
4. Для PlayGo: «Настройки → PlayGo», выберите игры и нажмите «Сохранить». Закройте игры и дождитесь готовности кэша перед запуском.
5. У обновлятора FIX7 новый адрес TITAN. Доступны стабильные/pre-release и выбор версии для обновления/даунгрейда. При откате на FIX6 старый адрес обновлятора возвращается: для перехода обратно на FIX7 может снова понадобиться ручная загрузка.

Каталог Payload Manager с аватаркой: https://github.com/grimmtroll2285-dot/TITAN/releases/download/fix7/payloads.json

## Проверки и ограничения

81 переносимый тест Rust, 8 тестов PKG, 20 JavaScript и 3 Python: всего 112. Проверены типы PS5, локализация, синтаксис встроенного JavaScript и интерфейс на синтетических данных. Обе стадии ELF, вложенный stage1, компоненты и SHA-256 проверены отдельно в validation.json.

**Новая сборка, загрузка бэкпортов, перезагрузка и откат на реальной PS5 не проверены.** Тесты ПК не подтверждают запуск игр. Существующая гонка запуска игры во время пересборки кэша остаётся открытой: не запускайте игру до Ready. PlayGo не исправляет лицензии и не гарантирует работу MGS 4, 007, Yōtei или большинства игр. Сторонние патчи проверяйте на точное соответствие своей версии/прошивке/модели.

Сохранены компоненты FIX6: Kraken Mount 0.2.1, AMPR 0.4.1, оригинальный drakmor PlayGo Stub 0.6, ShadowMountPlus 1.7beta12-titan-isolated4, kstuff-lite 1.11. Отдельные экспериментальные изменения расследования PKG/fakelib2 сюда не включены. Native PS4, retail/encrypted PKG, AES-XTS и отдельные LIH-патчи не добавлены. Игра с внешнего диска требует подключённого оригинала и внутреннего кэша.

Полные соответствующие исходники: TITAN-SirenaGoloviy-fix7-source.zip в Assets. Автоматический GitHub Source code содержит страницу распространения, а не полный исходный код ELF. Авторство и лицензии upstream сохранены.

## English

FIX7 1.0.5 renames the app/repository to TITAN, adds named PlayGo game checkboxes and catalog-backed native PS5 PKG/folder backport management. Exact compatibility matching, per-file SHA-256, separate immutable overlays and reboot-deferred selection/rollback are implemented. ShadowMount image installation is not supported by this catalog yet. The default project catalog is connected but currently contains zero verified game backports; three reference projects are clearly labeled as tools/information, not installable feeds.

After the repository rename, FIX6's pinned URL checks can prevent its updater from listing releases. Load FIX7 manually once, and update any old autoload/Payload Manager copy. FIX7's updater uses the new TITAN address and also recognizes historical TITAN-CORE asset filenames. Downgrading restores that old release's updater behavior. Data paths and existing settings stay compatible.

112 host tests passed. Both ELF stages and embedded components are verified in validation.json. This new build and the console backport/download/reboot/rollback flow have not been hardware-tested. Original PKGs and saves are not overwritten; close games and wait for Ready before playing. Complete corresponding source, licenses and the catalog packager are in the separately named source ZIP asset.
