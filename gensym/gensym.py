"""
GenSym — Fundamental Units of Sense
136 symbols for generative fiction.

Usage:
    python3 gensym.py          # 4 main symbols
    python3 gensym.py 7        # 7 main symbols
    python3 gensym.py 4 deep   # 4 main + 4 details for each
"""

import secrets
import sys

SYMBOLS = {
    # 1. Forces
    1:   "Transformation",
    2:   "Stasis",
    3:   "Dissolution",
    4:   "Birth",
    5:   "Void",
    6:   "Emergence",
    7:   "Tension",
    8:   "Release",
    # 2. Space & Movement
    9:   "Ascent",
    10:  "Descent",
    11:  "Crossing",
    12:  "Threshold",
    13:  "Center",
    14:  "Boundary",
    15:  "Exile",
    16:  "Return",
    # 3. States
    17:  "Awakening",
    18:  "Sleep",
    19:  "Blindness",
    20:  "Insight",
    21:  "Memory",
    22:  "Oblivion",
    23:  "Solitude",
    24:  "Connection",
    # 4. Actions
    25:  "Search",
    26:  "Flight",
    27:  "Creation",
    28:  "Destruction",
    29:  "Sacrifice",
    30:  "Revelation",
    31:  "Choice",
    32:  "Consequence",
    # 5. Relations
    33:  "Union",
    34:  "Separation",
    35:  "Betrayal",
    36:  "Loyalty",
    37:  "Power",
    38:  "Submission",
    39:  "Protection",
    40:  "Dependence",
    # 6. Archetypes
    41:  "Seeker",
    42:  "Guardian",
    43:  "Trickster",
    44:  "Shadow",
    45:  "Child",
    46:  "Sage",
    47:  "Destroyer",
    48:  "Builder",
    # 7. Elements
    49:  "Fire",
    50:  "Water",
    51:  "Earth",
    52:  "Air",
    53:  "Time",
    54:  "Light",
    55:  "Darkness",
    56:  "Abyss",
    # 8. Psychology
    57:  "Doubt",
    58:  "Confidence",
    59:  "Guilt",
    60:  "Forgiveness",
    61:  "Wonder",
    62:  "Fear",
    63:  "Longing",
    64:  "Rage",
    # 9. Cognition
    65:  "Discovery",
    66:  "Deception",
    67:  "Intuition",
    68:  "Logic",
    69:  "Mystery",
    70:  "Disclosure",
    71:  "Question",
    72:  "Answer",
    # 10. Temporal
    73:  "Beginning",
    74:  "End",
    75:  "Cycle",
    76:  "Moment",
    77:  "Eternity",
    78:  "Anticipation",
    79:  "Resonance",
    80:  "Foresight",
    # 11. Conflict
    81:  "Confrontation",
    82:  "Surrender",
    83:  "Death",
    84:  "Victory",
    85:  "Love",
    86:  "Entropy",
    87:  "Rebellion",
    88:  "Acceptance",
    # 12. Nature & Cosmos
    89:  "Storm",
    90:  "Silence",
    91:  "Chaos",
    92:  "Order",
    93:  "Growth",
    94:  "Consciousness",
    95:  "Will",
    96:  "Asymmetry",
    # 13. Body & Matter
    97:  "Pain",
    98:  "Healing",
    99:  "Hunger",
    100: "Flow",
    101: "Fatigue",
    102: "Strength",
    103: "Touch",
    104: "Distance",
    # 14. Social
    105: "Community",
    106: "Catalyst",
    107: "Leader",
    108: "Quantity",
    109: "Mask",
    110: "Authenticity",
    111: "Signal",
    112: "Legacy",
    # 15. Abstract
    113: "Balance",
    114: "Paradox",
    115: "Illusion",
    116: "Reality",
    117: "Symbol",
    118: "Rhythm",
    119: "Feedback",
    120: "Myth",
    # 16. Structural
    121: "Relation",
    122: "Pattern",
    123: "Polarity",
    124: "Synthesis",
    125: "Recursion",
    126: "Noise",
    127: "Existence",
    128: "Propagation",
    # 17. Form & Space
    129: "Vessel",
    130: "Path",
    131: "Shelter",
    132: "Tool",
    133: "Stage",
    134: "Archive",
    135: "Node",
    136: "Surface",
}


def draw(n=4, pool=None):
    """Draw n unique symbols."""
    available = list(pool or SYMBOLS.keys())
    chosen = []
    for _ in range(n):
        idx = secrets.randbelow(len(available))
        chosen.append(available.pop(idx))
    return {k: SYMBOLS[k] for k in chosen}


def draw_deep(n=4, detail=4):
    """Hierarchical draw: n main symbols + detail symbols for each."""
    main = draw(n)
    result = {}
    for key, symbol in main.items():
        details = draw(detail, pool=[k for k in SYMBOLS if k != key])
        result[key] = {"symbol": symbol, "details": details}
    return result


def print_draw(n=4, deep=False):
    if deep:
        result = draw_deep(n)
        print(f"\n=== GenSym: {n} main × 4 details ===\n")
        for key, data in result.items():
            print(f"◆ [{key:3d}] {data['symbol']}")
            for dk, ds in data["details"].items():
                print(f"      · [{dk:3d}] {ds}")
            print()
    else:
        result = draw(n)
        print(f"\n=== GenSym: {n} symbols ===\n")
        for key, symbol in result.items():
            print(f"  [{key:3d}] {symbol}")
        print()


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    deep = len(sys.argv) > 2 and sys.argv[2] == "deep"
    print_draw(n, deep)
