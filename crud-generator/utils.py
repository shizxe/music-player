import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from config import PROJECT_ROOT

SNAKE_PATTERN = re.compile(r"(?<!^)(?=[A-Z])")


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def snake_case(value: str) -> str:
    if not value:
        return ""

    value = re.sub(r"[^A-Za-z0-9]+", "_", value)
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", value)
    value = re.sub(r"(?<=[A-Za-z])(?=[A-Z][a-z])", "_", value)
    value = re.sub(r"_+", "_", value).strip("_").lower()
    return value


def pluralize(value: str) -> str:
    lowered = value.lower()
    if lowered.endswith("y") and len(lowered) > 1 and lowered[-2] not in "aeiou":
        return lowered[:-1] + "ies"
    if lowered.endswith(("s", "x", "z", "ch", "sh")):
        return lowered + "es"
    return lowered + "s"


def class_name(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", " ", value).strip()
    return "".join(word.capitalize() for word in value.split())


def singular_table_name(value: str) -> str:
    if not value:
        return value
    if value.endswith("ies"):
        return value[:-3] + "y"
    if value.endswith("sses"):
        return value[:-2]
    if value.endswith("ses"):
        return value[:-2]
    if value.endswith("s") and len(value) > 1:
        return value[:-1]
    return value


def table_name_for_model(model_name: str, explicit_table: str | None = None) -> str:
    if explicit_table:
        return explicit_table.strip().lower()

    return pluralize(snake_case(model_name))


def route_name_for_table(table_name: str) -> str:
    return table_name.replace("_", "-")


def normalize_field_token(token: str) -> dict[str, Any]:
    parts = [part.strip() for part in token.split(":") if part.strip()]
    if not parts:
        return {}

    name = parts[0]
    raw_type = parts[1] if len(parts) > 1 else "string"
    modifiers = [m.strip().lower() for m in parts[2:] if m.strip()]

    type_name = raw_type.lower()
    if type_name in {"email", "password"}:
        canonical_type = "string"
    elif type_name in {"bool"}:
        canonical_type = "boolean"
    elif type_name in {"int"}:
        canonical_type = "integer"
    else:
        canonical_type = type_name

    if "nullable" in modifiers:
        nullable = True
    else:
        nullable = False

    return {
        "name": snake_case(name),
        "type": canonical_type,
        "raw_type": raw_type,
        "nullable": nullable,
        "modifiers": modifiers,
    }


def parse_fields(fields_value: str | None) -> list[dict[str, Any]]:
    if not fields_value:
        return []

    tokens = [token.strip() for token in fields_value.split(",") if token.strip()]
    return [normalize_field_token(token) for token in tokens if normalize_field_token(token)]


def migration_type(field: dict[str, Any]) -> str:
    raw = field["raw_type"].lower()
    if raw.startswith("string"):
        return raw
    if raw.startswith("decimal"):
        return raw
    mapping = {
        "id": "unsignedBigInteger",
        "bigint": "bigInteger",
        "integer": "integer",
        "int": "integer",
        "boolean": "boolean",
        "bool": "boolean",
        "text": "text",
        "date": "date",
        "datetime": "dateTime",
        "time": "time",
        "json": "json",
        "float": "float",
        "double": "double",
        "uuid": "uuid",
        "enum": "enum",
        "jsonb": "json",
    }
    return mapping.get(raw, "string")


def validation_rule(field: dict[str, Any], update: bool = False) -> str:
    rules: list[str] = []
    if update:
        rules.append("sometimes")

    if field["nullable"]:
        rules.append("nullable")
    else:
        rules.append("required")

    field_type = field["type"]
    if field_type == "email":
        rules.append("email")
    elif field_type == "boolean":
        rules.append("boolean")
    elif field_type in {"integer", "bigInteger", "unsignedBigInteger", "int"}:
        rules.append("integer")
    elif field_type in {"json", "array"}:
        rules.append("array")
    elif field_type in {"date", "dateTime", "time"}:
        rules.append("date")
    else:
        rules.append("string")

    if field["raw_type"].lower() == "password" and not field["nullable"]:
        rules.append("min:8")

    return "|".join(rules)


def load_file_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_file_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def unique_migration_filename(table_name: str) -> str:
    base_time = datetime.now()
    timestamp = base_time.strftime("%Y_%m_%d_%H%M%S")
    filename = f"{timestamp}_create_{table_name}_table.php"
    migration_path = PROJECT_ROOT / "database" / "migrations" / filename
    index = 1
    while migration_path.exists():
        filename = f"{timestamp}_{index}_create_{table_name}_table.php"
        migration_path = PROJECT_ROOT / "database" / "migrations" / filename
        index += 1
    return filename


def normalize_model_name(value: str) -> str:
    return class_name(value)


def normalize_table_name(value: str | None, model: str) -> str:
    if value and value.strip():
        return value.strip().lower()
    return table_name_for_model(model)
