from A_OO_get_post_soup_update_dec import DEFAULT_HEADERS, update_peviitor_api
from L_00_logo import update_logo
import requests
import uuid


def prepare_post_request() -> tuple:
    """
    aceasta functie va returna headere fresh pentru un post request
    """
    url = 'https://nngroup.wd3.myworkdayjobs.com/wday/cxs/nngroup/WDExternal/jobs'

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'PLAY_SESSION=f5bf9a4db33899e4504941ac97c183a051e16588-nngroup_pSessionId=h84opj7gbmlihiqnjt3ejlcfk&instance=wd3prvps0005c; wday_vps_cookie=2586220042.58930.0000; timezoneOffset=-180; TS014c1515=01f629630405732127c167207b69cbb094ecc2683a71e895879b5cc07270720ea341da2beb10aa0a67752a27454f089678ea3b4376; wd-browser-id=2d653eb8-f638-4b86-8874-189d80f5f47c; CALYPSO_CSRF_TOKEN=ea91ffe0-c805-4062-a09a-3e76572a4666',
        'Origin': 'https://nngroup.wd3.myworkdayjobs.com',
        'Referer': 'https://nngroup.wd3.myworkdayjobs.com/WDExternal?locationCountry=f2e609fe92974a55a05fc1cdc2852122',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-CALYPSO-CSRF-TOKEN': 'ea91ffe0-c805-4062-a09a-3e76572a4666',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'}

    data = {
        "appliedFacets": {
            "locationCountry": ["f2e609fe92974a55a05fc1cdc2852122"]
        },
        "limit": 20,
        "offset": 0,
        "searchText": ""
    }

    return url, headers, data


def collect_data_from_nn() -> list[dict]:
    url, headers, data = prepare_post_request()
    response = requests.post(url=url, headers=headers, json=data).json()
    lstdata = []
    for job in response['jobPostings']:
        lstdata.append({
            "id": str(uuid.uuid4()),
            "job_title": job['title'],
            "job_link": f'https://nngroup.wd3.myworkdayjobs.com/en-US/WDExternal/details/{job["externalPath"].split("/")[-1]}?q=Romania',
            "company": "NN",
            "country": "Romania",
            "city": job["locationsText"]
        })
    return lstdata


print(collect_data_from_nn())


@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'NN'
data_list = collect_data_from_nn()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('NN',
                  'https://www.nndirect.ro/clients/images/NN_logo_facebook_share.png'))