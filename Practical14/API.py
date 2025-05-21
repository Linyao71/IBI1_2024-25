import xml.dom.minidom
import xml.sax
import time
from datetime import datetime

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.current_data = ""
        self.current_term = {}
        self.terms = []
        self.is_a_count = 0
    
    # Initialize the handler
    def startElement(self, tag, attributes):
        self.current_tag = tag
        self.current_data = ""
        if tag == "term":
            self.current_term = {}
            self.is_a_count = 0
        elif tag == "is_a":
            self.is_a_count += 1
    
    # Handle character data
    def characters(self, content):
        if self.current_tag in ["id", "namespace", "name"]:
            self.current_data += content
    
    # Handle end of an element
    def endElement(self, tag):
        if tag == "id":
            self.current_term["id"] = self.current_data
        elif tag == "namespace":
            self.current_term["namespace"] = self.current_data
        elif tag == "name":
            self.current_term["name"] = self.current_data
        elif tag == "term":
            self.current_term["is_a_count"] = self.is_a_count
            self.terms.append(self.current_term)

def print_results(results, api_name):
    print(f"\n{api_name} Result:")
    
    for namespace, data in results.items():
        terms = data["terms"]
        max_count = data["max_count"]
        
        if terms:
            print(f"\n{namespace.replace('_', ' ').title()} (max is_a count: {max_count}):")
            for term in terms:
                print(f"  GO ID: {term['id']}")
                print(f"  Term: {term['name']}")

xml_file = "go_obo.xml"

dom_start = time.time()
dom = xml.dom.minidom.parse(xml_file)
terms = dom.getElementsByTagName("term")
    
dom_results = {"molecular_function": {"max_count": -1, "terms": []},
    "biological_process": {"max_count": -1, "terms": []},
    "cellular_component": {"max_count": -1, "terms": []}}

for term in terms:
    namespace = term.getElementsByTagName("namespace")[0].firstChild.data
    is_a_count = len(term.getElementsByTagName("is_a"))
    
    if namespace in dom_results:
        if is_a_count == dom_results[namespace]["max_count"]:
            term_id = term.getElementsByTagName("id")[0].firstChild.data
            term_name = term.getElementsByTagName("name")[0].firstChild.data
            dom_results[namespace]["terms"].append({"id": term_id, "name": term_name, "is_a_count": is_a_count})

        elif is_a_count > dom_results[namespace]["max_count"]:
            dom_results[namespace]["max_count"] = is_a_count
            dom_results[namespace]["terms"] = []  
            term_id = term.getElementsByTagName("id")[0].firstChild.data
            term_name = term.getElementsByTagName("name")[0].firstChild.data
            dom_results[namespace]["terms"].append({"id": term_id, "name": term_name, "is_a_count": is_a_count})

dom_time = time.time() - dom_start      
print_results(dom_results, "DOM")
    
sax_start = time.time()
handler = GOHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(xml_file)
    
sax_results = {"molecular_function": {"max_count": -1, "terms": []},
    "biological_process": {"max_count": -1, "terms": []},
    "cellular_component": {"max_count": -1, "terms": []}}
    
for term in handler.terms:
    namespace = term["namespace"]
    is_a_count = term["is_a_count"]
        
    if namespace in sax_results:
        if is_a_count == sax_results[namespace]["max_count"]:
            sax_results[namespace]["terms"].append({"id": term["id"], "name": term["name"], "is_a_count": is_a_count })

        elif is_a_count > sax_results[namespace]["max_count"]:
            sax_results[namespace]["max_count"] = is_a_count
            sax_results[namespace]["terms"] = []  
            sax_results[namespace]["terms"].append({"id": term["id"], "name": term["name"], "is_a_count": is_a_count})
    
sax_time = time.time() - sax_start 
print_results(sax_results, "SAX")
    
fastest = "SAX" if sax_time < dom_time else "DOM"
print("\nPerformance comparison results:")
print(f"DOM processing time: {dom_time:.2f} s")
print(f"SAX processing time: {sax_time:.2f} s")
print(f"Fastest API: {fastest}")

'''
DOM processing time: 19.15 s
SAX processing time: 2.87 s
Fastest API: SAX
'''