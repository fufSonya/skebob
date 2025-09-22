import os
import shlex

def expand_vars(command: str) -> str:
    return os.path.expandvars(command)

def parse_command(command: str):
    return shlex.split(command)

def main():
    VFS_NAME = "skebob"

    while True:
        try:
            raw_command = input(f"{VFS_NAME}> ").strip()
            if not raw_command:
                continue
            expanded_command = expand_vars(raw_command)
            args = parse_command(expanded_command)
        except KeyboardInterrupt:
            print("\nОкончание работы программы")
            break
        except Exception as e:
            print(f"Ошибка парсинга: {e}")
            continue

        cmd = args[0]

        if cmd == "exit":
            print("Выход...")
            break
        elif cmd == "ls":
            print(f"[ls] Аргументы: {args[1:]}")
        elif cmd == "cd":
            print(f"[cd] Аргументы: {args[1:]}")
        else:
            print(f"Неизвестная команда: {cmd}")

if __name__ == "__main__":
    main()
