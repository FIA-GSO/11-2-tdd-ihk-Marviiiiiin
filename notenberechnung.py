def notenberechnung(punkte: int, gesamt: int) -> float:
    if not isinstance(punkte, int) or not isinstance(gesamt, int):
        raise TypeError("Punkte müssen eine Ganzzahl sein")
    else:
        if punkte < 0:
            raise ValueError("Punkte dürfen nicht negativ sein")
        if gesamt < 6:
            raise ValueError("Gesamt muss mindestens 6 sein")
        if punkte > gesamt:
            raise ValueError("Punkte dürfen nicht größer als Gesamtpunktzahl sein")
        return punkte / gesamt * 100