# Micro servicios
En esta carpeta se definen los micro servicios utilizados en el capítulo 5. La especificación de cada micro servicio se realizó utilizando blueprint de Apiary.
La especificación de cada micro servicio es la siguiente:

## Text Analysis Microservice
+----------------------------------------------------------------------------------------+  
FORMAT: 1A  
HOST: https://uaz.cloud.tyk.io/sentiment

# Analysis API

Api que permite evaluar el sentimiento en un texto específico.

## Text Analysis Microservice [/api/v1/text-analysis]

### Sentiment Analysis [POST]

+ Request (application/json)

        {
            "review 0": "Some text",
            "review 1": "Some text",
            "review n": "Some text"
        }

+ Response 200 (application/json)

        {
            "positive": "0",
            "negative": "10",
            "neutral": "5",
            "total reviews": "15"
        }
+----------------------------------------------------------------------------------------+

## Information Microservice
+----------------------------------------------------------------------------------------+  
FORMAT: 1A  
HOST: https://uaz.cloud.tyk.io/content

# Information API

## Information Microservice [/api/v1/information{?t}]

+ Parameters
    + t - Corresponde al título de la película o serie de Netflix.

### Get Information [GET]

+ Response 200 (application/json)

        { 
            "Title": "Some text",
            "Year": "Some text", 
            "Rated": "Some text",
            "Released": "Some text",
            "Runtime": "Some text",
            "Genre": "Some text",
            "Director": "Some text",
            "Writer": "Some text",
            "Actors": "Some text",
            "Plot": "Some text",
            "Language": "Some text",
            "Country": "Some text",
            "Awards": "Some text.",
            "Poster": "Some text",
            "Metascore": "Some text",
            "imdbRating": "Some text",
            "imdbVotes": "Some text",
            "imdbID": "Some text",
            "Type": "Some text",
            "totalSeasons": "Some text",
            "Response": "Some text"
        }
+----------------------------------------------------------------------------------------+  

## Reviews Microservice
+----------------------------------------------------------------------------------------+  
FORMAT: 1A  
HOST: https://uaz.cloud.tyk.io/reviews

# Reviews API

## Reviews Microservice [/api/v1/tweets{?u}]

+ Parameters
    + u - Corresponde al nombre de usuario en Twitter.

### Get Reviews [GET]

+ Response 200 (application/json)

        {
            "review 0": "Some text",
            "review 1": "Some text",
            "review n": "Some text"
        }
