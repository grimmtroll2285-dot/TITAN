"""Reconstruct FIX12 from the verified published FIX11 source and reviewed text patch."""
from pathlib import Path
import hashlib,subprocess,urllib.request,zipfile,shutil,json

repo=Path(__file__).resolve().parents[2]
work=repo/'rebuild';work.mkdir(exist_ok=True)
def fetch(url,path,expected):
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'TITAN-FIX12-build'}),timeout=90) as r:path.write_bytes(r.read())
    assert hashlib.sha256(path.read_bytes()).hexdigest()==expected,str(path)
base=work/'fix11-source.zip'
fetch('https://github.com/grimmtroll2285-dot/TITAN/releases/download/fix11/TITAN-SirenaGoloviy-fix11-source.zip',base,'46e9bec6ee678f1695d79fb82749b39b0321692102e7803ca06c4129343ab4d4')
source=work/'source'
if source.exists():raise SystemExit('Refusing to overwrite an existing reconstructed source tree')
source.mkdir()
with zipfile.ZipFile(base) as z:
    for info in z.infolist():
        rel=Path(*Path(info.filename).parts[1:])
        if not rel.parts:continue
        assert not rel.is_absolute() and '..' not in rel.parts
        dest=source/rel
        if info.is_dir():dest.mkdir(parents=True,exist_ok=True)
        else:dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(info))
# The published Windows source ZIP mixes CRLF/LF; the reviewed patch is canonical LF.
for path in source.rglob('*'):
    if path.is_file() and (path.suffix in {'.rs','.toml','.lock','.py','.js','.cjs','.mjs','.html','.json','.tsv','.md','.sh','.c','.h','.S','.link','.txt'} or path.name in {'VERSION','SHA256SUMS','.gitignore'}):
        data=path.read_bytes()
        try:data.decode('utf-8')
        except UnicodeDecodeError:continue
        path.write_bytes(data.replace(b'\r\n',b'\n'))
subprocess.run(['git','apply','--check',str(repo/'release/fix12/payload.patch')],cwd=source,check=True)
subprocess.run(['git','apply',str(repo/'release/fix12/payload.patch')],cwd=source,check=True)
v=source/'vendor/ampr-emu-ng'
fetch('https://github.com/quer3q/ampr-emu-ng/releases/download/v0.5.1/libSceAmpr.sprx',v/'libSceAmpr.sprx','7ca61afc444f0b44d2f005506dde16cb43e74dae4b1e045323b291b8db1c3d5d')
fetch('https://api.github.com/repos/quer3q/ampr-emu-ng/zipball/v0.5.1',v/'upstream-v0.5.1-source.zip','9c7f8ebffa360997e91a12e8e5632ccf02bceb5920fbaa99565173f6d3433645')
v=source/'vendor/kraken-mount';v.mkdir(exist_ok=True)
fetch('https://api.github.com/repos/quer3q/kraken-mount/zipball/v0.3.2',v/'upstream-v0.3.2-source.zip','6b8afe215ed0154f3e7529242083d458d20fb6a6894dc6a686c1d2de6399207c')
for name in ['README.md','README_EN.md','INSTALL_RU.md','INSTALL_EN.md','CREDITS.md','CREDITS_HISTORY.md','KRAKEN_0_3_2_UPGRADE.md','CHANGELOG_RU.md','BACKPORTS.md','PLAYGO_INTEGRATION.md','CONSOLE_UPDATER.md','VALIDATION.md']:
    shutil.copyfile(repo/name,source/name);shutil.copyfile(repo/name,source/'docs'/name)
for script in ['embed-monitor.py','embed-features.py','embed-localization.py']:
    subprocess.run(['python3',str(source/'review'/script)],cwd=source,check=True)
inputs=json.loads((repo/'release/fix12/source-inputs.json').read_text())
for name,expected in inputs.items():
    path=source/name
    assert path.is_file(),name
    assert hashlib.sha256(path.read_bytes().replace(b'\r\n',b'\n')).hexdigest()==expected,name
print('Reconstructed verified FIX12 sources:',source)
