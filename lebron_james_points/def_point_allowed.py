data = """
TOR
Toronto Raptors
64	24.19	7.66	4.33	3.13	1.46	0.98	2.25	44.95
ATL
Atlanta Hawks
64	23.20	7.53	4.86	3.20	1.35	0.83	2.70	43.37
WAS
Washington Wizards
64	23.20	8.33	4.78	2.83	1.97	0.93	2.14	46.93
IND
Indiana Pacers
65	22.90	8.19	3.80	2.14	1.45	0.84	2.43	42.87
SAC
Sacramento Kings
63	22.60	7.20	3.83	3.11	1.47	0.64	1.81	41.51
CHA
Charlotte Hornets
64	22.52	7.39	4.38	2.73	1.29	0.71	2.09	41.87
GSW
Golden State Warriors
63	22.28	8.02	3.57	3.04	1.67	0.78	2.09	42.52
UTH
Utah Jazz
64	22.14	7.07	4.52	2.95	1.84	1.18	1.71	44.75
DET
Detroit Pistons
63	21.93	7.42	4.49	2.70	1.64	0.67	1.83	42.67
CLE
Cleveland Cavaliers
64	21.88	7.97	4.08	2.47	1.55	0.64	2.59	41.54
BKN
Brooklyn Nets
65	21.52	7.88	4.12	2.78	1.33	0.68	2.04	41.15
LAL
Los Angeles Lakers
66	21.51	8.06	4.18	2.86	1.58	0.73	2.02	42.36
NYK
New York Knicks
64	21.45	7.69	4.41	2.52	1.72	0.88	2.37	42.72
MEM
Memphis Grizzlies
65	21.29	8.45	3.82	3.11	1.70	0.89	2.35	42.58
LAC
Los Angeles Clippers
63	21.28	7.26	3.92	2.83	1.53	0.74	2.15	40.53
CHI
Chicago Bulls
64	20.88	7.15	4.53	2.76	1.37	0.72	2.36	40.17
MIA
Miami Heat
64	20.57	7.35	4.40	2.73	1.51	0.79	2.38	40.51
MIN
Minnesota Timberwolves
65	20.46	7.49	3.76	2.51	1.59	0.77	2.30	39.87
NOR
New Orleans Pelicans
64	20.28	7.42	4.41	3.03	1.34	0.81	2.46	39.79
PHI
Philadelphia 76ers
64	20.28	8.36	3.66	2.55	1.50	0.92	2.35	40.71
POR
Portland Trail Blazers
63	20.13	7.46	3.94	2.40	1.73	1.03	2.32	40.95
BOS
Boston Celtics
63	19.72	7.72	3.66	2.66	1.47	0.58	1.83	38.79
SAS
San Antonio Spurs
64	19.68	8.07	4.18	2.51	1.69	0.76	2.14	40.84
MIL
Milwaukee Bucks
65	19.59	7.41	4.25	2.08	1.60	0.70	1.64	40.12
ORL
Orlando Magic
65	19.41	6.66	3.57	2.64	1.62	0.67	2.45	37.18
OKC
Oklahoma City Thunder
64	19.25	7.26	3.56	2.64	1.28	0.87	2.49	37.26
DAL
Dallas Mavericks
64	19.19	7.98	4.41	2.39	1.17	0.81	2.09	39.23
PHO
Phoenix Suns
64	19.16	7.34	3.28	2.54	1.96	0.79	1.75	39.39
HOU
Houston Rockets
64	19.05	7.82	3.89	2.36	1.51	0.90	2.12	39.38
DEN
Denver Nuggets
64	18.69	7.23	3.56	2.03	1.42	0.82	2.40	37.03"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed
