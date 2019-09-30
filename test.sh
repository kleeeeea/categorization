#!/usr/bin/env bash

source ./environs.sh


python ./conceptGraphPPR.py $SEGGED_TEXT_phrase_as_word_retain_alphanumeric $CATEGORY_SEED_CONCEPTS $SEGGED_TEXT_CATEGORIZATION $SEGGED_TEXT_WORDVEC $SEGGED_TEXT_TFIDF
python ./evaluate.py $SEGGED_TEXT_CATEGORIZATION

#random forest, big data, neural network, maximum likelihood
