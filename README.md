# SOFTEC Competitions Data Extractor

This project fetches SOFTEC competitions data directly from the official API and generates:

- A structured CSV file with prizes, registration fees, and team-size limits.
- A local folder of competition logos with clean filenames.
- A local folder of competition PDF documents/details.

## Project Purpose

The script is designed to automate competition data collection for documentation and reporting, without scraping local HTML files.

## Data Source

- API Endpoint: `https://backend.softecnu.org/api/competitions_listable/`
- Input fields used: `name`, `registration_name`, `logo`, `details[].document`, `winner_Prize`, `runnerUp_Prize`, `fees`, `min_team_size`, `max_team_size`

## Output Files

| File / Folder | Description |
|---|---|
| `extract_competitions.py` | Python script that fetches API data and generates outputs |
| `competitions_data.csv` | Generated competition dataset |
| `competition_logos/` | Downloaded logo images (one per competition) |
| `competition_pdfs/` | Downloaded PDF/detail documents (ignored by Git) |

## CSV Schema

| Column | Description |
|---|---|
| `logo` | Logo filename stored in `competition_logos/` |
| `documents` | Pipe-separated PDF filenames stored in `competition_pdfs/` |
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

After running, refresh `competitions_data.csv`, `competition_logos/`, and `competition_pdfs/`.

## Competitions Table

