import pytest
import assignment_7_1 as hw


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ('load_hp_data', True),
        ('create_dataset_dict', True),
        ('get_frequency_table', True),
        ('get_most_common', True),
        ('main', True),
    ]
)
def test_attributes(string, expected):
    assert hasattr(hw, string)


@pytest.mark.parametrize(
    ("file_name", "idx_line", "expected_dataset"),
    [
        ("datasets/Characters.csv", 9, ['9', 'Voldemort', 'Human', 'Male', 'Slytherin', '', 'Yew', 'Phoenix Feather']),
        ("datasets/Characters.csv", 15, ['15', 'Dolores Umbridge', 'Human', 'Female', 'Slytherin', 'Cat', 'Birch', 'Dragon Heartstring']),
        ("datasets/Dialogue.csv", 54, ['54', '3', '8', '21', "There's no such thing as magic!"]),
        ("datasets/Dialogue.csv", 300, ['300', '14', '61', '2', 'That was bloody brilliant.']),
    ]
)
def test_load_hp_data(file_name, idx_line, expected_dataset):
    dataset = hw.load_hp_data(file_name)
    assert isinstance(dataset, list)
    if file_name == "datasets/Characters.csv":
        assert len(dataset) == 167
    else:
        assert len(dataset) == 7445
    assert dataset[idx_line] == expected_dataset


@pytest.mark.parametrize(
    ("dataset", "expected_data"),
    [
        (
            [
                ['Character ID', 'Character Name', 'Species', 'Gender', 'House', 'Patronus', 'Wand (Wood)', 'Wand (Core)'],
                ['1', 'Harry Potter', 'Human', 'Male', 'Gryffindor', 'Stag', 'Holly', 'Phoenix Feather'],
                ['2', 'Ron Weasley', 'Human', 'Male', 'Gryffindor', 'Jack Russell Terrier', '', ''],
            ],
            {'1': {'Character Name': 'Harry Potter',
                   'Gender': 'Male',
                   'House': 'Gryffindor',
                   'Patronus': 'Stag',
                   'Species': 'Human',
                   'Wand (Core)': 'Phoenix Feather',
                   'Wand (Wood)': 'Holly'},
             '2': {'Character Name': 'Ron Weasley',
                   'Gender': 'Male',
                   'House': 'Gryffindor',
                   'Patronus': 'Jack Russell Terrier',
                   'Species': 'Human',
                   'Wand (Core)': '',
                   'Wand (Wood)': ''},
             },
        ),
        (
            [
                ['Character ID', 'Character Name', 'Species', 'Gender', 'House', 'Patronus', 'Wand (Wood)', 'Wand (Core)'],
                ['5', 'Rubeus Hagrid', 'Half-Human/Half-Giant', 'Male', 'Gryffindor', '', 'Oak', ''],
                ['6', 'Severus Snape', 'Human', 'Male', 'Slytherin', 'Doe', '', ''],
                ['7', 'Minerva McGonagall', 'Human', 'Female', 'Gryffindor', 'Cat', 'Fir', 'Dragon Heartstring'],
                ['8', 'Horace Slughorn', 'Human', 'Male', 'Slytherin', '', 'Cedar', 'Dragon Heartstring'],
                ['9', 'Voldemort', 'Human', 'Male', 'Slytherin', '', 'Yew', 'Phoenix Feather'],
            ],
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
        ),
        (
            [
                ['Dialogue ID', 'Chapter ID', 'Place ID', 'Character ID', 'Dialogue'],
                ['1', '1', '8', '4', 'I should have known that you would be here...Professor McGonagall.'],
                ['2', '1', '8', '7', 'Good evening, Professor Dumbledore. Are the rumours true, Albus?'],
                ['3', '1', '8', '4', "I'm afraid so, Professor. The good, and the bad."],
            ],
            {'1': {'Chapter ID': '1',
                   'Character ID': '4',
                   'Dialogue': 'I should have known that you would be here...Professor McGonagall.',
                   'Place ID': '8'},
             '2': {'Chapter ID': '1',
                   'Character ID': '7',
                   'Dialogue': 'Good evening, Professor Dumbledore. Are the rumours true, Albus?',
                   'Place ID': '8'},
             '3': {'Chapter ID': '1',
                   'Character ID': '4',
                   'Dialogue': "I'm afraid so, Professor. The good, and the bad.",
                   'Place ID': '8'},
             },
        ),
        (
            [
                ['Dialogue ID', 'Chapter ID', 'Place ID', 'Character ID', 'Dialogue'],
                ['150', '6', '2', '30', 'Vault 687. Lamp, please.  Key please.'],
                ['151', '6', '2', '5', "Didn't think your mum and dad would leave you with nothing now, did ya?"],
                ['152', '6', '2', '30', 'Vault 713.'],
                ['153', '6', '2', '1', "What's in there, Hagrid?"],
                ['154', '6', '2', '5', "Can't tell you, Harry. It's Hogwarts business. Very secret."],
            ],
            {'150': {'Chapter ID': '6',
                     'Character ID': '30',
                     'Dialogue': 'Vault 687. Lamp, please.  Key please.',
                     'Place ID': '2'},
             '151': {'Chapter ID': '6',
                     'Character ID': '5',
                     'Dialogue': "Didn't think your mum and dad would leave you with nothing now, did ya?",
                     'Place ID': '2'},
             '152': {'Chapter ID': '6',
                     'Character ID': '30',
                     'Dialogue': 'Vault 713.',
                     'Place ID': '2'},
             '153': {'Chapter ID': '6',
                     'Character ID': '1',
                     'Dialogue': "What's in there, Hagrid?",
                     'Place ID': '2'},
             '154': {'Chapter ID': '6',
                     'Character ID': '5',
                     'Dialogue': "Can't tell you, Harry. It's Hogwarts business. Very secret.",
                     'Place ID': '2'}
             },
        ),
    ]
)
def test_create_dataset_dict(dataset, expected_data):
    assert hw.create_dataset_dict(dataset) == expected_data


