def notenausgabe(prozent: int) -> str:
    if not isinstance(prozent, int):
        raise TypeError("Prozent muss eine Gleitkommazahl sein")
    else:
        if prozent < 0 or prozent > 100:
            raise ValueError("Prozent muss zwischen 0 und 100 liegen")
        if prozent < 30:
            return "ungenügend"
        if prozent < 50:
            return "mangelhaft"
        if prozent < 67:
            return "ausreichend"
        if prozent < 81:
            return "befriedigend"
        if prozent < 92:
            return "gut"
        return "sehr gut"