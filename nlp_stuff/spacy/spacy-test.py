import sys
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy import displacy
import pdfplumber

with pdfplumber.open(sys.argv[1]) as pdf:
    pdf_full_text = ''
    for pdf_page in pdf.pages:
      single_page_text = pdf_page.extract_text()
      pdf_full_text = pdf_full_text + '\n' + single_page_text

red_flag_terms = ["exclusivity", "Exclusivity", "exclusively and in perpetuity", "Exclusively", "intellectual property rights", "Intellectual property rights", "right to sublicense", "material disclosure", "material connection"]
notice_terms = ["Attach", "attach", "Attached", "attached"]

nlp = spacy.load("en_core_web_sm")

# Only run nlp.make_doc to speed things up
#patterns = [nlp.make_doc(text) for text in terms]

red_flag_patterns = [nlp(term) for term in red_flag_terms] # process each term to create phrase pattern
#matcher.add("TerminologyList", patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add('IMPORTANT', None, *red_flag_patterns) #add patterns to matcher

notice_patterns = [nlp(term) for term in notice_terms]
matcher.add('ATTACHMENT', None, *notice_patterns)


doc = nlp(pdf_full_text)
matches = matcher(doc)
#import ipdb; ipdb.set_trace()
for match_id, start, end in matches:
    span = Span(doc, start, end, label=match_id)
    doc.ents = list(doc.ents) + [span] # add span to doc.ents
    #print(span.text)
print([(ent.text, ent.label_) for ent in doc.ents]) 

# Custom display - our custom defined keywords only
colors = {"IMPORTANT": "linear-gradient(90deg, #aa9cfc, #fc9ce7)", "ATTACHMENT": "linear-gradient(90deg, #B58ECC, #5DE6DE)"}
options = {"ents": ["IMPORTANT", "ATTACHMENT"], "colors": colors}
displacy.serve(doc, style="ent", options=options)

# Default display
#displacy.serve(doc, style="ent")
