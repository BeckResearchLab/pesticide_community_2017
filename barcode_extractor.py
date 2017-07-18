#!/usr/bin/python

import argparse
import gzip

from Bio.SeqIO.QualityIO import FastqGeneralIterator


parser = argparse.ArgumentParser(description='Extract and trim barcodes from a FASTQ file', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('input_fastq', help='input read fastq file')
parser.add_argument('output_fastq', help='output trimmed read fastq file')
parser.add_argument('barcode_fastq', help='output barcode fastq file')
parser.add_argument('barcode_length', help='barcode length as integer', type=int)
args = parser.parse_args()

#input_fastq = "SAM1-12a_S3_L001_R1_001.fastq.gz"
#output_fastq = "SAM1-12a_S3_L001_R1_001.no_barcodes.fastq.gz"
#index_fastq = "SAM1-12a_S3_L001_R1_001.barcodes.fastq.gz"
#barcode_length = args.barcode_length

reads_processed = 0

print("reading input reads from: %s" % args.input_fastq)
print("writing trimmed reads to: %s" % args.output_fastq)
print("writing barcode fastq to: %s" % args.barcode_fastq)
print("expected barcode length is: %d" % args.barcode_length)

with gzip.open(args.input_fastq, "rt") as handle, gzip.open(args.output_fastq, "wt") as data_out, gzip.open(args.barcode_fastq, "wt") as barcode_out:
    for (title, sequence, quality) in FastqGeneralIterator(handle):
        data_out.write("@{}\n{}\n+\n{}\n".format(title, sequence[args.barcode_length:], quality[args.barcode_length:]))
        barcode_out.write("@{}\n{}\n+\n{}\n".format(title, sequence[:args.barcode_length], quality[:args.barcode_length]))
        reads_processed += 1
        if reads_processed % 10000 == 0:
            print("processed %d reads" % reads_processed)

print("processed %d reads" % reads_processed)
