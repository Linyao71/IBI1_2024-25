import xml.dom.minidom
import xml.sax
from datetime import datetime

def process_dom():
    start_time = datetime.now()
    doc = xml.dom.minidom.parse('go_obo.xml')
    terms = doc.getElementsByTagName('term')
    max_counts = {'molecular_function': {'max': 0, 'id': ''},'biological_process': {'max': 0, 'id': ''},'cellular_component': {'max': 0, 'id': ''}}
    
    for term in terms:
        # Extract GO ID
        id_elements = term.getElementsByTagName('id')
        if not id_elements:
            continue
        go_id = id_elements[0].firstChild.data.strip()
        
        # Extract Namespace
        ns_elements = term.getElementsByTagName('namespace')
        if not ns_elements:
            continue
        namespace = ns_elements[0].firstChild.data.strip()
        if namespace not in max_counts:
            continue
        
        # Count is_a elements under def
        def_elements = term.getElementsByTagName('def')
        is_a_count = 0
        if def_elements:
            def_element = def_elements[0]
            is_a_list = def_element.getElementsByTagName('is_a')
            is_a_count = len(is_a_list)
        
        # Update max counts
        current = max_counts[namespace]
        if is_a_count > current['max'] or (is_a_count == current['max'] and go_id < current['id']):
            current['max'] = is_a_count
            current['id'] = go_id
    
    end_time = datetime.now()
    print("\nDOM Results:")
    for ns, data in max_counts.items():
        print(f"{ns}: Term {data['id']} has {data['max']} is_a elements")
    print(f"DOM Time: {end_time - start_time}")
    return end_time - start_time

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.in_def = False
        self.current_term = {'id': '', 'namespace': '', 'is_a_count': 0}
        self.max_counts = {'molecular_function': {'max': 0, 'id': ''},'biological_process': {'max': 0, 'id': ''},'cellular_component': {'max': 0, 'id': ''}}
    
    def startElement(self, name, attrs):
        if name == 'term':
            self.current_term = {'id': '', 'namespace': '', 'is_a_count': 0}
        elif name == 'id':
            self.current_data = 'id'
        elif name == 'namespace':
            self.current_data = 'namespace'
        elif name == 'def':
            self.in_def = True
        elif name == 'is_a' and self.in_def:
            self.current_term['is_a_count'] += 1
    
    def characters(self, content):
        if self.current_data == 'id':
            self.current_term['id'] += content
        elif self.current_data == 'namespace':
            self.current_term['namespace'] += content
    
    def endElement(self, name):
        if name == 'term':
            ns = self.current_term['namespace'].strip()
            if ns in self.max_counts:
                current = self.max_counts[ns]
                count = self.current_term['is_a_count']
                go_id = self.current_term['id'].strip()
                if count > current['max'] or (count == current['max'] and go_id < current['id']):
                    current['max'] = count
                    current['id'] = go_id
        elif name == 'id':
            self.current_term['id'] = self.current_term['id'].strip()
            self.current_data = ""
        elif name == 'namespace':
            self.current_term['namespace'] = self.current_term['namespace'].strip()
            self.current_data = ""
        elif name == 'def':
            self.in_def = False

def process_sax():
    start_time = datetime.now()
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('go_obo.xml')
    end_time = datetime.now()
    print("\nSAX Results:")
    for ns, data in handler.max_counts.items():
        print(f"{ns}: Term {data['id']} has {data['max']} is_a elements")
    print(f"SAX Time: {end_time - start_time}")
    return end_time - start_time

if __name__ == "__main__":
    print("Processing with DOM...")
    dom_duration = process_dom()
    
    print("\nProcessing with SAX...")
    sax_duration = process_sax()
    
    print("\nTime Comparison:")
    print(f"DOM took: {dom_duration}")
    print(f"SAX took: {sax_duration}")
    if dom_duration < sax_duration:
        print("# DOM was faster.")
    else:
        print("# SAX was faster.")