"""
GenSym — Fundamental Units of Sense
128 символів для генеративної фантастики.

Використання:
    python3 gensym.py          # 4 головних символи
    python3 gensym.py 7        # 7 головних символів
    python3 gensym.py 4 deep   # 4 головних + по 4 деталі для кожного
"""

import secrets
import sys

SYMBOLS = {
    # 1. Сили / Forces
    1:   {"en": "Transformation", "uk": "Трансформація"},
    2:   {"en": "Stasis",         "uk": "Застій"},
    3:   {"en": "Dissolution",    "uk": "Розпад"},
    4:   {"en": "Birth",          "uk": "Народження"},
    5:   {"en": "Void",           "uk": "Порожнеча"},
    6:   {"en": "Emergence",      "uk": "Поява"},
    7:   {"en": "Tension",        "uk": "Натяг"},
    8:   {"en": "Release",        "uk": "Вивільнення"},
    # 2. Рух / Space & Movement
    9:   {"en": "Ascent",         "uk": "Підйом"},
    10:  {"en": "Descent",        "uk": "Спуск"},
    11:  {"en": "Crossing",       "uk": "Перетин"},
    12:  {"en": "Threshold",      "uk": "Поріг"},
    13:  {"en": "Center",         "uk": "Центр"},
    14:  {"en": "Boundary",       "uk": "Межа"},
    15:  {"en": "Exile",          "uk": "Вигнання"},
    16:  {"en": "Return",         "uk": "Повернення"},
    # 3. Стани / States
    17:  {"en": "Awakening",      "uk": "Пробудження"},
    18:  {"en": "Sleep",          "uk": "Сон"},
    19:  {"en": "Blindness",      "uk": "Сліпота"},
    20:  {"en": "Insight",        "uk": "Прозріння"},
    21:  {"en": "Memory",         "uk": "Пам'ять"},
    22:  {"en": "Oblivion",       "uk": "Забуття"},
    23:  {"en": "Solitude",       "uk": "Самотність"},
    24:  {"en": "Connection",     "uk": "З'єднання"},
    # 4. Дії / Actions
    25:  {"en": "Search",         "uk": "Пошук"},
    26:  {"en": "Flight",         "uk": "Втеча"},
    27:  {"en": "Creation",       "uk": "Творення"},
    28:  {"en": "Destruction",    "uk": "Руйнування"},
    29:  {"en": "Sacrifice",      "uk": "Жертва"},
    30:  {"en": "Revelation",     "uk": "Одкровення"},
    31:  {"en": "Choice",         "uk": "Вибір"},
    32:  {"en": "Consequence",    "uk": "Наслідок"},
    # 5. Стосунки / Relations
    33:  {"en": "Union",          "uk": "Союз"},
    34:  {"en": "Separation",     "uk": "Розлука"},
    35:  {"en": "Betrayal",       "uk": "Зрада"},
    36:  {"en": "Loyalty",        "uk": "Вірність"},
    37:  {"en": "Power",          "uk": "Влада"},
    38:  {"en": "Submission",     "uk": "Підкорення"},
    39:  {"en": "Protection",     "uk": "Захист"},
    40:  {"en": "Dependence",     "uk": "Залежність"},
    # 6. Архетипи / Archetypes
    41:  {"en": "Seeker",         "uk": "Шукач"},
    42:  {"en": "Guardian",       "uk": "Страж"},
    43:  {"en": "Trickster",      "uk": "Трікстер"},
    44:  {"en": "Shadow",         "uk": "Тінь"},
    45:  {"en": "Child",          "uk": "Дитина"},
    46:  {"en": "Sage",           "uk": "Мудрець"},
    47:  {"en": "Destroyer",      "uk": "Руйнівник"},
    48:  {"en": "Builder",        "uk": "Будівничий"},
    # 7. Елементи / Elements
    49:  {"en": "Fire",           "uk": "Вогонь"},
    50:  {"en": "Water",          "uk": "Вода"},
    51:  {"en": "Earth",          "uk": "Земля"},
    52:  {"en": "Air",            "uk": "Повітря"},
    53:  {"en": "Time",           "uk": "Час"},
    54:  {"en": "Light",          "uk": "Світло"},
    55:  {"en": "Darkness",       "uk": "Темрява"},
    56:  {"en": "Abyss",          "uk": "Безодня"},
    # 8. Психологія / Psychology
    57:  {"en": "Doubt",          "uk": "Сумнів"},
    58:  {"en": "Confidence",     "uk": "Впевненість"},
    59:  {"en": "Guilt",          "uk": "Провина"},
    60:  {"en": "Forgiveness",    "uk": "Прощення"},
    61:  {"en": "Wonder",         "uk": "Захоплення"},
    62:  {"en": "Fear",           "uk": "Страх"},
    63:  {"en": "Longing",        "uk": "Туга"},
    64:  {"en": "Rage",           "uk": "Гнів"},
    # 9. Пізнання / Cognition
    65:  {"en": "Discovery",      "uk": "Відкриття"},
    66:  {"en": "Deception",      "uk": "Омана"},
    67:  {"en": "Intuition",      "uk": "Інтуїція"},
    68:  {"en": "Logic",          "uk": "Логіка"},
    69:  {"en": "Mystery",        "uk": "Таємниця"},
    70:  {"en": "Disclosure",     "uk": "Розкриття"},
    71:  {"en": "Question",       "uk": "Питання"},
    72:  {"en": "Answer",         "uk": "Відповідь"},
    # 10. Час / Temporal
    73:  {"en": "Beginning",      "uk": "Початок"},
    74:  {"en": "End",            "uk": "Кінець"},
    75:  {"en": "Cycle",          "uk": "Цикл"},
    76:  {"en": "Moment",         "uk": "Мить"},
    77:  {"en": "Eternity",       "uk": "Вічність"},
    78:  {"en": "Anticipation",   "uk": "Очікування"},
    79:  {"en": "Resonance",      "uk": "Резонанс"},
    80:  {"en": "Foresight",      "uk": "Передчуття"},
    # 11. Конфлікт / Conflict
    81:  {"en": "Confrontation",  "uk": "Протистояння"},
    82:  {"en": "Surrender",      "uk": "Капітуляція"},
    83:  {"en": "Death",           "uk": "Смерть"},
    84:  {"en": "Victory",        "uk": "Перемога"},
    85:  {"en": "Love",            "uk": "Любов"},
    86:  {"en": "Entropy",        "uk": "Ентропія"},
    87:  {"en": "Rebellion",      "uk": "Бунт"},
    88:  {"en": "Acceptance",     "uk": "Прийняття"},
    # 12. Природа / Nature & Cosmos
    89:  {"en": "Storm",          "uk": "Буря"},
    90:  {"en": "Silence",        "uk": "Тиша"},
    91:  {"en": "Chaos",          "uk": "Хаос"},
    92:  {"en": "Order",          "uk": "Порядок"},
    93:  {"en": "Growth",         "uk": "Ріст"},
    94:  {"en": "Consciousness",   "uk": "Свідомість"},
    95:  {"en": "Will",            "uk": "Воля"},
    96:  {"en": "Asymmetry",      "uk": "Асиметрія"},
    # 13. Тіло / Body & Matter
    97:  {"en": "Pain",           "uk": "Біль"},
    98:  {"en": "Healing",        "uk": "Зцілення"},
    99:  {"en": "Hunger",         "uk": "Голод"},
    100: {"en": "Flow",           "uk": "Потік"},
    101: {"en": "Fatigue",        "uk": "Втома"},
    102: {"en": "Strength",       "uk": "Сила"},
    103: {"en": "Touch",          "uk": "Дотик"},
    104: {"en": "Distance",       "uk": "Відстань"},
    # 14. Соціальне / Social
    105: {"en": "Community",      "uk": "Спільнота"},
    106: {"en": "Catalyst",       "uk": "Каталіз"},
    107: {"en": "Leader",         "uk": "Лідер"},
    108: {"en": "Quantity",        "uk": "Кількість"},
    109: {"en": "Mask",           "uk": "Маска"},
    110: {"en": "Authenticity",   "uk": "Справжність"},
    111: {"en": "Signal",         "uk": "Сигнал"},
    112: {"en": "Legacy",         "uk": "Спадщина"},
    # 15. Абстрактне / Abstract
    113: {"en": "Balance",        "uk": "Баланс"},
    114: {"en": "Paradox",        "uk": "Парадокс"},
    115: {"en": "Illusion",       "uk": "Ілюзія"},
    116: {"en": "Reality",        "uk": "Реальність"},
    117: {"en": "Symbol",         "uk": "Символ"},
    118: {"en": "Rhythm",         "uk": "Ритм"},
    119: {"en": "Feedback",       "uk": "Зворотній зв'язок"},
    120: {"en": "Myth",           "uk": "Міф"},
    # 16. Структурне / Structural
    121: {"en": "Relation",       "uk": "Відношення"},
    122: {"en": "Pattern",        "uk": "Патерн"},
    123: {"en": "Polarity",       "uk": "Полярність"},
    124: {"en": "Synthesis",      "uk": "Синтез"},
    125: {"en": "Recursion",      "uk": "Рекурсія"},
    126: {"en": "Noise",          "uk": "Шум"},
    127: {"en": "Existence",      "uk": "Буття"},
    128: {"en": "Propagation",    "uk": "Поширення"},
}


