from Bio import SeqIO
import json

# from Bio.SeqIO import parse  # you won't need that, you imported the whole SeqIO package above

my_dict = {}

with open("/Users/sjtrauber/Documents/WPI/DataVis/assignments/final/datavis-final/data/FEY_2_All7_final.fasta", 'r') as new_fasta:
    for x in SeqIO.parse(new_fasta, 'fasta'):
        # dataset = x.id
        # sequence = x.seq # you won't need that, if the variables go out of scope and aren't used
        my_dict = {
            "dataset": x.id,
            "sequence": str(x.seq) # string cast to SeqRecord seq object
        }

my_json = json.dumps(my_dict)  # maybe use json.dump directly to a file (use pretty print option, eg. indent=2)?

with open('FEY_2_All7_final.json', 'w') as f: json.dump(my_dict, f, indent=2)