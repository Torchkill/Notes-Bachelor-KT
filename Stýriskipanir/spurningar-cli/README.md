# Styriskipanir spurningar cli

Hetta er eitt python program man fær avprøva sína vidan við.

hendan appin byggur uppá spurningar frá tveimum dokumentum
[royndarset](royndarset.pdf) og [Spurningar-úr-Stýriskipanir-bókini](Spurningar-úr-Stýriskipanir-bókini.pdf)

## Koyr programi

Fyri koyra programi við at skriva:

Opna terminalin í `spurningar-cli` mappuni

```bash
cd Stýriskipanir/spurningar-cli
```

og koyr python programmi

```bash
python quiz.py
```

## Leggja spurningar afturat

Um ein hevur hug at leggja spurningar afturat, so skal ein gera eina json fílu í `questions` mappuni.
json fílan skal hava hetta skapið:

```json
[
    {
        "question": "Textur til spurning",
        "options": ["Option 0", "Option 2"],
        "answer": 0 // correct Option index
    }
]
```

dømi:

```json
[
    {
        "question": "System call interface is the boundary between user programs and operating system services.",
        "options": ["Yes", "No"],
        "answer": 0
    },
    ...
]
```
