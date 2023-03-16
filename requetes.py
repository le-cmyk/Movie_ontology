
dictionnaire={"List_the_instances_of_the_class_Actor":
            """
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX mv: <http://www.semanticweb.org/esilv/ontologies/2023/2/untitled-ontology-20#>

                    SELECT ?actor
                    WHERE {
                        ?actor rdf:type mv:Actor
                        }
            """,
            
            "List_the_name_of_all_Thriller_movies":
            """
                        PREFIX owl: <http://www.w3.org/2002/07/owl#>
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        PREFIX mv: <http://www.semanticweb.org/esilv/ontologies/2023/2/untitled-ontology-20#>

                        SELECT ?d ?m
                        WHERE {
                                ?d mv:isDirectorOf ?m .
                                ?m mv:genre ?genre .
                                ?m rdf:type mv:Movie .
                                FILTER (?genre = "Thriller")	
                        }
            """,
            "List_the_name_of_all_Crime_Thriller_movies":
            """
                        PREFIX owl: <http://www.w3.org/2002/07/owl#>
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        PREFIX mv: <http://www.semanticweb.org/esilv/ontologies/2023/2/untitled-ontology-20#>

                        SELECT DISTINCT ?t ?m
                        WHERE {
                                ?t mv:title ?title .
                                ?m mv:genre ?genre .
                                ?m rdf:type mv:Movie .
                                FILTER (?genre = "Thriller" || ?genre = "Crime")	
                        }
            """,
            "List_the_name_of_Actors_older_than_51_years":
            """
                        PREFIX owl: <http://www.w3.org/2002/07/owl#>
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        PREFIX mv: <http://www.semanticweb.org/esilv/ontologies/2023/2/untitled-ontology-20#>

                        SELECT ?actor
                        WHERE {
                                ?actor mv:age ?age .
                                ?actor rdf:type mv:Actor .
                                FILTER (?age >= 51)
                        }
            """,
            "List_of_movies_that_are_played_in_theater_for_a_specific_day":
            """


                        PREFIX owl: <http://www.w3.org/2002/07/owl#>
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        PREFIX mv: <http://www.semanticweb.org/esilv/ontologies/2023/2/untitled-ontology-20#>

                        SELECT DISTINCT ?theatre ?m ?sd
                        WHERE {
                                ?nt mv:nameTheatre ?theatre .
                                ?m mv:title ?Movie .
                                ?dt mv:startDate ?sd
                        }
            """,
            "A_query_that_contains_at_least_2_Optional_Graph_Patterns":
            """

                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX owl: <http://www.w3.org/2002/07/owl#>
                        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                        PREFIX mv: <http://www.semanticweb.org/esilv/ontologies/2023/2/untitled-ontology-20#>

                        SELECT ?movie ?worker ?theatre
                        WHERE {
                                ?movie rdf:type mv:Movie .
                                OPTIONAL {
                                        ?movie mv:hasActor ?worker . 
                                }
                                OPTIONAL {
                                        ?movie mv:hasTheatre ?theatre .
                                        FILTER  NOT EXISTS { ?movie mv:hasActor ?worker .}
                                }
                        }
            """,
            "A_query_that_contains_at_least_2_alternatives_and_conjunctions":
            """
            
            """,
            "A_query_that_contains_a_CONSTRUCT_query_form":
            """
            
            """,
            "A_query_that_contains_an_ASK_query_form":
            """
            
            """,
            "A_query_that_contains_a_DESCRIBE_query_form":
            """
            
            """
    }