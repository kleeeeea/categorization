#!/usr/bin/env bash


export RAW_TRAIN=$(realpath $( dirname "${BASH_SOURCE[0]}" ))/input/signal_processing_sample_input.txt
export MODEL=concept_medical_10000
export CATEGORY_SEED_CONCEPTS=$(realpath $( dirname "${BASH_SOURCE[0]}" ))/input/taxonomy_signal_processing_test.txt

source conf.d/autoPhrase.sh

mkdir -p ../AutoPhrase/$MODEL
mkdir -p tmp

export SEGGED_TEXT=../AutoPhrase/$MODEL/segmentation.txt
export SEGGED_TEXT_phrase_as_word=$SEGGED_TEXT.phrase_as_word
export SEGGED_TEXT_phrase_as_word_retain_alphanumeric=$SEGGED_TEXT_phrase_as_word.retain_alphanumeric
export SEGGED_TEXT_WORDVEC=../AutoPhrase/$MODEL/wordvec
export SEGGED_TEXT_TFIDF=../AutoPhrase/$MODEL/tfidf
export SEGGED_TEXT_CATEGORIZATION=$SEGGED_TEXT.categorization

