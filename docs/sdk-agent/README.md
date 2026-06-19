# ŠDK Agent

**ŠDK Agent** je návrh asistenta pre školského digitálneho koordinátora. Jeho cieľom je pomáhať pri plánovaní, dokumentovaní, komunikácii, školeniach, digitálnej stratégii školy, podpore učiteľov a vyhodnocovaní digitálnej transformácie.

Tento priečinok obsahuje základný návrh agenta pripravený pre ďalší vývoj v GitHube alebo pre použitie ako inštrukcie v ChatGPT Custom GPT.

## Najlepšia počiatočná verzia

Najvhodnejšie je začať ako **promptovo-dokumentačný agent**, nie ako plná aplikácia.

Dôvod:

- rýchlo sa dá použiť priamo v ChatGPT,
- netreba hneď riešiť backend, databázu ani prihlasovanie,
- bezpečnejšie sa nastaví rozsah práce a GDPR pravidlá,
- dá sa postupne rozšíriť na webovú alebo internú školskú aplikáciu.

## Hlavné úlohy agenta

1. Tvorba ročného a mesačného plánu činností ŠDK.
2. Pomoc pri digitálnej stratégii školy a akčnom pláne.
3. Návrh školení pre učiteľov, vedenie školy a predmetové tímy.
4. Príprava správ, zápisov, vyhodnotení a argumentačných podkladov.
5. Podpora zavádzania Microsoft 365, Teams, SharePoint, Forms, OneNote, AI a digitálnych nástrojov.
6. Pomoc pri zmene školy cez manažérsky rámec: vízia, naliehavosť, tím, komunikácia, malé víťazstvá, vyhodnotenie.
7. Vysvetľovanie pozície ŠDK tak, aby bolo jasné, že ŠDK nie je iba technik, ale koordinátor digitálnej transformácie.

## Odporúčaná štruktúra

```text
docs/sdk-agent/
├── README.md
├── agent-instructions.md
├── knowledge-map.md
├── mvp-roadmap.md
└── security-gdpr.md
```

## Použitie v ChatGPT

Obsah súboru `agent-instructions.md` sa dá vložiť ako základné inštrukcie vlastného GPT agenta. Ostatné súbory slúžia ako znalostná mapa, plán rozvoja a bezpečnostné mantinely.

## Ďalší krok

Po schválení MVP je vhodné doplniť:

- šablóny výstupov,
- mesačné reporty,
- plán školení,
- digitálnu stratégiu školy,
- databázu odporúčaných promptov,
- interný systém úloh pre ŠDK.
