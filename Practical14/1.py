import xml.dom.minidom
import xml.sax
from datetime import datetime

# DOM PARSING

def parse_with_dom(file_path):
    start_time = datetime.now()

    dom = xml.dom.minidom.parse(file_path)
    terms = dom.getElementsByTagName('term')

    result = {
        'biological_process': {'id': '', 'name': '', 'count': 0},
        'molecular_function': {'id': '', 'name': '', 'count': 0},
        'cellular_component': {'id': '', 'name': '', 'count': 0}
    }

    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].firstChild.data
        term_id = term.getElementsByTagName('id')[0].firstChild.data
        name = term.getElementsByTagName('name')[0].firstChild.data
        is_a_tags = term.getElementsByTagName('is_a')
        count = len(is_a_tags)

        if namespace in result and count > result[namespace]['count']:
            result[namespace] = {'id': term_id, 'name': name, 'count': count}

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    return result, duration

# SAX PARSING

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ''
        self.namespace = ''
        self.term_id = ''
        self.name = ''
        self.is_a_count = 0
        self.in_term = False
        self.result = {
            'biological_process': {'id': '', 'name': '', 'count': 0},
            'molecular_function': {'id': '', 'name': '', 'count': 0},
            'cellular_component': {'id': '', 'name': '', 'count': 0}
        }
        self.temp_namespace = ''
        self.temp_id = ''
        self.temp_name = ''
        self.temp_count = 0
        self.buffer = ''

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == 'term':
            self.in_term = True
            self.temp_namespace = ''
            self.temp_id = ''
            self.temp_name = ''
            self.temp_count = 0
            self.buffer = ''

    def characters(self, content):
        if self.in_term:
            self.buffer += content

    def endElement(self, tag):
        if tag == 'id':
            self.temp_id = self.buffer.strip()
        elif tag == 'name':
            self.temp_name = self.buffer.strip()
        elif tag == 'namespace':
            self.temp_namespace = self.buffer.strip()
        elif tag == 'is_a':
            self.temp_count += 1
        elif tag == 'term':
            if self.temp_namespace in self.result and self.temp_count > self.result[self.temp_namespace]['count']:
                self.result[self.temp_namespace] = {
                    'id': self.temp_id,
                    'name': self.temp_name,
                    'count': self.temp_count
                }
            self.in_term = False
        self.buffer = ''


def parse_with_sax(file_path):
    start_time = datetime.now()

    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    return handler.result, duration


if __name__ == "__main__":
    file_path = "go_obo.xml"

    # DOM
    dom_result, dom_time = parse_with_dom(file_path)

    # SAX
    sax_result, sax_time = parse_with_sax(file_path)

    # Output
    print("\n--- DOM Results ---")
    for ont, info in dom_result.items():
        print(f"Ontology: {ont}")
        print(f"Term ID: {info['id']}")
        print(f"Name: {info['name']}")
        print(f"Number of <is_a>: {info['count']}\n")

    print("--- SAX Results ---")
    for ont, info in sax_result.items():
        print(f"Ontology: {ont}")
        print(f"Term ID: {info['id']}")
        print(f"Name: {info['name']}")
        print(f"Number of <is_a>: {info['count']}\n")

    print(f"DOM parsing time: {dom_time:.4f} seconds")
    print(f"SAX parsing time: {sax_time:.4f} seconds")

    # Comment on performance
    if dom_time < sax_time:
        print("# DOM was faster.")
    else:
        print("# SAX was faster.")
