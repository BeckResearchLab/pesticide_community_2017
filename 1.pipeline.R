library(dada2); packageVersion("dada2")
# expecting 1.4.0

path <- "data"
list.files(path)
# expect a list of files in the data directory

# Sort ensures forward/reverse reads are in same order
fnFs <- sort(list.files(path, pattern="_R1_001.no_barcodes"))
fnRs <- sort(list.files(path, pattern="_R2_001"))
sample.names <- sapply(strsplit(fnFs, "_"), `[`, 7)
print(sapply(strsplit(sample.names, ".", fixed = TRUE), `[`, 1))
# Specify the full path to the fnFs and fnRs
fnFs <- file.path(path, fnFs)
fnRs <- file.path(path, fnRs)

