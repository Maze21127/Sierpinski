from cx_Freeze import setup, Executable

ico = 'icon.ico'
executables = [Executable('main.py', target_name='sierpinski.exe', icon=ico, base="Win32GUI")]

excludes = ['venv']


options = {'build_exe': {
      'include_msvcr': True,
      'excludes': excludes,
      }
}

setup(name='Sierpinski',
      version='1',
      description='Треугольник серпинского',
      executables=executables,
      options=options
      )
