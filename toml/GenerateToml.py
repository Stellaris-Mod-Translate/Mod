from pathlib import Path

def is_mod_directory(path):
    return (path / 'en').is_dir()

def write_toml(file, name):
    file.write('basepath = \"..\"\n\n')
    file.write('[[pahts]]\n')
    file.write(f'\treference = \"{name}/en/*.yml\"\n')
    file.write(f'\treference = \"{name}/{{locale}}/*.yml\"')

def main():
    toml_path = Path.cwd()
    mods_path = toml_path.parent
    mod_path_lists = [mod_path for mod_path in mods_path.iterdir() if is_mod_directory(mod_path)]

    for mod_path in mod_path_lists:
        toml_file_path = toml_path / (mod_path.name + '.toml')
        with toml_file_path.open(mode='w', encoding='utf-8') as f:
            write_toml(f, mod_path.name)
            print(f'Write {toml_file_path.name}')

if __name__ == "__main__":
    main()