@pytest.mark.parametrize(
    ("dataset", "field", "expected_table"),
    [
        (
            {'1': {'Character Name': 'Harry Potter',
                   'Gender': 'Male',
                   'House': 'Gryffindor',
                   'Patronus': 'Stag',
                   'Species': 'Human',
                   'Wand (Core)': 'Phoenix Feather',
                   'Wand (Wood)': 'Holly'},
             '2': {'Character Name': 'Ron Weasley',
                   'Gender': 'Male',
                   'House': 'Gryffindor',
                   'Patronus': 'Jack Russell Terrier',
                   'Species': 'Human',
                   'Wand (Core)': '',
                   'Wand (Wood)': ''},
             },
            "Patronus",
            {'Jack Russell Terrier': 1, 'Stag': 1},
        ),
        (
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
            "Species",
            {'Half-Human/Half-Giant': 1, 'Human': 4},
        ),
(
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
            "House",
            {'Gryffindor': 2, 'Slytherin': 3},
        ),
        (
            {'1': {'Chapter ID': '1',
                   'Character ID': '4',
                   'Dialogue': 'I should have known that you would be here...Professor McGonagall.',
                   'Place ID': '8'},
             '2': {'Chapter ID': '1',
                   'Character ID': '7',
                   'Dialogue': 'Good evening, Professor Dumbledore. Are the rumours true, Albus?',
                   'Place ID': '8'},
             '3': {'Chapter ID': '1',
                   'Character ID': '4',
                   'Dialogue': "I'm afraid so, Professor. The good, and the bad.",
                   'Place ID': '8'},
             },
            "Character ID",
            {'4': 2, '7': 1},
        ),
        (
            {'150': {'Chapter ID': '6',
                     'Character ID': '30',
                     'Dialogue': 'Vault 687. Lamp, please.  Key please.',
                     'Place ID': '2'},
             '151': {'Chapter ID': '6',
                     'Character ID': '5',
                     'Dialogue': "Didn't think your mum and dad would leave you with nothing now, did ya?",
                     'Place ID': '2'},
             '152': {'Chapter ID': '6',
                     'Character ID': '30',
                     'Dialogue': 'Vault 713.',
                     'Place ID': '2'},
             '153': {'Chapter ID': '6',
                     'Character ID': '1',
                     'Dialogue': "What's in there, Hagrid?",
                     'Place ID': '2'},
             '154': {'Chapter ID': '6',
                     'Character ID': '5',
                     'Dialogue': "Can't tell you, Harry. It's Hogwarts business. Very secret.",
                     'Place ID': '2'}
             },
            "Character ID",
            {'1': 1, '30': 2, '5': 2},
        ),
    ]
)
def test_get_frequency_table(dataset, field, expected_table):
    assert hw.get_frequency_table(dataset, field) == expected_table


