# define a dictionary of 20 valid AA characters and their masses
d_AA_mass = {"A": 71.03711360, "C": 103.0091854, "D": 115.0269428, "E": 129.0425928, "F": 147.0684136, "G": 57.02146360,
             "H": 137.0589116, "I": 113.0840636, "K": 128.0949626, "L": 113.0840636, "M": 131.0404854, "N": 114.0429272,
             "P": 97.05276360, "Q": 128.0585772, "R": 156.1011106, "S": 87.03202820, "T": 101.0476782, "V": 99.06841360,
             "W": 186.0793126, "Y": 163.0633282};
# mass of water
d_AA_mass["h2o"] = 18.010564684;

# protein data
list_of_protein_dicts = [{'seq': 'ACACIMED', 'ch': 2},
                         {'seq': 'ELEMYRATNE', 'ch': 1},
                         {'seq': 'wapwop', 'ch': 3},
                         {'seq': 'zeittsieg', 'ch': 2},
                         {'seq': 'DESFBIRC', 'ch': 1},
                         {'seq': 'altaatsiv', 'ch': 3},
                         {'seq': 'MEINWOHC', 'ch': 2}];

for protein in list_of_protein_dicts:
    # grab sequence & charge from dictionary
    AA_seq = protein["seq"];
    charge = protein["ch"];
    # base mass is mass of h2o
    mass = d_AA_mass["h2o"];
    valid = True;
    # make uppercase to align with dictionary
    for AA_value in AA_seq.upper():
        # add mass of AAs while checking validity
        if AA_value in d_AA_mass:
            mass += d_AA_mass[AA_value];
        else:
            print(AA_seq + ": Not a valid AA (" + AA_value + ")");
            valid = False;
            break;
    # calculate m/z and print if valid
    if valid:
        ratio = mass / charge;
        print(AA_seq, ":", ratio);