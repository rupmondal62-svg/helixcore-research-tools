# Fetches active clinical trials for any disease area
import requests
import json

def fetch_trials(condition, status="RECRUITING", max_results=10):
    """
    Fetch active clinical trials from ClinicalTrials.gov
    
    Args:
        condition: Disease/condition to search
        status: Trial status (RECRUITING, ACTIVE, etc.)
        max_results: Number of results to return
    """
    
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    
    params = {
        "query.cond": condition,
        "filter.overallStatus": status,
        "pageSize": max_results,
        "format": "json"
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    trials = []
    for study in data.get("studies", []):
        protocol = study.get("protocolSection", {})
        id_module = protocol.get("identificationModule", {})
        status_module = protocol.get("statusModule", {})
        desc_module = protocol.get("descriptionModule", {})
        
        trial_info = {
            "NCT_ID": id_module.get("nctId", "N/A"),
            "Title": id_module.get("briefTitle", "N/A"),
            "Status": status_module.get("overallStatus", "N/A"),
            "Start_Date": status_module.get("startDateStruct", {}).get("date", "N/A"),
            "Summary": desc_module.get("briefSummary", "N/A")[:200]
        }
        trials.append(trial_info)
    
    return trials

# Example usage
if __name__ == "__main__":
    print("Fetching AI-related cancer clinical trials...\n")
    trials = fetch_trials("cancer", max_results=5)
    
    for i, trial in enumerate(trials, 1):
        print(f"Trial {i}:")
        print(f"  ID: {trial['NCT_ID']}")
        print(f"  Title: {trial['Title']}")
        print(f"  Status: {trial['Status']}")
        print(f"  Started: {trial['Start_Date']}")
        print(f"  Summary: {trial['Summary']}...")
        print("-" * 60)