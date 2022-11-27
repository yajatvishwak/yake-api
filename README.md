
# yake-api
Find Keywords in any sentence (English)

    pip install  -r requirements.txt

Then, 

    python app.py

Then, hit `http://localhost:5001/` with a POST request and with body

    {
      "text": "your target sentence here"
    }

Will respond with

    [
    	[
    		"target sentence",
    		0.09700399286574239
    	],
    	[
    		"target",
    		0.29736558256021506
    	],
    	[
    		"sentence",
    		0.29736558256021506
    	]
    ]
