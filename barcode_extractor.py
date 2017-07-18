#!/usr/bin/python

from Bio.SeqIO.QualityIO import FastqGeneralIterator
import gzip

input_fastq = "SAM1-12a_S3_L001_R1_001.fastq.gz"
output_fastq = "SAM1-12a_S3_L001_R1_001.no_barcodes.fastq.gz"
index_fastq = "SAM1-12a_S3_L001_R1_001.barcodes.fastq.gz"
barcode_length = 8

with gzip.open(input_fastq, "rt") as handle, gzip.open(output_fastq, "wt") as data_out, gzip.open(index_fastq, "wt") as index_out:
    for (title, sequence, quality) in FastqGeneralIterator(handle):
        data_out.write("{}\n{}\n+\n{}\n\n".format(title, sequence[8:], quality[8:]))
        index_out.write("{}\n{}\n+\n{}\n\n".format(title, sequence[:8], quality[:8]))
