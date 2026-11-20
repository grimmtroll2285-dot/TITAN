# TITAN · FIX11 · 1.0.9

**PLAY NO LIMIT by SirenaGoloviy**

## Русский

Исправляющий выпуск поверх FIX10. Устраняет несовместимость служебных записей установленных PKG после переименования TITAN CORE в TITAN.

Старая запись с `owner: TITAN CORE` раньше отклонялась сообщением **Installed source receipt belongs to another source**. Теперь TITAN распознаёт прежнее имя владельца, проверяет Title ID и исходный путь и атомарно сохраняет запись в текущем формате. При совпадении файла сохраняются записанные исходные права, inode/device и размер. PKG остаётся в исходном системном месте; миграция не переносит и не удаляет игру.

Чужие владельцы, несовпадающие Title ID и пути по-прежнему отклоняются. Проверки обычного файла, symlink и изменения источника во время подготовки сохранены.

Сохранены все функции FIX10: Kraken 0.3.1, официальный AMPR 0.5.0, пакетная регистрация, PlayGo, обновлятор, бэкпорты и внешние PKG только из `homebrew` и её подпапок. ShadowMount 1.7beta12-titan-isolated4, kstuff-lite 1.11 и PlayGo Stub 0.6 не менялись.

### Обновление
Закройте игры, полностью перезагрузите PS5 и запустите **TITAN-SirenaGoloviy-fix11.elf**. Если используете обновлятор TITAN, подготовьте FIX11, затем полностью перезагрузите консоль и запустите сохранённую копию. Замените старый ELF в Payload Manager/автозагрузке. Дождитесь Ready перед запуском игры. Совместимая старая запись исправится при следующей подготовке установленного PKG; вручную удалять запись для этой миграции не требуется.

### Проверки
97 тестов Rust (включая четыре новых сценария миграции), 8 тестов чтения PKG и 27 тестов JavaScript прошли — всего **132**. Проверка типов FreeBSD/unified-stack завершилась без предупреждений. Обе стадии ELF собраны, вложенный stage1 и компоненты проверены, контрольные суммы приложены.

**На реальной PS5 исправление ещё не проверено.** Файл записи PPSA12544 с консоли не предоставлен: исправлен подтверждённый в коде сценарий старого имени владельца. Если конкретная запись содержит другой путь или Title ID, защита продолжит её отклонять. Исправление других вылетов, включая 007 First Light, не заявляется. Windows-проверки не выполняют Unix-assertions для symlink и реальный directory fsync.

Полные соответствующие исходники — **TITAN-SirenaGoloviy-fix11-source.zip**, а не автоматический Source code GitHub. Предыдущие выпуски сохранены для отката. Авторство и лицензии upstream сохранены.

## English

FIX11 fixes installed-PKG receipt compatibility after the TITAN CORE → TITAN rename. Older `TITAN CORE` owner labels caused **Installed source receipt belongs to another source**. The old label is now accepted only for the exact expected title and source path, and normalized atomically. For an unchanged file, the original permission history, identity and size remain intact. The PKG stays in its original location.

Foreign owners and mismatching titles/paths remain rejected; regular-file, symlink and source-change guards are retained. All FIX10 features and bundled service binaries remain available, including Kraken 0.3.1, AMPR 0.5.0, PlayGo, the updater and homebrew-only external PKG playback.

Close games, fully reboot, launch the new ELF and wait for Ready. When using TITAN's updater, reboot after preparing the update and update any older Payload Manager/autoload copy separately. Compatible legacy receipts migrate when the installed game is prepared.

**132 host tests passed (97 Rust + 8 PKG + 27 JavaScript), FreeBSD types checked and both ELF stages verified. No PS5 hardware validation was performed.** The actual PPSA12544 receipt was not supplied; different-path/title conflicts remain protected. No unrelated game-crash fix is claimed. Windows tests do not exercise Unix symlink assertions or real directory fsync.

Use the separately named source ZIP for complete matching sources. Earlier releases remain available for rollback; upstream authorship and licenses are preserved.
