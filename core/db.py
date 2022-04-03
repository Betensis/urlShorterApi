from importlib.machinery import SourceFileLoader
from pathlib import Path

import databases
import ormar
import sqlalchemy

from settings import DB_DSN, MODEL_DIRS

db = databases.Database(DB_DSN)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DB_DSN)


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = db


class BaseModel(ormar.Model):
    class Meta(BaseMeta):
        abstract = True

    id: int = ormar.Integer(primary_key=True)


def import_models() -> None:
    excluded_dir_names = [
        "__pycache__",
    ]
    excluded_file_names = ["__init__.py"]

    def import_models_by_file(file_path: Path) -> None:
        file_content = SourceFileLoader(
            "some_module.name", str(file_path.resolve())
        ).load_module()
        # models = {}
        # for variable_name, variable_value in file_content.items():
        #     if not isclass(variable_value):
        #         continue
        #
        #     if issubclass(variable_value, ormar.Model):
        #         models[variable_name] = variable_value
        #
        # return models

    def create_models_tables_by_dir(model_dir: Path):
        for file_or_dir in model_dir.iterdir():
            if file_or_dir.is_dir() and file_or_dir.name in excluded_dir_names:
                continue
            if file_or_dir.is_dir():
                create_models_tables_by_dir(file_or_dir)

            file = file_or_dir
            if not file.name.endswith(".py") or file.name in excluded_file_names:
                continue

            import_models_by_file(file)
            # for model_class in model_classes.values():
            #     if model_class.Meta.abstract:
            #         continue
            #     model_class.Meta.table.create(engine)

    for model_dir in MODEL_DIRS:
        create_models_tables_by_dir(model_dir)
