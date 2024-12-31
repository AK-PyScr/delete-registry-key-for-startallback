import winreg

def delete_registry_key():
    try:
        # Открываем ключ HKEY_CURRENT_USER
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\CLSID",
            0,
            winreg.KEY_SET_VALUE
        )

        # Удаляем подключ {577254bc-7618-7681-c049-ab9be73e916}
        winreg.DeleteKey(registry_key, "{577254bc-7618-7681-c049-ab9be73e916}")
        winreg.CloseKey(registry_key)

        print("Ключ успешно удалён.")
    except FileNotFoundError:
        print("Ключ не найден.")
    except PermissionError:
        print("Недостаточно прав для удаления ключа. Запустите скрипт с правами администратора.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    delete_registry_key()
