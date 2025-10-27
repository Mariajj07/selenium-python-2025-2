Feature: Buscar una pelicula y validar su titulo y rating
    Scenario: Validar el nombre y el rating de la pelicula "Inception"
        Given el usuario esta en el home page de IMDb
        When busca la pelicula "Inception" 
        And selecciona el primer resultado de IMDb
        Then el titulo debe ser "Origen"
        And el rating debe ser 8,8