def draw(n=4, pool=None):
    """Витягнути n унікальних символів."""
    available = list(pool or SYMBOLS.keys())
    chosen = []
    for _ in range(n):
        idx = secrets.randbelow(len(available))
        chosen.append(available.pop(idx))
    return {k: SYMBOLS[k] for k in chosen}


def draw_deep(n=4, detail=4):
    """Ієрархічний розклад: n головних + detail деталей для кожного."""
    main = draw(n)
    result = {}
    for key, symbol in main.items():
        details = draw(detail, pool=[k for k in SYMBOLS if k != key])
        result[key] = {"symbol": symbol, "details": details}
    return result


def format_symbol(key, symbol):
    return f"  [{key:3d}] {symbol['en']} / {symbol['uk']}"


def print_draw(n=4, deep=False):
    if deep:
        result = draw_deep(n)
        print(f"\n=== GenSym: {n} головних × 4 деталі ===\n")
        for key, data in result.items():
            s = data["symbol"]
            print(f"◆ [{key:3d}] {s['en']} / {s['uk']}")
            for dk, ds in data["details"].items():
                print(f"      · [{dk:3d}] {ds['en']} / {ds['uk']}")
            print()
    else:
        result = draw(n)
        print(f"\n=== GenSym: {n} символів ===\n")
        for key, symbol in result.items():
            print(format_symbol(key, symbol))
        print()


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    deep = len(sys.argv) > 2 and sys.argv[2] == "deep"
    print_draw(n, deep)
