data = """
UTH
Utah Jazz
60	27.20	9.53	4.73	3.13	1.69	1.44	2.25	52.87
IND
Indiana Pacers
61	27.04	10.89	4.46	1.81	1.28	1.36	2.73	51.99
WAS
Washington Wizards
60	26.29	10.91	4.94	2.14	1.31	1.16	2.62	51.58
ATL
Atlanta Hawks
59	25.35	10.60	4.68	2.73	1.47	1.24	2.31	50.91
CHA
Charlotte Hornets
60	25.21	10.91	4.98	2.45	1.36	1.16	2.83	50.50
DAL
Dallas Mavericks
60	25.61	10.77	4.79	2.30	1.53	0.97	2.83	50.39
DET
Detroit Pistons
59	25.28	9.98	4.29	2.43	1.46	1.18	2.27	49.34
HOU
Houston Rockets
59	23.69	10.59	4.28	2.14	1.43	1.55	2.73	49.03
SAC
Sacramento Kings
59	26.24	10.23	4.63	2.48	1.38	0.88	3.21	49.03
CHI
Chicago Bulls
60	24.17	11.22	3.94	2.68	1.31	1.29	2.71	48.63
GSW
Golden State Warriors
59	23.38	10.81	4.69	2.27	1.55	1.02	2.51	48.59
TOR
Toronto Raptors
60	24.16	10.34	4.39	2.63	1.27	1.20	2.43	48.13
SAS
San Antonio Spurs
60	23.55	10.56	4.76	2.48	1.40	1.02	2.72	47.90
PHO
Phoenix Suns
59	25.02	9.68	3.56	2.36	1.72	1.08	2.63	47.75
PHI
Philadelphia 76ers
59	23.19	11.56	4.42	2.24	0.92	1.36	2.89	47.64
LAL
Los Angeles Lakers
61	24.59	9.69	4.43	2.81	1.31	1.07	2.58	47.42
POR
Portland Trail Blazers
58	23.30	9.89	4.61	2.02	1.49	1.25	2.95	47.35
MEM
Memphis Grizzlies
60	23.78	10.58	3.97	2.50	1.50	1.15	3.13	47.25
OKC
Oklahoma City Thunder
59	23.57	10.90	4.22	2.16	1.34	1.01	2.88	47.15
MIL
Milwaukee Bucks
61	23.81	10.25	3.78	2.76	1.26	1.19	2.49	46.64
NOR
New Orleans Pelicans
61	23.06	10.71	3.95	2.31	1.07	1.28	2.49	46.40
DEN
Denver Nuggets
60	22.86	10.29	3.92	2.08	1.26	1.13	1.95	46.31
LAC
Los Angeles Clippers
58	21.54	10.39	4.51	2.03	1.35	1.20	2.59	45.83
MIA
Miami Heat
59	23.15	9.70	4.64	2.39	1.31	1.01	2.89	45.82
BKN
Brooklyn Nets
59	22.67	10.59	4.37	2.24	1.11	0.99	2.58	45.65
CLE
Cleveland Cavaliers
59	22.19	10.05	4.01	2.19	1.30	1.07	2.44	44.94
NYK
New York Knicks
60	24.09	8.83	4.35	2.94	1.22	0.95	2.82	44.90
ORL
Orlando Magic
60	21.16	9.77	3.79	1.90	1.24	1.07	2.92	42.58
MIN
Minnesota Timberwolves
60	21.48	9.30	3.23	2.14	1.28	1.12	2.39	42.30
BOS
Boston Celtics
59	19.68	9.76	3.96	2.17	1.02	0.84	1.94	40.97"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed

