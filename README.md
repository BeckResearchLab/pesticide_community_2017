This pipeline depends on R and DADA2.

At the time of this writing, R 3.4.0 or greater must be used.  For this work, R 3.4.1 was used.

To install DADA2, these instructions were followed to install it:
* https://benjjneb.github.io/dada2/dada-installation.html

To demultiplex, you will need a biopython install.  Do this with conda:
* `conda create --name biopython biopython`
* `source activate biopython # switch to the virtual environment`
