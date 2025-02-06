import pymongo
from pymongo import MongoClient
import csv
import sys
import time

g0 = {"chr1": 1,
      "chr2": 250000000,
      "chr3":495000000,
      "chr4":695000000,
      "chr5":890000000,
      "chr6":1075000000,
      "chr7":1250000000,
      "chr8":1412000000,
      "chr9":1560000000,
      "chr10":1700000000,
      "chr11":1835000000,
      "chr12":1972000000,
      "chr13":2107000000,
      "chr14":2223000000,
      "chr15":2333000000,
      "chr16":2438000000,
      "chr17":2533000000,
      "chr18":2618000000,
      "chr19":2700000000,
      "chr20":2760000000,
      "chr21":2826000000,
      "chr22":2876000000,
      "chrX":2928000000,
      "chrY":3088000000,
      "chrM":3148000000}

client = MongoClient("mongodb://localhost:27017")
db = client["foundinpd"]
collection = db["MSCR"]

# cell type dictionary
cellTypes = {}
with open('cellID_cellType.csv') as f:
    file = csv.reader(f)
    header = True
    for line in file:
        if header:
            header = False
        else:
            cellTypes[line[0]] = line[1]

# mutation dictionary
mutations = {}
with open('sample_meta.csv') as f:
    file = csv.reader(f)
    header = True
    for line in file:
        if header:
            header = False
        else:
            mutations[line[0].split('_')[1]] = line[2]


# gene g0 dictionary
gene_g0 = {}
with open('GRCh38_GENCODE29_geneInfo.txt', 'r') as f:
    file = csv.reader(f, delimiter="\t")
    header = 0
    for line in file:
        if header < 2:
            header += 1
        else:
            if line[0] in g0:
                if line[11] not in gene_g0:
                    gene_g0[line[11]] = g0[line[0]] + int(line[1])

num = {}
cellID = ""
mutKeys = {}
count = 0
start_time = time.time()
with open(sys.argv[1]) as f:
    file = csv.reader(f)
    header = True
    for line in file:
        if header:
            cellID = line
            for i in range(1, len(cellID)):
                mutKeys[cellID[i]] = mutations[cellID[i].split('_')[1]]
                if mutKeys[cellID[i]] in num:
                    num[mutKeys[cellID[i]]] += 1
                else:
                    num[mutKeys[cellID[i]]] = 1
            header = False
        else:
            totals = {}
            if line[0] in gene_g0:
                g = gene_g0[line[0]]
                for i in range(1, len(cellID)):
                    v = int(line[i])  
                    key = mutKeys[cellID[i]]
                    if key in totals:
                        totals[key] += v
                    else:
                        totals[key] = v
                
                for key in totals:
                    insert = {"g0": g,"gene": line[0], "m":key, "t":totals[key],"n":num[key],"v": round(totals[key]/num[key], 4)}
                    #x = collection.insert_one(insert)
                    print(insert)
        count += 1
        if count % 10000 == 0:
            print("Time at " + str(count) + "th loci: %s sec" %(round(time.time() - start_time, 2)))

print("Time:  %s sec" %(round(time.time() - start_time, 2)))