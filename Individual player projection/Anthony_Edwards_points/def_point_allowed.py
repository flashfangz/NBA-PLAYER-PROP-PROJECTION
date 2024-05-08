data = """
SAS
San Antonio Spurs
62	23.51	6.93	5.76	3.41	2.05	0.68	2.49	46.17
WAS
Washington Wizards
62	23.22	7.38	5.73	3.10	1.72	0.89	2.73	45.77
ATL
Atlanta Hawks
62	24.92	6.45	5.47	3.62	1.70	0.71	2.87	45.23
LAL
Los Angeles Lakers
64	23.57	6.54	5.52	3.42	1.58	0.86	2.69	44.33
DAL
Dallas Mavericks
62	23.56	6.90	5.54	3.78	1.50	0.58	2.31	44.08
DET
Detroit Pistons
61	22.92	5.87	4.53	2.82	2.14	0.95	2.21	43.82
UTH
Utah Jazz
63	22.72	6.32	5.21	3.62	1.65	0.83	2.11	43.45
PHO
Phoenix Suns
62	21.98	6.80	5.40	3.24	1.57	0.91	2.52	43.16
POR
Portland Trail Blazers
61	22.43	6.54	5.18	2.73	1.87	0.64	2.69	42.89
BKN
Brooklyn Nets
62	22.88	7.07	4.95	3.57	1.40	0.64	2.19	42.72
LAC
Los Angeles Clippers
61	23.00	6.37	5.14	3.22	1.51	0.60	2.26	42.42
IND
Indiana Pacers
63	24.09	5.88	4.72	2.91	1.43	0.75	2.38	42.39
OKC
Oklahoma City Thunder
62	23.18	6.15	5.37	3.75	1.42	0.79	3.01	42.24
MIL
Milwaukee Bucks
63	23.35	6.84	5.11	3.14	1.25	0.44	2.28	42.01
MIA
Miami Heat
61	22.64	6.47	5.24	3.48	1.41	0.67	2.51	41.99
CHA
Charlotte Hornets
62	20.36	6.39	5.29	3.15	1.80	0.81	2.27	41.52
TOR
Toronto Raptors
62	23.12	6.06	5.07	3.50	1.43	0.52	2.37	41.48
MEM
Memphis Grizzlies
63	20.70	6.44	5.34	2.95	1.75	0.71	2.40	41.42
NOR
New Orleans Pelicans
62	21.88	5.92	5.37	3.52	1.73	0.54	2.68	41.17
CHI
Chicago Bulls
62	22.13	5.97	5.69	3.87	1.36	0.56	2.49	41.10
HOU
Houston Rockets
62	21.12	6.78	4.74	3.17	1.59	0.60	2.35	40.59
NYK
New York Knicks
62	22.47	5.83	5.20	3.74	1.09	0.78	2.35	40.53
PHI
Philadelphia 76ers
62	22.62	5.76	5.50	3.14	1.13	0.65	2.78	40.34
DEN
Denver Nuggets
62	20.87	6.16	5.00	2.92	1.51	0.61	2.26	39.86
SAC
Sacramento Kings
61	22.26	5.59	4.85	3.38	1.32	0.66	2.54	39.64
GSW
Golden State Warriors
61	22.24	5.53	4.35	3.26	1.58	0.60	2.47	39.47
BOS
Boston Celtics
61	21.15	6.59	4.52	3.22	1.33	0.36	2.19	38.72
ORL
Orlando Magic
63	21.10	5.86	4.72	2.95	1.47	0.43	2.81	38.10
MIN
Minnesota Timberwolves
62	20.18	6.56	4.40	2.90	1.47	0.55	2.62	38.09
CLE
Cleveland Cavaliers
62	19.64	5.78	4.44	3.14	1.30	0.62	2.22	36.78
"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed
