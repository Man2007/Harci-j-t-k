function displayName() {
    var name = document.getElementById('nameInput').value;
    document.getElementById('nameDisplay').textContent = name;
}


// Függvény a dobásokhoz
function rollDice(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Kasztok definiálása
const classes = {
    "harcos": {
        "Erő": () => rollDice(1, 10) + 10,
        "Gyorsaság": () => rollDice(2, 6) + 8,
        "Ügyesség": () => rollDice(3, 6),
        "fegyverTípusok": ["Pallos", "Buzogány"]
    },
    "tolvaj": {
        "Erő": () => rollDice(3, 6),
        "Gyorsaság": () => rollDice(1, 10) + 10,
        "Ügyesség": () => rollDice(2, 6) + 8,
        "fegyverTípusok": ["Tőr", "Kard"]
    },
    "pap": {
        "Erő": () => rollDice(2, 6) + 8,
        "Gyorsaság": () => rollDice(3, 6),
        "Ügyesség": () => rollDice(1, 10) + 10,
        "fegyverTípusok": ["Bot"]
    }
};

// Fegyverek definiálása
const weapons = {
    "Kard": { "Sebzés": () => rollDice(1, 6) + 3, "Sebesség": 6, "Védekezés": 8, "Támadás": 6 },
    "Tőr": { "Sebzés": () => rollDice(1, 6), "Sebesség": 10, "Védekezés": 3, "Támadás": 10 },
    "Bot": { "Sebzés": () => rollDice(1, 4), "Sebesség": 8, "Védekezés": 10, "Támadás": 8 },
    "Pallos": { "Sebzés": () => rollDice(2, 6), "Sebesség": 1, "Védekezés": 1, "Támadás": 4 },
    "Buzogány": { "Sebzés": () => rollDice(2, 4) + 2, "Sebesség": 4, "Védekezés": 5, "Támadás": 4 }
};

// Kasztok és fegyverek harchoz használt értékeinek kiszámítása
Object.keys(classes).forEach(className => {
    Object.keys(weapons).forEach(weaponName => {
        const attackValue = classes[className]["Erő"]() - 10 + weapons[weaponName]["Támadás"];
        const defenseValue = classes[className]["Ügyesség"]() - 10 + weapons[weaponName]["Védekezés"];
        weapons[weaponName][className] = { "Attack": attackValue, "Defense": defenseValue };
    });
});

// Függvény a harc folyamatának végrehajtásához
function fight(character1, character2) {
    let round = 1;
    let winner = null;

    while (character1["Életerő"] > 0 && character2["Életerő"] > 0) {
        console.log(`--- Kör ${round} ---`);
        console.log(`${character1["Név"]} életereje: ${character1["Életerő"]}`);
        console.log(`${character2["Név"]} életereje: ${character2["Életerő"]}`);

        const initiative1 = rollDice(1, 10) + character1["Kezdeményezés"];
        const initiative2 = rollDice(1, 10) + character2["Kezdeményezés"];

        if (initiative1 > initiative2) {
            console.log(`${character1["Név"]} cselekszik először.`);
            performAction(character1, character2);
            if (character2["Életerő"] <= 0) {
                winner = character1;
                break;
            }
            console.log(`${character2["Név"]} cselekszik.`);
            performAction(character2, character1);
            if (character1["Életerő"] <= 0) {
                winner = character2;
                break;
            }
        } else {
            console.log(`${character2["Név"]} cselekszik először.`);
            performAction(character2, character1);
            if (character1["Életerő"] <= 0) {
                winner = character2;
                break;
            }
            console.log(`${character1["Név"]} cselekszik.`);
            performAction(character1, character2);
            if (character2["Életerő"] <= 0) {
                winner = character1;
                break;
            }
        }

        round++;
    }

    if (winner) {
        console.log(`A harc győztese: ${winner["Név"]}`);
    } else {
        console.log("A harc döntetlen lett.");
    }
}

// Függvény a karakter cselekedetének végrehajtásához
function performAction(attacker, defender) {
    const action = prompt(`${attacker["Név"]} cselekedik (Támad/Védekezik/Képesség)?`).toLowerCase();
    switch (action) {
        case "támad":
            attack(attacker, defender);
            break;
        case "védekezik":
            console.log(`${attacker["Név"]} védekezik.`);
            break;
        case "képesség":
            if (!attacker["KépességUsed"]) {
                useAbility(attacker, defender);
            } else {
                console.log("A képesség már használt.");
                performAction(attacker, defender);
            }
            break;
        default:
            console.log("Nem megfelelő művelet.");
            performAction(attacker, defender);
            break;
    }
}

// Függvény a támadás végrehajtásához
function attack(attacker, defender) {
    const attackRoll = rollDice(1, 10) + attacker["Támadás"];
    const defenseRoll = rollDice(1, 10) + defender["Védekezés"];
}
    if (attackRoll > defenseRoll) {
        const damage = weapons["attacker"];
}
