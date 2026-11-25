import json
from pathlib import Path
from tempfile import TemporaryDirectory

from logic import add_record
from storage import load_records, save_records

RECORDS = [
    {"id": 1, "title": "Хакатон", "category": "конференции", "amount": 40,
     "completed": False},
    {"id": 2, "title": "Встреча", "category": "встречи", "amount": 25,
     "completed": True},
]

with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"

    # сохранение и повторная загрузка: все поля и статусы восстановлены
    save_records(path, RECORDS)
    assert load_records(path) == RECORDS
    assert "Хакатон" in path.read_text(encoding="utf-8")  # кириллица читаема
    assert not Path(str(path) + ".tmp").exists()

    # пустой список
    empty = Path(directory) / "empty.json"
    empty.write_text("[]", encoding="utf-8")
    assert load_records(empty) == []

    # нового id после загрузки
    loaded = load_records(path)
    assert add_record(loaded, "Новое", "встречи", 1)["id"] == 3

    # отсутствующий файл
    try:
        load_records(Path(directory) / "net.json")
    except FileNotFoundError:
        pass
    else:
        assert False, "Ожидался FileNotFoundError"

    # повреждённый JSON, неверная кодировка, повторный id — файл не меняется
    def expect(exc, content, name):
        target = Path(directory) / name
        if isinstance(content, bytes):
            target.write_bytes(content)
        else:
            target.write_text(content, encoding="utf-8")
        before = target.read_bytes()
        try:
            load_records(target)
        except exc:
            pass
        else:
            assert False, f"{name}: ожидался {exc.__name__}"
        assert target.read_bytes() == before

    expect(json.JSONDecodeError, "[{'id': 1}", "broken.json")
    expect(UnicodeError, b"\xff\xfe\x00", "encoding.json")
    duplicate = [dict(RECORDS[0]), dict(RECORDS[1], id=1)]
    expect(ValueError, json.dumps(duplicate), "duplicate.json")
    expect(ValueError, '{"id": 1}', "not_list.json")

    # ошибка сохранения: нет папки -> OSError, прежний файл не тронут
    try:
        save_records(Path(directory) / "net_papki" / "data.json", RECORDS)
    except OSError:
        pass
    else:
        assert False, "Ожидался OSError"

    # ошибка сериализации не портит прежний файл
    before = path.read_bytes()
    try:
        save_records(path, [{"id": 1, "bad": object()}])
    except TypeError:
        pass
    else:
        assert False, "Ожидался TypeError"
    assert path.read_bytes() == before
    assert not Path(str(path) + ".tmp").exists()

print("Все проверки test_storage пройдены")
