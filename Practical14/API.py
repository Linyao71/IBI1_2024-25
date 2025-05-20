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
    
    def startElement(self, tag, attributes):
        self.current_tag = tag
        self.current_data = ""
        if tag == "term":
            self.current_term = {}
            self.is_a_count = 0
        elif tag == "is_a":
            self.is_a_count += 1
    
    def characters(self, content):
        if self.current_tag in ["id", "namespace", "name"]:
            self.current_data += content
    
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

def analyze_with_dom(xml_file):
    start_time = time.time()
    
    with open(xml_file, "r", encoding="utf-8") as f:
        xml_content = f.read()
    xml_content = xml_content.replace("&", "&amp;")
        
    dom = xml.dom.minidom.parseString(xml_content)
    terms = dom.getElementsByTagName("term")
        
    results = {
        "molecular_function": {"max_count": -1, "term": None},
        "biological_process": {"max_count": -1, "term": None},
        "cellular_component": {"max_count": -1, "term": None}}
        
    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data
        is_a_count = len(term.getElementsByTagName("is_a"))
                
        if namespace in results and is_a_count > results[namespace]["max_count"]:
            results[namespace]["max_count"] = is_a_count
            term_id = term.getElementsByTagName("id")[0].firstChild.data
            term_name = term.getElementsByTagName("name")[0].firstChild.data
            results[namespace]["term"] = {"id": term_id, "name": term_name, "is_a_count": is_a_count}
        
        return results, time.time() - start_time

def analyze_with_sax(xml_file):
    start_time = time.time()
    

    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
        
    results = {
        "molecular_function": {"max_count": -1, "term": None},
        "biological_process": {"max_count": -1, "term": None},
        "cellular_component": {"max_count": -1, "term": None}}
        
    for term in handler.terms:
        namespace = term["namespace"]
        is_a_count = term["is_a_count"]
            
        if namespace in results and is_a_count > results[namespace]["max_count"]:
            results[namespace]["max_count"] = is_a_count
            results[namespace]["term"] = {"id": term["id"], "name": term["name"], "is_a_count": is_a_count}
        
        return results, time.time() - start_time

def print_results(results, api_name, time_taken):
    print(f"\n{api_name} 分析结果:")
    print(f"处理时间: {time_taken:.4f} 秒")
    
    for namespace, data in results.items():
        term = data["term"]
        if term:
            print(f"\n{namespace.replace('_', ' ').title()}:")
            print(f"GO ID: {term['id']}")
            print(f"术语名称: {term['name']}")
            print(f"is_a关系数量: {term['is_a_count']}")

xml_file = "go_obo.xml"
    
print("\n Using the DOM API for analysis...")
dom_results, dom_time = analyze_with_dom(xml_file)
if dom_results:
    print_results(dom_results, "DOM API", dom_time)
    
print("\nUsing the SAX API for analysis...")
sax_results, sax_time = analyze_with_sax(xml_file)
if sax_results:
    print_results(sax_results, "SAX API", sax_time)
    
if dom_results and sax_results:
    fastest = "SAX" if sax_time < dom_time else "DOM"
    print("\nPerformance comparison results:")
    print(f"DOM processing time: {dom_time:.4f} s")
    print(f"SAX processing time: {sax_time:.4f} s")
    print(f"Fastest API: {fastest}")