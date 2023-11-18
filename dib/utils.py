import argparse
from typing import Type

import pydantic


def arguments_from_pydantic(parser: argparse.ArgumentParser, model: Type[pydantic.BaseModel]):
    """
    Add Pydantic model to an ArgumentParser
    Ideas from: https://stackoverflow.com/questions/72741663/argument-parser-from-a-pydantic-model
    """
    fields = model.model_fields
    for name, field in fields.items():
        parser.add_argument(
            f"--{name}",
            dest=name,
            type=field.annotation,
            default=field.default,
            help=field.description,
        )
