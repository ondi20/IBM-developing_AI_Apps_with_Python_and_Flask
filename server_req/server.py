from flask import Flask, make_response
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


#create an end point that returns the person’s data to the client in JSON format.
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404

        '''
        The above code simply checks if the variable data exits. If it does not, 
        the NameError is raised and an HTTP 404 is returned. If data exists and is 
        empty, an HTTP 500 is returned. If data exists and is not empty, 
        an HTTP 200 success message is returned.
        '''

#task 1
@app.route("/name_search")
def name_search():
    """find a person in the database

    Returns:
        json: person if found, with status of 200
        404: if not found
        422: if argument q is missing
    """
    query = request.args.get("q")

    if not query:
        return {"message": "Invalid input parameter"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person

    return ({"message": "Person not found"}, 404)

