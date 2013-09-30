# -*- mode: python -*-
a = Analysis(['ComparePrice.py'],
             pathex=['E:\\workspace\\GitHub\\ComparePrice'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ComparePrice_W.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
