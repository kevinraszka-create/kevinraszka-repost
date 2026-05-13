def kviz_vesmir():
    otazky = [
        {
            "otazka": "Jaká je největší planeta ve sluneční soustavě?",
            "moznosti": ["A) Země", "B) Jupiter", "C) Mars", "D) Saturn"],
            "odpoved": "B"
        },
        {
            "otazka": "Která galaxie je nejblíže Mléčné dráze?",
            "moznosti": ["A) Andromeda", "B) Sombrero", "C) Trojúhelník", "D) Vírová"],
            "odpoved": "A"
        }
    ]
    score = 0
    for otazka in otazky:
        print(otazka["otazka"])
        for moznost in otazka["moznosti"]:
            print(moznost)
        odpoved = input("Zadejte svou odpověď (A, B, C, D): ").upper()
        if odpoved == otazka["odpoved"]:
            print("Správně!")
            score += 1
        else:
            print("Špatně! Správná odpověď je:", otazka["odpoved"])
        print()