[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/06bFzJ4n)
# Domácí úkol č. 7

> **Upravujte pouze soubor `assignment_7_1.py`!**


## Harry Potter a datová analýza
Filmy s Harrym Potterem určitě všichni znáte. V tomto domácím úkolu si vyzkoušíme menší datovou analýzu na dvou 
datasetech, které byly vytvořené na základě filmů o Harrym Potterovi. Tyto dva datasety můžete najít ve složce 
`datasets`. Oba datasety se nejdříve otevřete a dobře si prohlédněte jejich strukturu.

První z nich `Characters.csv` obsahuje informace o všech postavách, které se ve všech osmi filmech objevili, a to:
* `Character ID` - unikátní identifikátor postavy,
* `Character Name` - jméno postavy,
* `Species` - druh postavy,
* `Gender` - pohlaví postavy,
* `House` - název bradavické koleje (nebo název jiné kouzelnické školy),
* `Patronus` - podoba Patronova zaklínadla,
* `Wand (Wood)` - typ dřeva hůlky,
* `Wand (Core)` - typ jádra hůlky.

Druhý dataset `Dialogue.csv` se skládá ze všech dialogů, které ve filmech zazněli, a obsahuje tyto položky:
* `Dialogue ID` - unikátní identifikátor pro jednotlivé řádky dialogů,
* `Chapter ID` - cizí klíč, který odpovídá identifikátoru v datasetu `Chapters` (není k dispozici),
* `Place ID` - cizí klíč, který odpovídá identifikátoru v datasetu `Places` (není k dispozici),
* `Character ID` - cizí klíč, který odpovídá identifikátoru v datasetu `Characters` (viz výše),
* `Dialogue` - řádek dialogu z filmového scénáře.


### Načtení datasetu
* Vytvořte funkci `load_hp_data()`, která provede načtení libovolného datasetu.
* Funkce bude mít jeden vstupní parametr typu `str` představující cestu k souboru, který má být načten.
* Funkce bude vracet načtený dataset v datové struktuře `list`, kde každý řádek datasetu bude reprezentován jedním
  vnořeným seznamem.
* Např.:
  ```
  Character ID,Character Name,Species,Gender,House,Patronus,Wand (Wood),Wand (Core)
  1,Harry Potter,Human,Male,Gryffindor,Stag,Holly,Phoenix Feather
  2,Ron Weasley,Human,Male,Gryffindor,Jack Russell Terrier,,
  3,Hermione Granger,Human,Female,Gryffindor,Otter,Vine,Dragon Heartstring
  ```
  převede na:
  ```python
  [
       ['Character ID', 'Character Name', 'Species', 'Gender', 'House', 'Patronus', 'Wand (Wood)', 'Wand (Core)'], 
       ['1', 'Harry Potter', 'Human', 'Male', 'Gryffindor', 'Stag', 'Holly', 'Phoenix Feather'], 
       ['2', 'Ron Weasley', 'Human', 'Male', 'Gryffindor', 'Jack Russell Terrier', '', ''], 
       ['3', 'Hermione Granger', 'Human', 'Female', 'Gryffindor', 'Otter', 'Vine', 'Dragon Heartstring'],
  ]
  ```


### Předzpracování datasetů
* Vytvořte funkci `create_dataset_dict()`, která předzpracuje libovolný načtený dataset do datové struktury `dict`
  se specifickou strukturou.
* Funkce bude mít jeden vstupní parametr typu `list` reprezentující načtený dataset.
* Funkce vrátí předzpracovaný dataset typu `dict`.
* Předzpracování zajistí, že každý řádek datasetu bude ve výstupním slovníku uložen pod klíčem odpovídající svému
  unikátnímu identifikátoru. Zbylé informace v řádku datasetu bude ale nutné převést na slovník a tento slovník vložit jako hodnotu 
  pod odpovídající klíč, resp. unikátní identifikátor. Budete tedy vytvářet vnořené slovníky.
* Vnořený slovník bude vypadat následovně: klíči budou textové řetězce uvedené v hlavičce datasetu tzn. v každém 
  vnořeném slovníku se budou opakovat. Hodnotami v tomto vnořeném slovníku budou odpovídající hodnoty z řádku datasetu.
* Např.
  ```python
  [
      ['Character ID', 'Character Name', 'Species', 'Gender', 'House', 'Patronus', 'Wand (Wood)', 'Wand (Core)'], 
      ['1', 'Harry Potter', 'Human', 'Male', 'Gryffindor', 'Stag', 'Holly', 'Phoenix Feather'], 
      ['2', 'Ron Weasley', 'Human', 'Male', 'Gryffindor', 'Jack Russell Terrier', '', ''], 
  ]
  ```
  předzpracuje na slovník:
  ```python
  {'1': {'Character Name': 'Harry Potter', 
        'Species': 'Human', 
        'Gender': 'Male', 
        'House': 'Gryffindor', 
        'Patronus': 'Stag', 
        'Wand (Wood)': 'Holly', 
        'Wand (Core)': 'Phoenix Feather'},
  '2': {'Character Name': 'Ron Weasley',
        'Species': 'Human', 
        'Gender': 'Male', 
        'House': 'Gryffindor', 
        'Patronus': 'Jack Russell Terrier', 
        'Wand (Wood)': '', 
        'Wand (Core)': ''},
  }
  ```


