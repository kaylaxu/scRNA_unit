# scRNA_unit
Unit test files and scripts for scRNA mongodb insert

Documents will be inserted in to a database named 'scRNA' and collection named 'UNIT'.

Test file unit_1000.csv contains counts for 1,000 ATAC loci across 4,863 PFPP cells (9.4 MB).

To run:
1. Create a python environment with pymongo python package.
2. Run ``` python unit_insert.py unit_100.csv ``` to insert documents split by both mutation status (e.g. isoLRRK2, GBA_N370S, etc.) and cell type (ie. PFPP)
3. Run ``` python byMut_insert.py unit_100.csv ``` to insert documents split by only mutation status (e.g. isoLRRK2, GBA_N370S, etc.) 
