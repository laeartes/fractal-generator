# FRAKTALO GENERATORIUS – CLI versija

Šits daiktas leidžia tau generuoti keistus, gal kartais ir gražius fraktalus, naudojant paprastus parametrus.
Visa tai per CMD/PowerShell or whatever floats your boat

## Kaip naudoti .exe:
    atsiradai per file exploreri direktorija kur yra fractal.ex
    ir tiesiog terminale paleisk taip:
        fractal.exe --vertices 5 --points 1000000 --factor 0.5 --factor-seed 2 --colormap plasma --output mano_fraktalas.png

### Galimi argumentai:
--vertices     /  -v    → kiek viršūnių turi daugiakampis (nuo 3 iki ~10-12)
--points       /  -p    → kiek taškų generuot (kuo daugiau – tuo gražesnis, bet ilgiau veikia)
--jump         /  -j    → kiek "judama" link viršūnių (0.5 duoda klasikinį sierpinskio trikampį)
--seed         /  -s    → režimas kaip dinamiškai keist tą "judėjimo" faktorių (nuo 0 iki 5) VEIKIA TIK SU SALIA PARASYTU -d. KITAIP KONSTANTA JUMPAS
--cmap         /  -c    → matplotlib spalvų schema (pvz.: plasma, viridis, turbo, rainbow...)
--output       /  -o    → kelias kur išsaugoti paveikslėlį (.png)
### Pvz:
    fractal.exe --vertices 3 --points 1500000 --jump 0.5 --dynamic 0 --cmap viridis --output sierpinskis.png

Jei nori visiško randomo, gali tiesiog pridėt -r gale:

    fractal.exe -r

Tada viskas bus random: viršūnės, spalvos, taškai, faktoriai, viskas.

## Reikalavimai

NĖRA! Šita versija jau yra .exe – tau nereikia turėti įdiegto pitono ar kažkokių priklausomybių.
Tiesiog paspaudi ir veikia.

Sukūrė laeartes