import logging
import re
import sys

logging.basicConfig(filename=__file__ + '.log', level=logging.DEBUG)

file = None

if len(sys.argv) > 1:
    file = destinedir = sys.argv[1]

outfile = file + '_phraseAsWord'
# '../data/data_oneFilePerLine/jmlr_vldb/segmented_text.txt_phraseAsWord_alnumRetained_removedJournalHeader_strong_concepts'

if len(sys.argv) > 2:
    outfile = sys.argv[2]

square_brackets_enclosed = re.compile(
    r"<phrase>(?P<phrase>[^<]*)</phrase>"
)


def brackets2UnderScoreNotation(l):
    return square_brackets_enclosed.sub(lambda x: "<phrase>%s</phrase>" % re.sub('\s', '_', x.group('phrase')), l)


# x.group('phrase')

underScore = '_'
consecutive_underScore_regex = re.compile('%s{5,}' % underScore)


def condenseConsecutiveunderScoreToOne(l):
    return consecutive_underScore_regex.sub(lambda x: underScore, l)


def singleFileClean(file, file_output):
    # import ipdb; ipdb.set_trace()
    lineno = -1
    with open(file_output, "w") as f_out:
        with open(file) as f:
            for l in f:
                lineno += 1
                # l = l.replace('$', ' ')
                # l = l.lower()
                l_o = l

                l = brackets2UnderScoreNotation(l)

                l = condenseConsecutiveunderScoreToOne(l)
                # if '_____' in l:
                #     import ipdb;ipdb.set_trace()
                # if 'dimension)._There' in l:
                #     import ipdb; ipdb.set_trace() 
                try:
                    # f_forword2vec.write(l.strip() + ' ')
                    f_out.write(l.strip() + '\n')
                except Exception as e:
                    import ipdb;
                    ipdb.set_trace()
                    logging.debug(e)
                else:
                    pass


if __name__ == '__main__':
    singleFileClean(file, outfile)
