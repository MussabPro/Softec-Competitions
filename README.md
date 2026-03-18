# SOFTEC Competitions Data Extractor

This project fetches SOFTEC competitions data directly from the official API and generates:

- A structured CSV file with prizes, registration fees, and team-size limits.
- A local folder of competition logos with clean filenames.

## Project Purpose

The script is designed to automate competition data collection for documentation and reporting, without scraping local HTML files.

## Data Source

- API Endpoint: `https://backend.softecnu.org/api/competitions_listable/`
- Input fields used: `name`, `registration_name`, `logo`, `winner_Prize`, `runnerUp_Prize`, `fees`, `min_team_size`, `max_team_size`

## Output Files

| File / Folder | Description |
|---|---|
| `extract_competitions.py` | Python script that fetches API data and generates outputs |
| `competitions_data.csv` | Generated competition dataset |
| `competition_logos/` | Downloaded logo images (one per competition) |

## CSV Schema

| Column | Description |
|---|---|
| `logo` | Logo filename stored in `competition_logos/` |
| `Competition Name` | Competition title |
| `Winner Prize` | Winner prize amount (PKR) |
| `Runner Up Prize` | Runner-up prize amount (PKR) |
| `Registration Fees` | Registration fee (PKR) |
| `Minimum Team Member Allowed` | Minimum team size |
| `Maximum Team Member Allowed` | Maximum team size |

## How to Run

```bash
python3 extract_competitions.py
```

After running, refresh `competitions_data.csv` and `competition_logos/`.

## Competitions Table

| Competition | Winner Prize | Runner Up Prize | Registration Fees | Min Team | Max Team |
|---|---:|---:|---:|---:|---:|
| <img src="competition_logos/01_ai_hackathon.png" width="38" alt="AI Hackathon"> AI Hackathon | 100000 | 50000 | 5000 | 2 | 3 |
| <img src="competition_logos/02_app_development_competition.png" width="38" alt="App Development Competition"> App Development Competition | 60000 | 30000 | 2500 | 1 | 3 |
| <img src="competition_logos/03_bridge_construction_competition.png" width="38" alt="Bridge Construction Competition"> Bridge Construction Competition | 30000 | 15000 | 1700 | 1 | 2 |
| <img src="competition_logos/04_cad_war_competition.png" width="38" alt="CAD War Competition"> CAD War Competition | 25000 | 10000 | 1700 | 1 | 1 |
| <img src="competition_logos/05_cinematography_competition.png" width="38" alt="Cinematography Competition"> Cinematography Competition | 20000 | 10000 | 1500 | 1 | 1 |
| <img src="competition_logos/06_cyber_security_competition.png" width="38" alt="Cyber Security Competition"> Cyber Security Competition | 50000 | 25000 | 2000 | 1 | 3 |
| <img src="competition_logos/07_engineering_project_competition.png" width="38" alt="Engineering Project Competition"> Engineering Project Competition | 70000 | 35000 | 3000 | 1 | 4 |
| <img src="competition_logos/08_free_hand_sketching_competition.png" width="38" alt="Free Hand Sketching Competition"> Free Hand Sketching Competition | 20000 | 10000 | 1500 | 1 | 1 |
| <img src="competition_logos/09_game_jam_competition.png" width="38" alt="Game Jam Competition"> Game Jam Competition | 50000 | 25000 | 2500 | 1 | 4 |
| <img src="competition_logos/10_genx_gaming.png" width="38" alt="GenX Gaming"> GenX Gaming | 20000 | 10000 | 2000 | 1 | 1 |
| <img src="competition_logos/11_ideas_xtreme.png" width="38" alt="Ideas Xtreme"> Ideas Xtreme | 25000 | 20000 | 3000 | 1 | 2 |
| <img src="competition_logos/12_line_following_robot.png" width="38" alt="Line Following Robot"> Line Following Robot | 30000 | 15000 | 2000 | 3 | 4 |
| <img src="competition_logos/13_machine_learning_competition.png" width="38" alt="Machine Learning Competition"> Machine Learning Competition | 80000 | 40000 | 3000 | 1 | 3 |
| <img src="competition_logos/14_programming_competition.png" width="38" alt="Programming Competition"> Programming Competition | 80000 | 40000 | 3000 | 1 | 3 |
| <img src="competition_logos/15_query_vista_competition.png" width="38" alt="Query Vista Competition"> Query Vista Competition | 50000 | 25000 | 2000 | 1 | 2 |
| <img src="competition_logos/16_robo_rumble.png" width="38" alt="Robo Rumble"> Robo Rumble | 100000 | 50000 | 5000 | 1 | 4 |
| <img src="competition_logos/17_software_project_competition.png" width="38" alt="Software Project Competition"> Software Project Competition | 80000 | 40000 | 2500 | 1 | 4 |
| <img src="competition_logos/18_ui_ux_competition.png" width="38" alt="UI/UX Competition"> UI/UX Competition | 30000 | 15000 | 1700 | 1 | 3 |
| <img src="competition_logos/19_web_development_competition.png" width="38" alt="Web Development Competition"> Web Development Competition | 80000 | 40000 | 2500 | 1 | 3 |

## Notes

- Current API response contains 19 competitions.
- If API data changes, rerun the script to update both CSV and logos.
