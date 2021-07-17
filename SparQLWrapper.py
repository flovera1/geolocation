from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3
from pprint import pprint






list_key_phrases = [
"16 second  downpour  moisture  http://t.co/HHImyESBPu ",
 "last Monday  floods  side",
 "Party  suns  life  Summer",
 "Land &  Sea  Calgary  Alberta  amp",
 "17th Avenue  McLeod Trail &  Centre Street  McLeod  25th  3rd  amp  west  way ",
 "American  #ecoliving  # @…  clay  @americanclay  sale  yyc  #  #  #  http://t.co/dNk9u5oPa6",
 "Kenyans  today  today  mall "
]





sparql = SPARQLWrapper('https://dbpedia.org/sparql')
sparql.setQuery(''' PREFIX dbo: <http://dbpedia.org/ontology/>
                    PREFIX geo:  <http://www.w3.org/2003/01/geo/wgs84_pos#>
                    
                    SELECT DISTINCT ?place ?label ?lat ?lng
                    WHERE { 
                      ?place a dbo:Place .
                      ?place rdfs:label ?label 
                         VALUES ?label { "Battery Park"@en} .
                      ?place geo:lat ?lat .
                      ?place geo:long ?lng .
                    }
                    ''')
sparql.setReturnFormat(JSON)
qres = sparql.query().convert()
pprint(qres)