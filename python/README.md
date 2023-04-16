

pyinstaller.exe --onedir --add-data "ikonki\*;ikonki" --add-data "identity.ini;." --add-data "strona\*;strona" --add-data "strona\styles\*;strona\styles" --path=. .\initWebhook.py --noconfirm