from typing import Dict

acquisition = "acquired"
ipo = "IPO"
size = "over max revenue"  # only need this one

# sources:
# 2021 https://blog.wealthfront.com/announcing-2021-career-launching-companies/
# 2020 https://blog.wealthfront.com/announcing-2020-career-launching-companies/
# 2019 https://blog.wealthfront.com/announcing-2019-career-launching-companies/
# 2018 https://blog.wealthfront.com/2018-wealthfront-career-launching-companies-list/
# 2017 https://blog.wealthfront.com/2017-career-launching-companies-list/
# 2016 https://blog.wealthfront.com/2016-career-launching-companies-list/

# Year is needed when creating the data, not using
dropped: Dict[str, str] = {
    # 2021
    "23andme": size,
    "Chime": size,
    "Databricks": size,
    "goPuff": size,
    "Instacart": size,
    "Marqueta": size,
    "Payoneer": size,
    "Samsara": size,
    "Warby Parker": size,
    "Asana": ipo,
    "Affirm": ipo,
    "Snowflake": ipo,
    "Wish": ipo,
    # 2020
    "Avalara": ipo,
    "Cloudflare": ipo,
    "CrowdStrike": ipo,
    "Datadog": ipo,
    "Health Catalyst": ipo,
    "Madallia": ipo,
    "PagerDuty": ipo,
    "Zoom": ipo,
    "Lyft": ipo,
    "Pinterest": ipo,
    "Slack": ipo,
    "Uber": ipo,
    "Postmates": size,
    "Procore": size,
    "Robinhood": size,
    "Rubrik": size,
    "Tanium": size,
    "Squarespace": size,
    "UiPath": size,
    "Wish": size,
    # 2019
    "Cohesity": size,
    "Coinbase": size,
    "DoorDash": size,
    "Slack Technologies": size,
    # 2018
    "Houzz": size,
    "Stitch Fix": size,
    "Stripe": size,
    # 2017
    "Credit Karma": size,
    "Pinterest": size,
    "Snap": size,
    # 2016
    "Airbnb": size,
    "Cloudera": size,
    "Dropbox": size,
    "JustFab": size,
    "Nutanix": size,
    "Sonos": size,
    "Spotify": size,
    "Survey Monkey": size,
    "Uber": size,
    "Wework": size,
}


dropped = {k.lower(): v for k, v in dropped.items()}
