import contextlib
import functools
import io
import os

from pathlib import Path
from typing import Callable, Union, Dict, Optional
from contextvars import ContextVar


_current_locale = ContextVar("_current_locale", default="en-US")

IN_MSGID = 2
IN_MSGSTR = 4

MSGID = 'msgid "'
MSGSTR = 'msgstr "'

_translators = []


def get_locale() -> str:
    return str(_current_locale.get())


def set_locale(locale: str):
    global _current_locale
    _current_locale = ContextVar("_current_locale", default=locale)
    reload_locales()


def _parse(translation_file: io.TextIOWrapper, locale: str) -> Dict[str, str]:
    step = None
    untranslated = ""
    translated = ""
    translations = {}

    translations[locale] = {}

    for line in translation_file:
        line = line.strip()

        if line.startswith(MSGID):
            if step is IN_MSGSTR and translated:
                translations[locale][_unescape(untranslated)] = _unescape(translated)
            step = IN_MSGID
            untranslated = line[len(MSGID) : -1]
        elif line.startswith('"') and line.endswith('"'):
            if step is IN_MSGID:
                untranslated += line[1:-1]
            elif step is IN_MSGSTR:
                translated += line[1:-1]
        elif line.startswith(MSGSTR):
            step = IN_MSGSTR
            translated = line[len(MSGSTR) : -1]
    
    if step is IN_MSGSTR and translated:
        translations[locale][_unescape(untranslated)] = _unescape(translated)
    return translations


def _unescape(string):
    string = string.replace(r"\\", "\\")
    string = string.replace(r"\t", "\t")
    string = string.replace(r"\r", "\r")
    string = string.replace(r"\n", "\n")
    string = string.replace(r"\"", '"')
    return string


def get_locale_path(cog_folder: Path, locale: str, extension: str) -> Path:
    return cog_folder / "locales" / "{}.{}".format(locale, extension)


class Translator(Callable[[str], str]):
    def __init__(self, name: str, file_location: Union[str, Path, os.PathLike]):
        self.cog_folder = Path(file_location).resolve().parent
        self.cog_name = name
        self.translations = {}

        _translators.append(self)

        self.load_translations()
    
    def __call__(self, untranslated: str, locale: str) -> str:
        print(locale, flush=True)
        print(self.translations, flush=True)
        try:
            print(self.translations[locale][untranslated], flush=True)
            return self.translations[locale][untranslated]
        except KeyError:
            print(untranslated, flush=True)
            return untranslated
    
    def load_translations(self):
        locales = [
            "en-US",
            "uk",
        ]

        for locale in locales:
            if locale.lower() == "en-us":
                pass
            elif locale in self.translations:
                pass
            else:
                locale_path = get_locale_path(self.cog_folder, locale, "po")
                with contextlib.suppress(IOError, FileNotFoundError):
                    with locale_path.open(encoding="utf-8") as file:
                        self._parse(file, locale)
    
    def _parse(self, translation_file, locale):
        self.translations.update(_parse(translation_file, locale))