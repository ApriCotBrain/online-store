"""Field regexes for models of all apps."""

FIELD_REGEXES = {
    "category_name": r"[А-ЯЁа-яё, ]+$",
    "subcategory_name": r"[А-ЯЁа-яё, ]+$",
    "product_name": r"[a-zA-zА-ЯЁа-яё0-9, ]+$",
}
