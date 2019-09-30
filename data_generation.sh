#!/usr/bin/env bash

DATA_DIR=/home/klee/data/concept_medical
cd $DATA_DIR
cat ml_and_anesthesia.txt >> papers_text_maxPapers10000.0.txt
cat dl_and_anesthesia.txt >> papers_text_maxPapers10000.0.txt