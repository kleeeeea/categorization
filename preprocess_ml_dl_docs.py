import re
import pickle
import os
from kleeeeea_helper.text import toOneLine
from kleeeeea_helper.io_util import open_writeLines

root_dir = '/home/klee/data/concept_medical/'

def clean_text(doc):
    doc = re.sub(r'\d+', '<NUM>', doc)
    # doc = re.sub(r'(DOI:|PMID:).+\r\n', '', doc)
    return doc


def get_expert_docs(text, line_no):
    line_no.append(-1)
    docs = [text[st:ed] for st, ed in zip(line_no[:-2], line_no[1:-1])]

    expert_docs = []
    for i, doc in enumerate(docs):
        doc = ''.join(doc).replace('\r\n', '\n\n')
        doc = re.sub(r'[^\x00-\x7F]+', ' ', doc)
        doc = doc.split('\n\n')
        new_doc = []
        for sent in doc:
            if re.search('(doi:)|(DOI:)|(Author information)|(PMID:)', sent):
                continue
            else:
                new_doc.append(sent)
        new_doc = ' '.join(new_doc).strip()

        expert_docs.append(clean_text(new_doc))
        # title, abstract = new_doc.split('. ', 1)
        #
        # # title = new_doc[0]
        # # abstract = ' '.join(new_doc[1:])
        # # title = clean_text(title)
        # # abstract = clean_text(abstract)
        #
        # # title, abstract =
        # expert_docs.append({'title': title, 'abstract': abstract})

    return expert_docs


with open('{}/dl_and_anesthesia_raw.txt'.format(root_dir)) as fin:
    line_no = []
    text = [l for l in fin]
    for i, l in enumerate(text):
        if re.search(r'^[\d]+\. ', l):
            # print(l)
            line_no.append(i)
    dl_docs = get_expert_docs(text, line_no)

with open('{}/ml_and_anesthesia_raw.txt'.format(root_dir)) as fin:
    line_no = []
    text = [l for l in fin]
    for i, l in enumerate(text):
        if re.search(r'^[\d]+\. ', l):
            # print(l)
            line_no.append(i)
    ml_docs = get_expert_docs(text, line_no)

ml_docs = [toOneLine(doc) for doc in ml_docs]
dl_docs = [toOneLine(doc) for doc in dl_docs]

open_writeLines('{}/ml_and_anesthesia.txt'.format(root_dir), ml_docs)
open_writeLines('{}/dl_and_anesthesia.txt'.format(root_dir), dl_docs)


