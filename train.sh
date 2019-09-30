#!/usr/bin/env bash

source ./environs.sh

# assume AutoPhrase is installed
cd ../AutoPhrase/
./auto_phrase.sh

export TEXT_TO_SEG=$RAW_TRAIN
./phrasal_segmentation.sh
cd -

python segmented2phrase_as_word.py $SEGGED_TEXT $SEGGED_TEXT_phrase_as_word
python retain_alphanumeric.py $SEGGED_TEXT_phrase_as_word $SEGGED_TEXT_phrase_as_word_retain_alphanumeric
python buildIndex.py $SEGGED_TEXT_phrase_as_word_retain_alphanumeric $SEGGED_TEXT_WORDVEC $SEGGED_TEXT_TFIDF

./test.sh
