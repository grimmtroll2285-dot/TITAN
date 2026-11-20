# TITAN · FIX10 · 1.0.8

**PLAY NO LIMIT by SirenaGoloviy**

## Русский

Обновили движок до Kraken Mount 0.3.1 и встроили официальный AMPR 0.5.0. База — опубликованный FIX9 pre1: обновлятор, откат, бэкпорты, выбор PlayGo по названиям игр и ограничения внешних PKG сохранены.

### Что нового
- На FW 12+ игры подготавливаются за проход сканирования и регистрируются одним вызовом AppInstallAll, если отдельная регистрация TitleDir недоступна. Для пакета показывается одно уведомление. Вызов обновляет регистрацию метаданных глобально, как в upstream; TITAN подготавливает и отслеживает свои игры и сохраняет проверки владения и занятых монтирований.
- Метаданные копируются блоками 1 МиБ с сохранением нашей атомарной записи.
- Поиск видит игры на один уровень папок глубже. Существующий приоритет внутренних установленных PKG сохранён; обычная вложенная копия не заменяет найденную непосредственно в корне.
- В карточке игры появился переключатель PlayGo stub. Он меняет только выбранную игру, сохраняет прежние исключения и блокируется во время игры или при выключенном глобальном PlayGo. Именные галочки в настройках остаются.
- Ошибка одного элемента массива настроек больше не отбрасывает следующие корректные элементы. В журнал добавлены время и длительность долгих операций.
- AMPR 0.5.0 содержит новые оптимизации чтения/индекса и исправления игр, перечисленные авторами. Скорость и совместимость именно этой сборки на консоли ещё не измерялись. Сообщение PLAY NO LIMIT теперь выдаёт TITAN; официальный модуль AMPR не изменён.

### Внешний диск
Архивы PKG на внешних накопителях разрешены **только внутри `homebrew` в корне диска и её подпапок**, например `/mnt/usb0/homebrew/Games/Game.pkg`. PKG в корне, Downloads и etaHEN/games не подхватываются. Внутренние игры, установленные системные PKG, обычные папки игр и образы ShadowMount сохраняют прежние правила. Оригиналы внешних PKG остаются на диске; диск нужен во время игры, а кэш занимает внутреннее место.

### Как обновиться
1. Закройте игры и полностью перезагрузите PS5.
2. Загрузите **TITAN-SirenaGoloviy-fix10.elf** через Payload Manager либо выберите FIX10 в обновляторе TITAN.
3. При обновлении через TITAN полностью перезапустите консоль и запустите сохранённый ELF. Обновите также старую копию в автозагрузке/Payload Manager, чтобы она не перезаписала подготовленную версию.
4. Откройте `http://IP_ПС5:8097` и дождитесь Ready. Не запускайте игру во время пересборки кэша.

ShadowMount **1.7beta12-titan-isolated4**, kstuff-lite **1.11** и PlayGo Stub **0.6** сохранены. Новый DLC-эмулятор не добавлялся. Настройки защищённого автоудаления плиток из FIX8 сохранены; это не удаление оригиналов или кэша.

### Проверки
93 теста Rust, 8 тестов PKG и 27 тестов JavaScript прошли — всего **128**. Проверены локализация, синтаксис интерфейса, обе стадии ELF, точное вложение stage1 и компонентов, SHA-256. Тесты выполнялись на Windows: Unix-проверки symlink и реальный directory fsync на ПК не выполнялись.

**На реальной PS5 эта сборка не проверена.** Не обещаем исправление 007 First Light или других ранее сообщённых вылетов без повторной проверки. Целевая конфигурация — 13.60. Нативный PKG-режим AMPR остаётся экспериментальным; PS4, retail/encrypted, AES-XTS и отдельные LIH-патчи не становятся поддерживаемыми.

Полные соответствующие исходники — **TITAN-SirenaGoloviy-fix10-source.zip** в Assets. Автоматический Source code GitHub содержит страницу распространения. Прежние релизы оставлены для отката. Авторство и лицензии сохранены.

Спасибо **quer3q**, **drakmor**, авторам TITAN CORE, AMPR, ShadowMount, kstuff и SDK, а также тестерам **@ImN3k1t** и **Владимиру Барсуку (@script_durova)** за сообщения об ошибках.

## English

FIX10 integrates Kraken Mount 0.3.1 and the official, unmodified AMPR 0.5.0 on top of FIX9 pre1. The console updater, rollback, backports, named PlayGo checkboxes, protected services and homebrew-only external PKG policy are retained.

On firmware without TitleDir, game registration is batched once per scan through AppInstallAll, with one notification. As upstream, that call refreshes registration metadata globally; TITAN stages/tracks native titles and keeps ownership and busy-mount guards. Metadata uses 1 MiB transfers with atomic publication. Discovery reaches one folder deeper. Game details now include a saved per-game PlayGo toggle. Config arrays skip invalid items, and logs include timestamps and operation durations.

AMPR 0.5.0 brings upstream read/index optimizations and game fixes. We have not measured their results on this combined build. TITAN supplies the custom PLAY NO LIMIT launch notice; AMPR retains its upstream identity. ShadowMount 1.7beta12-titan-isolated4, kstuff-lite 1.11 and PlayGo Stub 0.6 are unchanged; no new DLC emulator was added.

External archive PKGs must be under the drive-root `homebrew` directory or its subfolders. Keep the source drive connected during gameplay. Close games, fully reboot, launch the new ELF and wait for Ready. When updating through TITAN, reboot before launching the saved copy and update any older autoload/Payload Manager copy separately.

**128 host tests passed (93 Rust + 8 PKG + 27 JavaScript); both ELF stages and embedded components were verified. This build has not been tested on a real PS5.** Windows checks do not exercise Unix symlink assertions or real directory fsync. No console performance or individual game-crash fix is claimed; native PKG mode remains experimental. The earlier mid-build game-launch limitation remains: wait until preparation finishes.

Download the separately named source ZIP for complete matching sources. Earlier releases remain available for rollback. Upstream credits and license notices are preserved.
