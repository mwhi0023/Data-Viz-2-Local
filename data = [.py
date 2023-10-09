data = [
    {"Group": "Taliban", "Armed Assault": 17788, "Assassination": 1473, "Bombing/Explosion": 14597, "Facility/Infrastructure Attack": 438, "Hijacking": 41, "Hostage Taking (Barricade Incident)": 319, "Hostage Taking (Kidnapping)": 4086, "Unarmed Assault": 32, "Unknown": 15344},
    {"Group": "Islamic State of Iraq and the Levant (ISIL)", "Armed Assault": 3959, "Assassination": 316, "Bombing/Explosion": 21421, "Facility/Infrastructure Attack": 158, "Hijacking": 4, "Hostage Taking (Barricade Incident)": 519, "Hostage Taking (Kidnapping)": 10550, "Unarmed Assault": None, "Unknown": 6425},
    {"Group": "Boko Haram", "Armed Assault": 13543, "Assassination": 238, "Bombing/Explosion": 6929, "Facility/Infrastructure Attack": 316, "Hijacking": 26, "Hostage Taking (Barricade Incident)": 176, "Hostage Taking (Kidnapping)": 2346, "Unarmed Assault": None, "Unknown": 1954},
    {"Group": "Al-Shabaab", "Armed Assault": 3356, "Assassination": 750, "Bombing/Explosion": 5382, "Facility/Infrastructure Attack": 46, "Hijacking": 18, "Hostage Taking (Barricade Incident)": 395, "Hostage Taking (Kidnapping)": 1013, "Unarmed Assault": 34, "Unknown": 1283}
]

output = []

for row in data:
    group = row["Group"]
    for attack_type, count in row.items():
        if attack_type != "Group" and count is not None:
            entry = {"Group": group, "AttackType": attack_type, "Count": count}
            output.append(entry)

import json
json_output = json.dumps(output, indent=2)
print(json_output)