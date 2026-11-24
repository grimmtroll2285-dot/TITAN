"""Validate both ELF stages and their exact embedded inputs, then package release assets."""
from pathlib import Path
import hashlib,json,shutil,struct,zipfile,re
repo=Path(__file__).resolve().parents[2];source=repo/'rebuild/source';out=repo/'release-assets';out.mkdir(exist_ok=True)
def digest(data):return hashlib.sha256(data).hexdigest()
def elf(data):
    assert data[:6]==b'\x7fELF\x02\x01'
    assert struct.unpack_from('<HH',data,16)==(3,62)
    entry,phoff=struct.unpack_from('<QQ',data,24);ents,n=struct.unpack_from('<HH',data,54)
    ph=[struct.unpack_from('<IIQQQQQQ',data,phoff+i*ents) for i in range(n)]
    assert any(t==1 and flags&1 and va<=entry<va+ms for t,flags,o,va,pa,fs,ms,al in ph)
    dyn=next(p for p in ph if p[0]==2);entries=[]
    for off in range(dyn[2],dyn[2]+dyn[5],16):
        key,value=struct.unpack_from('<QQ',data,off)
        if key==0:break
        entries.append((key,value))
    strings=next(v for k,v in entries if k==5)
    seg=next(p for p in ph if p[0]==1 and p[3]<=strings<p[3]+p[5]);start=seg[2]+strings-seg[3]
    needed=[data[start+v:data.index(0,start+v)].decode() for k,v in entries if k==1]
    assert 'libkernel_web.sprx' in needed
    return {'bytes':len(data),'sha256':digest(data),'entry':hex(entry),'type':'ELF64 x86-64 ET_DYN','executable_entry':True,'needed':needed}
a=(source/'target/ps5/titan-core-stage1.elf').read_bytes();b=(source/'target/ps5/titan-core.elf').read_bytes();ui=(source/'src/ui.html').read_bytes()
assert a in b and ui in a
components={}
for name in ['unified/kstuff-lite-v1.11.elf','unified/shadowmountplus-1.7beta12-titan-isolated4.elf','ampr-emu-ng/libSceAmpr.sprx','playgo/libScePlayGo.sprx']:
    data=(source/'vendor'/name).read_bytes();assert data in a,name;components[name]=digest(data)
assert components['ampr-emu-ng/libSceAmpr.sprx']=='7ca61afc444f0b44d2f005506dde16cb43e74dae4b1e045323b291b8db1c3d5d'
assert 'version = "1.0.10"' in (source/'Cargo.toml').read_text()
v={'version':'1.0.10','tag':'fix12','base':'fix11','repository':'grimmtroll2285-dot/TITAN','prerelease':False,'stage1':elf(a),'stage2':elf(b),'embedded_components':components,'stage1_embedded_exactly':True,'ui_source_embedded_exactly':True,'tests':{'portable_rust':104,'pkg_library':8,'javascript':27,'passed':139,'additional_host_suite':94,'additional_host_suite_overlaps_portable':True},'browser_fixture_checks':['search','PKG overlay protection','native launch request','folder overlay toggle','last crash and text report','excluded-path save','390px mobile no overflow'],'hardware_tested':False,'console_benchmarks_run':False,'known_limitations':['Native PKG mode remains experimental','Forza Horizon 5 PKG crash is not confirmed fixed; upstream explicitly excludes a fix in Kraken 0.3.2','Game-start during cache build race remains; wait for Ready','Full reboot required when migrating from older payloads without lifetime lock'],'toolchain':{'rust':'1.99.0','llvm':'19','sdk':'0.43','compiler_jobs':2,'host':'Linux cross-build'}}
(source/'docs/FIX12_VALIDATION.json').write_text(json.dumps(v,indent=2)+'\n')
(out/'TITAN-SirenaGoloviy-fix12.elf').write_bytes(b)
for name in ['README.md','README_EN.md','INSTALL_RU.md','INSTALL_EN.md','CREDITS.md','CREDITS_HISTORY.md','KRAKEN_0_3_2_UPGRADE.md','VALIDATION.md','RELEASE-NOTES.txt']:
    shutil.copyfile(repo/name,out/name)
shutil.copyfile(repo/'INSTALL_RU.md',out/'README.txt')
icons=json.loads((repo/'icons.json').read_text());image=next(iter(icons['icons'].values()));icons['icons']={'titan-fix12':image};(repo/'icons.json').write_text(json.dumps(icons,ensure_ascii=False,indent=2)+'\n')
catalog=json.loads((repo/'payloads.json').read_text());catalog['icons_url']='https://github.com/grimmtroll2285-dot/TITAN/releases/download/fix12/icons.json'
item=catalog['payloads'][0];item.update(filename='TITAN-SirenaGoloviy-fix12.elf',url='https://github.com/grimmtroll2285-dot/TITAN/releases/download/fix12/TITAN-SirenaGoloviy-fix12.elf',version='1.0.10',last_update='2026-11-24',description='FIX12 stable: Kraken 0.3.2, official AMPR 0.5.1, exit lifecycle, game reports, Playden API, library search and lifetime instance lock. PS5 validation pending.',checksum=v['stage2']['sha256'],icon_key='titan-fix12',details_url='https://github.com/grimmtroll2285-dot/TITAN/releases/tag/fix12')
(repo/'payloads.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
for name in ['icons.json','payloads.json']:shutil.copyfile(repo/name,out/name)
archive=out/'TITAN-SirenaGoloviy-fix12-source.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for path in sorted(source.rglob('*')):
        rel=path.relative_to(source)
        if any(p in {'.git','target','__pycache__','.playwright-cli','output','dist','node_modules'} for p in rel.parts) or path.suffix in {'.log','.pyc'} or path.name.startswith('owner-'):continue
        if path.is_file():z.write(path,Path('TITAN-SirenaGoloviy-fix12-source')/rel)
v['source_zip']={'sha256':digest(archive.read_bytes()),'bytes':archive.stat().st_size}
for base in [repo,out]:(base/'validation.json').write_text(json.dumps(v,indent=2)+'\n')
shutil.copyfile(source/'target/ps5/titan-core.elf.txt',out/'ELF-HEADERS.txt')
sums=''.join(f'{digest(p.read_bytes())}  {p.name}\n' for p in sorted(out.iterdir()) if p.is_file() and p.name!='SHA256SUMS.txt')
for base in [repo,out]:(base/'SHA256SUMS.txt').write_text(sums)
print(json.dumps({'version':v['version'],'stage2_sha256':v['stage2']['sha256'],'source':v['source_zip']},indent=2))