<table>
	<thead>
		<tr>
			<th align="left">Competition</th>
			<th align="center">Winner Prize</th>
			<th align="center">Runner Up Prize</th>
			<th align="center">Registration Fees</th>
			<th align="center">Min Team</th>
			<th align="center">Max Team</th>
		</tr>
	</thead>
	<tbody>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/01_ai_hackathon.png" width="38" alt="AI Hackathon"> AI Hackathon</nobr></td><td align="center" valign="middle">100000</td><td align="center" valign="middle">50000</td><td align="center" valign="middle">5000</td><td align="center" valign="middle">2</td><td align="center" valign="middle">3</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/02_app_development_competition.png" width="38" alt="App Development Competition"> App Development Competition</nobr></td><td align="center" valign="middle">60000</td><td align="center" valign="middle">30000</td><td align="center" valign="middle">2500</td><td align="center" valign="middle">1</td><td align="center" valign="middle">3</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/03_bridge_construction_competition.png" width="38" alt="Bridge Construction Competition"> Bridge Construction Competition</nobr></td><td align="center" valign="middle">30000</td><td align="center" valign="middle">15000</td><td align="center" valign="middle">1700</td><td align="center" valign="middle">1</td><td align="center" valign="middle">2</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/04_cad_war_competition.png" width="38" alt="CAD War Competition"> CAD War Competition</nobr></td><td align="center" valign="middle">25000</td><td align="center" valign="middle">10000</td><td align="center" valign="middle">1700</td><td align="center" valign="middle">1</td><td align="center" valign="middle">1</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/05_cinematography_competition.png" width="38" alt="Cinematography Competition"> Cinematography Competition</nobr></td><td align="center" valign="middle">20000</td><td align="center" valign="middle">10000</td><td align="center" valign="middle">1500</td><td align="center" valign="middle">1</td><td align="center" valign="middle">1</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/06_cyber_security_competition.png" width="38" alt="Cyber Security Competition"> Cyber Security Competition</nobr></td><td align="center" valign="middle">50000</td><td align="center" valign="middle">25000</td><td align="center" valign="middle">2000</td><td align="center" valign="middle">1</td><td align="center" valign="middle">3</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/07_engineering_project_competition.png" width="38" alt="Engineering Project Competition"> Engineering Project Competition</nobr></td><td align="center" valign="middle">70000</td><td align="center" valign="middle">35000</td><td align="center" valign="middle">3000</td><td align="center" valign="middle">1</td><td align="center" valign="middle">4</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/08_free_hand_sketching_competition.png" width="38" alt="Free Hand Sketching Competition"> Free Hand Sketching Competition</nobr></td><td align="center" valign="middle">20000</td><td align="center" valign="middle">10000</td><td align="center" valign="middle">1500</td><td align="center" valign="middle">1</td><td align="center" valign="middle">1</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/09_game_jam_competition.png" width="38" alt="Game Jam Competition"> Game Jam Competition</nobr></td><td align="center" valign="middle">50000</td><td align="center" valign="middle">25000</td><td align="center" valign="middle">2500</td><td align="center" valign="middle">1</td><td align="center" valign="middle">4</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/10_genx_gaming.png" width="38" alt="GenX Gaming"> GenX Gaming</nobr></td><td align="center" valign="middle">20000</td><td align="center" valign="middle">10000</td><td align="center" valign="middle">2000</td><td align="center" valign="middle">1</td><td align="center" valign="middle">1</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/11_ideas_xtreme.png" width="38" alt="Ideas Xtreme"> Ideas Xtreme</nobr></td><td align="center" valign="middle">25000</td><td align="center" valign="middle">20000</td><td align="center" valign="middle">3000</td><td align="center" valign="middle">1</td><td align="center" valign="middle">2</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/12_line_following_robot.png" width="38" alt="Line Following Robot"> Line Following Robot</nobr></td><td align="center" valign="middle">30000</td><td align="center" valign="middle">15000</td><td align="center" valign="middle">2000</td><td align="center" valign="middle">3</td><td align="center" valign="middle">4</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/13_machine_learning_competition.png" width="38" alt="Machine Learning Competition"> Machine Learning Competition</nobr></td><td align="center" valign="middle">80000</td><td align="center" valign="middle">40000</td><td align="center" valign="middle">3000</td><td align="center" valign="middle">1</td><td align="center" valign="middle">3</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/14_programming_competition.png" width="38" alt="Programming Competition"> Programming Competition</nobr></td><td align="center" valign="middle">80000</td><td align="center" valign="middle">40000</td><td align="center" valign="middle">3000</td><td align="center" valign="middle">1</td><td align="center" valign="middle">3</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/15_query_vista_competition.png" width="38" alt="Query Vista Competition"> Query Vista Competition</nobr></td><td align="center" valign="middle">50000</td><td align="center" valign="middle">25000</td><td align="center" valign="middle">2000</td><td align="center" valign="middle">1</td><td align="center" valign="middle">2</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/16_robo_rumble.png" width="38" alt="Robo Rumble"> Robo Rumble</nobr></td><td align="center" valign="middle">100000</td><td align="center" valign="middle">50000</td><td align="center" valign="middle">5000</td><td align="center" valign="middle">1</td><td align="center" valign="middle">4</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/17_software_project_competition.png" width="38" alt="Software Project Competition"> Software Project Competition</nobr></td><td align="center" valign="middle">80000</td><td align="center" valign="middle">40000</td><td align="center" valign="middle">2500</td><td align="center" valign="middle">1</td><td align="center" valign="middle">4</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/18_ui_ux_competition.png" width="38" alt="UI/UX Competition"> UI/UX Competition</nobr></td><td align="center" valign="middle">30000</td><td align="center" valign="middle">15000</td><td align="center" valign="middle">1700</td><td align="center" valign="middle">1</td><td align="center" valign="middle">3</td></tr>
		<tr><td align="left" valign="middle"><nobr><img src="competition_logos/19_web_development_competition.png" width="38" alt="Web Development Competition"> Web Development Competition</nobr></td><td align="center" valign="middle">80000</td><td align="center" valign="middle">40000</td><td align="center" valign="middle">2500</td><td align="center" valign="middle">1</td><td align="center" valign="middle">3</td></tr>
	</tbody>
</table>

## Notes

- Current API response contains 19 competitions.
- If API data changes, rerun the script to update CSV, logos, and PDF documents.