@pytest.mark.parametrize(
    ("datatable", "k", "expected_commons"),
    [
        (
            {'7': 130, '32': 33, '31': 36, '21': 73, '161': 1, '139': 5, '92': 5, '132': 7, '41': 17, '138': 5,
             '130': 8, '30': 36, '43': 16, '149': 2},
            5,
            [['7', 130], ['21', 73], ['31', 36], ['30', 36], ['32', 33]],
        ),
        (
            {'7': 130, '32': 33, '31': 36, '21': 73, '161': 1, '139': 5, '92': 5, '132': 7, '41': 17, '138': 5,
             '130': 8, '30': 36, '43': 16, '149': 2},
            3,
            [['7', 130], ['21', 73], ['31', 36]],
        ),
        (
            {'Phoenix Feather': 3, '': 148, 'Dragon Heartstring': 9, 'Thestral Tail Hair': 1, 'Unicorn Hair': 5},
            2,
            [['', 148], ['Dragon Heartstring', 9]],
        ),
    ]
)
def test_get_most_common(datatable, k, expected_commons):
    assert hw.get_most_common(datatable, k) == expected_commons


@pytest.mark.parametrize(
    ("datatable", "expected_commons"),
    [
        (
            {'7': 130, '32': 33, '31': 36, '21': 73, '161': 1, '139': 5, '92': 5, '132': 7, '41': 17, '138': 5,
             '130': 8, '30': 36, '43': 16, '149': 2},
            [['7', 130]],
        ),
        (
            {'7': 130, '32': 33, '31': 36, '21': 73, '161': 1, '139': 5, '92': 5, '132': 7, '41': 17, '138': 5,
             '130': 8, '30': 36, '43': 16, '149': 2},
            [['7', 130]],
        ),
        (
            {'Phoenix Feather': 3, '': 148, 'Dragon Heartstring': 9, 'Thestral Tail Hair': 1, 'Unicorn Hair': 5},
            [['', 148]],
        ),
    ]
)
def test_get_most_common2(datatable, expected_commons):
    assert hw.get_most_common(datatable) == expected_commons


@pytest.mark.parametrize(
    ("char_start", "char_stop", "dia_start", "dia_stop", "expected_houses", "expected_talks"),
    [
        (
            1,
            167,
            1,
            7444,
            (43.66, 11.27, 16.9, 28.17),
            [['Harry Potter', 1922], ['Ron Weasley', 865], ['Hermione Granger', 848], ['Albus Dumbledore', 474], ['Rubeus Hagrid', 228]],
        ),
        (
            1,
            100,
            1,
            4000,
            (50.0, 6.9, 15.52, 27.59),
            [['Harry Potter', 1019], ['Ron Weasley', 490], ['Hermione Granger', 411], ['Albus Dumbledore', 184], ['Rubeus Hagrid', 171]],
        ),
        (
            1,
            50,
            5000,
            7444,
            (58.33, 2.78, 16.67, 22.22),
            [['Harry Potter', 674], ['Hermione Granger', 368], ['Ron Weasley', 315], ['Albus Dumbledore', 139], ['Horace Slughorn', 97]],
        ),
    ]
)
def test_main(char_start, char_stop, dia_start, dia_stop, expected_houses, expected_talks):
    characters = hw.load_hp_data("datasets/Characters.csv")
    new_characters = [characters[0]]
    new_characters.extend(characters[char_start:char_stop])

    dialogues = hw.load_hp_data("datasets/Dialogue.csv")
    new_dialogues = [dialogues[0]]
    new_dialogues.extend(dialogues[dia_start:dia_stop])

    houses_stats, dialogues_stats = hw.main(new_characters, new_dialogues)
    houses_stats = tuple([round(stat, 2) for stat in houses_stats])
    assert houses_stats == expected_houses
    assert dialogues_stats == expected_talks


def test_docstring():
    assert hw.main.__doc__
    assert hw.load_hp_data.__doc__
    assert hw.create_dataset_dict.__doc__
    assert hw.get_frequency_table.__doc__
    assert hw.get_most_common.__doc__
