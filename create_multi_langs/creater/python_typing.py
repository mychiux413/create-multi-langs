from __future__ import absolute_import
from create_multi_langs.creater.base import CreaterBase
from . import to_upper, to_lower, split_camelcase


class CreaterPythonTyping(CreaterBase):

    @staticmethod
    def from_csv_file(csv_file: str, output_code_file: str):
        assert output_code_file.endswith(".py"), \
            "python filename must ends with .py"
        creater = CreaterPythonTyping(
            csv_file,
            output_code_file,
            comment_head_prefix='"""',
            comment_tail_prefix="",
            comment_mid_prefix='"""',
            template_path="data/python/template_typing.tmpl",
            field_wrapper=lambda x: to_lower(split_camelcase(x)),
        )
        return creater

    @property
    def dict_contents(self) -> str:
        outs = []
        for lang_code in self._reader.lang_codes():
            out = ""
            out += self._templater.spaces(1) + '"' + lang_code + '"' + ': {\n'
            out += self._templater.key_value_lines(
                key_values=self._reader.field_values(lang_code),
                double_quote_key=True,
                double_quote_value=True,
                split_punctuation=": ",
                end_punctuation=",",
                n_indent=2,
            )
            out += "\n" + self._templater.spaces(1) + "},"
            outs.append(out)
        return '\n'.join(outs)

    @property
    def lang_code_constants(self) -> str:
        data = {}
        for lang_code in self._reader.lang_codes():
            data[to_upper(lang_code, non_en_repl='_')] = lang_code
        return self._templater.key_value_lines(
            key_values=data,
            double_quote_key=False,
            double_quote_value=True,
            split_punctuation=" = ",
            end_punctuation="",
        )

    @property
    def valid_lang_codes(self) -> str:
        data = {}
        for lang_code in self._reader.lang_codes():
            data['- "{}"'.format(lang_code)] = ""
        return self._templater.key_value_lines(
            key_values=data,
            double_quote_key=False,
            double_quote_value=False,
            split_punctuation="",
            end_punctuation="",
            n_indent=2,
        )

    @property
    def properties(self) -> str:
        outs = []
        for field, note in self._reader.field_notes().items():
            out = ""
            out += self._templater.spaces(1) + "@property\n"
            out += self._templater.spaces(1) + \
                "def {}(self) -> str:\n".format(field)
            out += self._templater.spaces(2) + '"' * 3 + note + '"' * 3 + '\n'
            out += self._templater.spaces(2) + \
                'return self._data["{}"]'.format(field)
            outs.append(out)
        return '\n\n'.join(outs) + '\n'

    def render_data(self) -> dict:
        return {
            'dict_contents': self.dict_contents,
            'lang_code_constants': self.lang_code_constants,
            'valid_lang_codes': self.valid_lang_codes,
            'properties': self.properties,
        }
