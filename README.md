# scRNA_unit
Unit test files and scripts for multiome scRNA mongodb insert

Documents will be inserted in to a database named 'foundinpd' and collection named 'MRNA'.

Test file unit_100.csv contains counts for 100 genes across all cells. 

To run:
1. Create a python environment with pymongo python package.
2. Run ``` python unit_insert.py unit_100.csv ``` to insert documents split by both mutation status (e.g. isoLRRK2, GBA_N370S, etc.) and cell type (ie. PFPP)
3. Run ``` python byMut_insert.py unit_100.csv ``` to insert documents split by only mutation status (e.g. isoLRRK2, GBA_N370S, etc.) 
