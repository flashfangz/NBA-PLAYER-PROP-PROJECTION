data = """
UTH
Utah Jazz
64	26.89	9.41	4.89	3.12	1.73	1.47	2.22	52.90
IND
Indiana Pacers
65	26.67	10.83	4.47	1.81	1.26	1.37	2.68	51.58
WAS
Washington Wizards
64	26.17	10.83	5.02	2.16	1.32	1.19	2.56	51.67
SAC
Sacramento Kings
63	25.84	10.20	4.75	2.44	1.43	0.89	3.18	48.99
DAL
Dallas Mavericks
64	25.49	10.73	4.70	2.29	1.52	0.94	2.81	49.99
CHA
Charlotte Hornets
64	25.16	10.92	5.03	2.39	1.38	1.11	2.89	50.39
DET
Detroit Pistons
63	24.92	9.86	4.21	2.40	1.51	1.14	2.28	48.74
ATL
Atlanta Hawks
64	24.89	10.36	4.66	2.66	1.51	1.27	2.22	50.43
PHO
Phoenix Suns
64	24.57	9.64	3.58	2.33	1.68	1.03	2.58	47.06
LAL
Los Angeles Lakers
66	24.38	9.74	4.53	2.72	1.28	1.02	2.52	47.24
TOR
Toronto Raptors
64	24.37	10.44	4.41	2.59	1.29	1.22	2.41	48.63
CHI
Chicago Bulls
64	24.05	11.10	4.00	2.63	1.31	1.32	2.68	48.58
MIL
Milwaukee Bucks
65	23.91	10.16	3.73	2.80	1.23	1.23	2.50	46.58
NYK
New York Knicks
64	23.90	9.04	4.35	2.83	1.23	1.01	2.77	45.22
GSW
Golden State Warriors
63	23.80	10.77	4.67	2.37	1.50	1.03	2.57	48.75
HOU
Houston Rockets
64	23.60	10.60	4.12	2.13	1.39	1.55	2.75	48.57
OKC
Oklahoma City Thunder
64	23.28	10.74	4.22	2.15	1.32	1.04	2.98	46.60
MEM
Memphis Grizzlies
65	23.22	10.59	4.04	2.50	1.50	1.16	3.10	46.87
NOR
New Orleans Pelicans
64	23.09	10.78	3.92	2.30	1.08	1.34	2.47	46.70
DEN
Denver Nuggets
64	23.01	10.17	4.05	2.07	1.25	1.12	2.01	46.39
POR
Portland Trail Blazers
63	22.99	9.76	4.45	2.09	1.47	1.28	2.97	46.66
SAS
San Antonio Spurs
64	22.99	10.49	4.65	2.40	1.36	1.00	2.64	46.99
MIA
Miami Heat
64	22.75	9.87	4.51	2.33	1.30	1.07	2.81	45.66
PHI
Philadelphia 76ers
64	22.60	11.60	4.28	2.17	0.95	1.38	2.81	47.12
BKN
Brooklyn Nets
65	22.31	10.54	4.25	2.19	1.11	0.92	2.57	44.85
CLE
Cleveland Cavaliers
64	22.09	10.01	4.03	2.24	1.28	1.09	2.42	44.84
LAC
Los Angeles Clippers
63	21.91	10.37	4.63	2.06	1.33	1.19	2.53	46.33
MIN
Minnesota Timberwolves
65	21.36	9.20	3.29	2.09	1.23	1.13	2.36	42.06
ORL
Orlando Magic
65	21.14	9.66	3.76	1.90	1.24	1.01	2.82	42.30
BOS
Boston Celtics
63	20.21	9.94	3.98	2.22	1.04	0.81	2.02	41.64"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed