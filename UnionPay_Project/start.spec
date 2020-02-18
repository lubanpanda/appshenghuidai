# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['start.py'],
             pathex=['C:\\Users\\found\\Desktop\\UnionPay_Project\\UnionPay\\certification_case_set.py', 'C:\\Users\\found\\Desktop\\UnionPay_Project\\UnionPay\\common.py', 'C:\\Users\\found\\Desktop\\UnionPay_Project\\UnionPay\\common.py', 'C:\\Users\\found\\Desktop\\UnionPay_Project'],
             binaries=[],
             datas=[],
             hiddenimports=['common', 'certification_case_set', 'custom_case_set'],
             hookspath=[],
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
          name='start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
