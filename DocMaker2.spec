# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['DocMaker2.py'],
             pathex=['./venv2/Lib/', 'D:\\Project Buffer\\Collstuff\\WEEKLY CODING CHALLENGE\\Software\\DocumentMaker2'],
             binaries=[],
             datas=[],
             hiddenimports=['pygments', 'cefpython3'],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='DocMaker2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='res\\Icon\\DocMaker.ico')
