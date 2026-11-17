<p align="center"><img src="https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/titan-avatar.jpg" width="128" height="128" alt="TITAN CORE · SirenaGoloviy"></p>

<h1 align="center">TITAN CORE · SirenaGoloviy</h1>
<p align="center"><b>PLAY NO LIMIT by SirenaGoloviy</b><br>Игры, внешние диски и библиотека PS5 в одном интерфейсе.</p>

<p align="center"><a href="#русский">Русский</a> · <a href="#english">English</a> · <a href="https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/tag/fix4">Fix4 · 1.0.2</a></p>

## Русский

TITAN CORE · SirenaGoloviy — пользовательская сборка TITAN CORE на базе Kraken Mount 0.2.1. Она объединяет библиотеку игр, установщик и диагностику в одном веб-интерфейсе, который можно открыть с компьютера или телефона.

В **Fix4** добавлено прямое чтение поддерживаемых PS5 PKG с внешнего диска. Файл остаётся на USB, а TITAN готовит нужный кэш внутри консоли. Переносить весь пакет во внутреннее хранилище для этого не требуется.

### Скачать

**[Скачать Fix4 ELF](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/TITAN-CORE-SirenaGoloviy-fix4.elf)** — это файл для запуска через Payload Manager.

[Все файлы релиза](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/tag/fix4) · [Полные исходники](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/TITAN-CORE-SirenaGoloviy-fix4-source.zip) · [SHA-256](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/SHA256SUMS.txt)

### Что нового в Fix4

- Поддерживаемые PS5 PKG теперь можно читать прямо с внешнего диска; оригиналы остаются на месте.
- Доработано обновление библиотеки при добавлении игры на ходу и определение того, кто управляет PKG — TITAN или ShadowMount.
- Добавлено ожидание окончания копирования. Если есть внутренняя и внешняя копии одной игры, приоритет получает установленная внутренняя.
- Поправлена запись метаданных и очистка монтирований после выхода. Занятые слои сохраняются для повторной попытки.
- Добавлена новая аватарка для TITAN и каталог иконок для Payload Manager.

### Как запустить

1. Скачай ELF, закрой игры и полностью перезагрузи PS5 — без режима покоя.
2. Для этой сборки отключи отдельный автозапуск Kraken/ShadowMount. Привычный jailbreak и elfldr оставь: нужные службы запускает сам TITAN.
3. Запусти новый ELF через Payload Manager.
4. Открой **http://IP_ПС5:8097**. В Diagnostics должна отображаться служба **1.7beta10-titan-isolated3**.

Если осталась запущенная старая служба, полностью перезагрузи консоль и загрузи новый ELF первым.

### Внешний диск и аватарка

Поддерживаемые PKG ищутся в стандартных папках сканирования, в том числе в корне диска и homebrew. Внутренний кэш всё равно занимает место, а диск должен оставаться подключённым во время игры.

Чтобы аватарка появилась в **Payload Manager**, добавь этот адрес в **Settings → Manage Sources → Add Source**:

https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/payloads.json

Картинка в списке Payload Manager загружается через этот каталог. При одной лишь ручной загрузке ELF она может не появиться. Иконка ярлыка TITAN на домашнем экране отдельно встроена в сборку.

### О совместимости

Fix4 собран без предупреждений; **80 локальных тестов прошли**. Следующий шаг — проверка именно этой версии на PS5. Поэтому пока не обещаю, что все сообщённые зависания и вылеты исчезли: падение **007 First Light (PPSA11386)** ещё требует разбора дампа.

Нативный движок работает с поддерживаемыми PS5 debug/plaintext PKG. **PS4, retail, AES-XTS и отдельные LIH-патчи им не поддерживаются.** Подробности проверок есть в [validation.json](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/validation.json). Сборка сохраняет защиту YouTube/Y2JB из Fix3, но уже изменённые иконки и удалённые файлы сама не восстанавливает.

Если встретишь проблему, приложи журнал TITAN, название игры, Title ID и укажи, где лежал пакет. Это поможет разбирать конкретную причину, а не гадать по скриншоту.

---

## English

TITAN CORE · SirenaGoloviy is a community build of TITAN CORE based on Kraken Mount 0.2.1. It brings your game library, installer and diagnostics together in a web interface you can open from a computer or phone.

**Fix4** adds direct playback of supported PS5 PKGs from external storage. The original package stays on your USB drive while TITAN prepares its cache on the console. You do not need to copy the entire package to internal storage for this workflow.

### Download

**[Download Fix4 ELF](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/TITAN-CORE-SirenaGoloviy-fix4.elf)** — the file to launch through Payload Manager.

[Release files](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/tag/fix4) · [Full build sources](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/TITAN-CORE-SirenaGoloviy-fix4-source.zip) · [SHA-256](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/SHA256SUMS.txt)

### What's new in Fix4

- Direct reading of supported external PS5 PKGs while keeping the original files in place.
- Updated live-library refresh and PKG ownership handling between TITAN and ShadowMount.
- A settling check for files being copied, with installed internal copies taking priority over external duplicates.
- Metadata-writing and exit-cleanup fixes. Busy mounts stay tracked for another cleanup attempt.
- A new TITAN avatar and an icon catalog for Payload Manager.

### Getting started

1. Download the ELF, close your games and fully reboot the PS5; do not use rest mode.
2. Disable separate Kraken/ShadowMount autoload for this bundle. Keep your usual jailbreak and elfldr setup; TITAN starts its bundled services.
3. Launch the new ELF through Payload Manager.
4. Open **http://PS5-IP:8097** and check Diagnostics for **1.7beta10-titan-isolated3**.

If an older service is already running, fully reboot and load the new ELF first.

### External storage and the avatar

Supported PKGs are discovered in the configured scan folders, including the drive root and homebrew in the default setup. Internal cache still uses console storage, and the source drive must stay connected while playing.

For the avatar in **Payload Manager**, add this source under **Settings → Manage Sources → Add Source**:

https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/payloads.json

Payload Manager gets its list icon from this catalog; manually uploading the ELF alone may not display it. The TITAN home-screen shortcut icon is bundled separately inside the ELF.

### Compatibility

Both ELF stages built without warnings and **80 local tests passed**. This exact version still needs PS5 testing, so the reported hangs and crashes are not all confirmed resolved. The **007 First Light (PPSA11386)** crash remains open pending dump analysis.

The native engine supports compatible PS5 debug/plaintext PKGs. **PS4, retail, AES-XTS and LIH patch-only packages are unsupported.** See [validation.json](https://github.com/grimmtroll2285-dot/TITAN-CORE-SirenaGoloviy/releases/download/fix4/validation.json) for the checks performed. Fix3's YouTube/Y2JB protections are retained; previously changed icons and deleted files are not automatically restored.

When reporting a problem, include the TITAN log, game name, Title ID and package location. Those details make it much easier to find the cause.

---

### Авторы / Credits

SirenaGoloviy обозначает пользовательскую сборку и уведомление **PLAY NO LIMIT**. TITAN CORE, Kraken Mount, AMPR, kstuff-lite и ShadowMountPlus остаются работой своих авторов. / SirenaGoloviy identifies this community build and its launch notice; the original engines retain their authorship.

[Авторы и компоненты / Authors and components](CREDITS.md) · [GPL-3.0 license](LICENSE)

Полные исходники конкретного ELF находятся в отдельном архиве релиза. Этот репозиторий служит страницей распространения; автоматический GitHub Source code не заменяет полный архив. / The exact ELF sources are provided as a separate release asset. This repository is the distribution page; GitHub's automatic Source code download does not replace that archive.