### Výpočet tabulky četností
* Vytvořte funkci `get_frequency_table()`, která zjistí, jaké hodnoty se nachází pod vybraným klíčem v datasetu, a 
  kolikrát se tyto hodnoty opakují v celém datasetu.
  Např. v datasetu `Characters` pro klíč `Wand (wood)` zjistí, z jakých druhů dřev jsou vyrobeny hůlky všech postav,
  a kolikrát se které dřevo v datasetu postav vyskytuje.
* Funkce bude mít dva vstupní parametry:
  * předzpracovaný dataset typu `dict`,
  * název klíče typu `str`, který má být prohledán.
* Funkce vrátí slovník s nalezenými výskyty, kde klíčem budou nalezené hodnoty v prohledávaném klíči (např. `"Oak"`, 
  `"Fir"` atd.), a k nim bude přiřazen nalezený počet výskytů.
* Např. pro část datasetu `Characters`
  ```python
  {'5': {'Character Name': 'Rubeus Hagrid',
         'Gender': 'Male',
         'House': 'Gryffindor',
         'Patronus': '',
         'Species': 'Half-Human/Half-Giant',
         'Wand (Core)': '',
         'Wand (Wood)': 'Oak'},
   '6': {'Character Name': 'Severus Snape',
         'Gender': 'Male',
         'House': 'Slytherin',
         'Patronus': 'Doe',
         'Species': 'Human',
         'Wand (Core)': '',
         'Wand (Wood)': ''},
   '7': {'Character Name': 'Minerva McGonagall',
         'Gender': 'Female',
         'House': 'Gryffindor',
         'Patronus': 'Cat',
         'Species': 'Human',
         'Wand (Core)': 'Dragon Heartstring',
         'Wand (Wood)': 'Fir'},
   '8': {'Character Name': 'Horace Slughorn',
         'Gender': 'Male',
         'House': 'Slytherin',
         'Patronus': '',
         'Species': 'Human',
         'Wand (Core)': 'Dragon Heartstring',
         'Wand (Wood)': 'Cedar'},
   '9': {'Character Name': 'Voldemort',
         'Gender': 'Male',
         'House': 'Slytherin',
         'Patronus': '',
         'Species': 'Human',
         'Wand (Core)': 'Phoenix Feather',
         'Wand (Wood)': 'Yew'},
   },
  ```
  a pro klíč `'Wand (Wood)'` vytvoří následující tabulku četností:
  ```python
  {'Oak': 1, '': 1, 'Fir': 1, 'Cedar': 1, 'Yew': 1}
  ```

### Nalezení nejčastějších výskytů
* Vytvořte funkci `get_most_common()`, která na základě tabulky četností vybere ty záznamy, které měly nejvyšší nalezený
  počet výskytů.
* Funkce bude mít dva vstupní parametry:
  * tabulku četností typu `dict`,
  * počet záznamů s nejvyšším výskytem, které má funkce vrátit, typu `int` s výchozí hodnotou `1`.
* Funkce vrátí požadovaný počet záznamů s nejvyšší četností uložených v seznamu, kde jsou jednotlivé záznamy uložené
  jako seznamy seřazené sestupně podle četností.
* Např. pro tuto tabulku četností
  ```python
  {'7': 130, '32': 33, '31': 36, '21': 73, '161': 1, '139': 5}
  ```
  a pro hodnotu `3` vrátí tři záznamy, u kterých byla nalezena nejvyšší četnost, tj. klíč `'7'` se 130-ti výskyty, klíč 
  `'21'` se 73 výskyty a klíč `'31'`, který má četnost 36. Nalezené záznamy se zapíší do výstupu následovně:
  ```python
  [['7', 130], ['21', 73], ['31', 36]]  
  ```


### Datová analýza
Vytvořené funkce teď použijte pro zjištění odpovědí na následující otázky:
1. Jaké je procentuální zastoupení postav v jednotlivých kolejích v Bradavicích?
2. Kterých pět postav mělo nejvíce dialogů ve všech filmech a kolik jich bylo?

**Ad `1.`:** Uvažujte pouze postavy, které studovali/studují v Bradavicích, tudíž výsledný součet procent musí dát 
dohromady 100%.

* Vytvořte funkci `main()`, kde budete provádět všechny kroky datové analýzy.
* Funkce bude mít dva vstupní parametry:
  * parametr typu `list` reprezentující načtený dataset `Characters`,
  * parametr typu `list` reprezentující načtený dataset `Dialogues`.
* Funkce bude mít dva výstupy:
  * Odpověď na otázku č. 1 bude typu `tuple`, kde procentuální zastoupení kolejí bude uvedeno v tomto pořadí: 
    Gryffindor (Nebelvír), Hufflepuff (Mrzimor), Ravenclaw (Havraspár) a Slytherin (Zmijozel).
  * Odpověď na otázku č. 2 bude typu `list`, kde prvky tohoto seznamu budou seznamy se jménem postavy a počtem dialogů.
    Prvky seznamu budou seřazeny podle počtu dialogů od nejvyššího po nejmenší.


### Dokumentační řetězce
Doplňte všechny funkce o dokumentační řetězec s popisem účelu funkce a jednotlivých vstupních a výstupních parametrů.
