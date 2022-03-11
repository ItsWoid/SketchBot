import os

import yaml


def _env_var_constructor(loader, node):

    default = None

    if node.id == 'scalar':
        value = loader.construct_scalar(node)
        key = str(value)
    else:
        value = loader.construct_sequence(node)

        if len(value) >= 2:
            default = value[1]
            key = value[0]
        else:
            key = value[0]

    return os.getenv(key, default)


yaml.SafeLoader.add_constructor("!ENV", _env_var_constructor)


with open("config.yml", encoding="UTF-8") as f:
    _CONFIG_YAML = yaml.safe_load(f)


class YAMLGetter(type):

    subsection = None

    def __getattr__(cls, name):
        name = name.lower()

        try:
            if cls.subsection is not None:
                print(_CONFIG_YAML[cls.section][cls.subsection][name], flush=True)
                return _CONFIG_YAML[cls.section][cls.subsection][name]
            print(_CONFIG_YAML[cls.section][name], flush=True)
            return _CONFIG_YAML[cls.section][name]
        except KeyError as e:
            dotted_path = '.'.join(
                (cls.section, cls.subsection, name)
                if cls.subsection is not None else (cls.section, name)
            )
            print(f"Tried accessing configuration variable at `{dotted_path}`, but it could not be found.")
            raise AttributeError(repr(name)) from e

    def __getitem__(cls, name):
        return cls.__getattr__(name)

    def __iter__(cls):
        for name in cls.__annotations__:
            yield name, getattr(cls, name)


class Bot(metaclass=YAMLGetter):
    section = "bot"

    token: str
    db: str


class Colours(metaclass=YAMLGetter):
    section = "style"
    subsection = "colours"

    pastel_purple: int