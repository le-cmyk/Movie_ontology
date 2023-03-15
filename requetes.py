
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
            
            """,
            "List_the_name_of_all_Crime_Thriller_movies":
            """

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
            
            """,
            "A_query_that_contains_at_least_2_Optional_Graph_Patterns":
            """
            
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