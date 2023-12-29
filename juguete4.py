import requests as rq

def get_covid_stats_about(state):
    # Make a GET request to the COVID Tracking Project API to fetch state-level COVID-19 data
    res = rq.get("https://api.covidtracking.com/v2/states.json")

    # Check if the request was successful (status code 200)
    if res.status_code != 200:
        return f"Request failed: {res}"

    found = None
    # Iterate through the data entries to find the one corresponding to the provided state code
    for entry in res.json()["data"]:
        # Check if the state name or state code matches the provided input
        if entry.get("state") == state or entry.get("state_code") == state:
            found = entry
            break

    # If no matching state is found, return an error message
    if found is None:
        return f"Invalid state: {state}"

    # Extract the number of deaths from the found state entry
    deaths = found["fips"]

    # Return a formatted string with information about the state's COVID-19 data
    return f"""
    Information for {found["name"]} ({found["state_code"]})
    Deaths: {deaths}
    """

# Prompt the user to input a state code and print the COVID-19 information for that state
state = input("Write the state code to get info about COVID-19:\n>>> ")
print(get_covid_stats_about(state))