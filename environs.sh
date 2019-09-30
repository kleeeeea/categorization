#!/usr/bin/env bash

export RAW_TRAIN=/home/klee/data/concept_medical/papers_text_maxPapers10000.0.txt
export MODEL=concept_medical_10000
export CATEGORY_SEED_CONCEPTS=./taxonomy_medical.txt

source conf.d/autoPhrase.sh



mkdir -p ../AutoPhrase/$MODEL
mkdir -p tmp

export SEGGED_TEXT=../AutoPhrase/$MODEL/segmentation.txt
export SEGGED_TEXT_phrase_as_word=$SEGGED_TEXT.phrase_as_word
export SEGGED_TEXT_phrase_as_word_retain_alphanumeric=$SEGGED_TEXT_phrase_as_word.retain_alphanumeric
export SEGGED_TEXT_WORDVEC=../AutoPhrase/$MODEL/wordvec
export SEGGED_TEXT_TFIDF=../AutoPhrase/$MODEL/tfidf
export SEGGED_TEXT_CATEGORIZATION=$SEGGED_TEXT.categorization

