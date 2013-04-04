Daniel Alabi and Cody Wang
CS324: Data Mining
Data Summarization

First, we cleaned the data by removing the 2 columns that weren't attributes of a record 
in the data attributes: 24th and 41st columns. The data was initially stored in
census-income.data. After "cleaning", the result was stored in census-income-clean.data (not submitted).
Done in python. Check data-clean.py.

Second, we performed statistical analysis on the continuous features to determine
the mean, median, maximum, minimum, and the first and third quartiles. The data are shown
below. Done in python. 
Third, we determined the distinct values in each nominal feature and the number of times
the distinct values occur. Done in python. 
Check data-summarize.py

Fourth, we plotted each pair of continuous features using R. Check data-summarize.r for the code. 
Check plotfile.png for the result of the scatterplots.

1. How many records are there?
   199523

2. How many attributes are there?
   40

3. How many attributes are continuous? Nominal?
   7; 33.

4. For the continuous features, what are the average, median, maximum, and minimum values? What are the first and third quartiles (also known as the 25th and 75th percentiles)?

   Feature| age       wage/hour      captialgains     capitallosses    dividendsfromstocks 	numpersonsworkedforemployer	   weeksworkedinayea
   ====================================================================================================================
   Average| 34.494198663813194 55.426908175999756 434.71898979065071 37.313788385298935  197.52953293605248   1.9561804904697704   23.174897129654227
   Median|  33.0  0.0  0.0  0.0  0.0 1.0 8.0
   Max|	    90.0  9999.0  99999.0   4608.0   99999.0  6.0  52.0
   Min|     0	  0	  0	    0	     0	      0	   0
   1st quartiles| 15.0	  0.0	    0.0	     0.0      0.0  0.0	0.0
   3rd quartiles| 50.0	  0.0	    0.0	     0.0      0.0  4.0	52.0





5. For the nominal features, what are the distinct values, and how
many times do they appear?

classofworker 
---------------------
distinctvalue	count
---------------------

Self-employed-incorporated 3265
State government 4227
Private 72028
Federal government 2925
Self-employed-not incorporated 8445
Not in universe 100245
Never worked 439
Local government 7784
Without pay 165



detailedindustryrecode
---------------------
distinctvalue	count
---------------------

28 143
22 952
29 4209
49 610
24 1503
25 1084
26 127
27 626
20 32
21 559
48 652
23 525
46 187
47 1644
44 2549
45 4482
42 4683
43 8283
40 1651
41 3964
1 827
0 100684
3 563
2 2196
5 553
4 5984
7 422
6 554
9 993
8 550
10 4
13 899
38 1629
11 1764
51 36
39 2937
12 1350
15 452
14 295
17 157
16 539
19 1346
32 3596
31 1178
30 1181
37 4022
36 945
35 3380
34 2765
33 17070
18 483
50 1704



detailedoccupationrecode
---------------------
distinctvalue	count
---------------------

28 1661
43 1382
24 1847
25 767
26 7887
27 780
20 71
21 533
22 411
23 3392
46 36
44 1592
45 172
42 1918
29 5105
40 617
41 1592
1 544
0 100684
3 3195
2 8756
5 855
4 1364
7 731
6 441
9 738
8 2151
39 1017
38 3003
11 637
10 3683
13 1271
12 3340
15 815
14 932
17 1771
16 3445
19 5413
18 1083
31 2699
30 1897
37 2234
36 4145
35 3168
34 4025
33 3325
32 2398

education
---------------------
distinctvalue	count
---------------------

1st 2nd 3rd or 4th grade 1799
Masters degree(MA MS MEng MEd MSW MBA) 6541
Some college but no degree 27820
7th and 8th grade 8007
Less than 1st grade 819
9th grade 6230
11th grade 6876
Bachelors degree(BA AB BS) 19865
Doctorate degree(PhD EdD) 1263
Prof school degree (MD DDS DVM LLB JD) 1793
5th or 6th grade 3277
Associates degree-occup /vocational 5358
High school graduate 48407
10th grade 7557
Children 47422
12th grade no diploma 2126
Associates degree-academic program 4363

enrollineduinstlastwk
---------------------
distinctvalue	count
---------------------

High school 6892
Not in universe 186943
College or university 5688

marital stat
---------------------
distinctvalue	count
---------------------

Separated 3460
Widowed 10463
Divorced 12710
Married-civilian spouse present 84222
Married-spouse absent 1518
Married-A F spouse present 665
Never married 86485



major industry code
---------------------
distinctvalue	count
---------------------

Public administration 4610
Entertainment 1651
Hospital services 3964
Manufacturing-durable goods 9015
Business and repair services 5651
Social services 2549
Utilities and sanitary services 1178
Mining 563
Transportation 4209
Medical except hospital 4683
Retail trade 17070
Construction 5984
Personal services except private HH 2937
Manufacturing-nondurable goods 6897
Private household services 945
Communications 1181
Armed Forces 36
Wholesale trade 3596
Finance insurance and real estate 6145
Not in universe or children 100684
Forestry and fisheries 187
Other professional services 4482
Education 8283
Agriculture 3023





major occupation code
---------------------
distinctvalue	count
---------------------

Protective services 1661
Other service 12099
Armed Forces 36
Private household services 780
Professional specialty 13940
Sales 11783
Not in universe 100684
Farming forestry and fishing 3146
Machine operators assmblrs & inspctrs 6379
Transportation and material moving 4020
Handlers equip cleaners etc 4127
Technicians and related support 3018
Precision production craft & repair 10518
Adm support including clerical 14837
Executive admin and managerial 12495





race
---------------------
distinctvalue	count
---------------------

Asian or Pacific Islander 5835
White 167365
Other 3657
Black 20415
Amer Indian Aleut or Eskimo 2251




hispanic origin
---------------------
distinctvalue	count
---------------------

Cuban 1126
Mexican-American 8079
Other Spanish 2485
Chicano 304
Mexican (Mexicano) 7234
Do not know 306
Central or South American 3895
Puerto Rican 3313
NA 874
All other 171907






sex
---------------------
distinctvalue	count
---------------------

Male 95539
Female 103984




member of a labor union
---------------------
distinctvalue	count
---------------------

Yes 3030
Not in universe 180459
No 16034




reason for unemployment
---------------------
distinctvalue	count
---------------------

Job loser - on layoff 976
Job leaver 598
Not in universe 193453
New entrant 439
Other job loser 2038
Re-entrant 2019



full or part-time employment stats
---------------------
distinctvalue	count
---------------------

PT for econ reasons usually FT 525
Children or Armed Forces 123769
Not in labor force 26808
Full-time schedules 40736
PT for econ reasons usually PT 1209
PT for non-econ reasons usually FT 3322
Unemployed part- time 843
Unemployed full-time 2311




tax filer stat
---------------------
distinctvalue	count
---------------------

Nonfiler 75094
Joint both 65+ 8332
Joint both under 65 67383
Single 37421
Joint one under 65 & one 65+ 3867
Head of household 7426



Region of previous residence
---------------------
distinctvalue	count
---------------------

Northeast 2705
West 4074
Not in universe 183750
Midwest 3575
Abroad 530
South 4889




state of previous residence
---------------------
distinctvalue	count
---------------------

Mississippi 204
Oklahoma 626
Wyoming 241
Minnesota 576
Illinois 180
Arkansas 205
North Carolina 812
Indiana 533
Maryland 136
Louisiana 192
Texas 209
Arizona 243
Iowa 189
Michigan 441
Kansas 149
Utah 1063
Virginia 126
Oregon 236
Connecticut 117
Montana 226
California 1714
Massachusetts 151
West Virginia 231
South Carolina 95
New Hampshire 242
Abroad 671
? 708
Wisconsin 105
Vermont 191
Georgia 227
North Dakota 499
Pennsylvania 199
Florida 849
Alaska 290
Kentucky 244
Nebraska 178
Missouri 175
Ohio 211
Alabama 216
New York 195
South Dakota 138
Colorado 239
Idaho 31
New Jersey 75
Not in universe 183750
Tennessee 202
District of Columbia 116
Nevada 174
Delaware 73
Maine 167
New Mexico 463




detailed household and family stat
---------------------
distinctvalue	count
---------------------

Other Rel 18+ spouse of subfamily RP 638
Child 18+ ever marr Not in a subfamily 1013
Child <18 spouse of subfamily RP 2
In group quarters 196
Grandchild <18 never marr not in subfamily 1066
Grandchild <18 ever marr not in subfamily 2
Other Rel 18+ never marr not in subfamily 1728
Grandchild <18 never marr child of subfamily RP 1868
Grandchild 18+ never marr not in subfamily 375
Grandchild 18+ ever marr RP of subfamily 9
Other Rel <18 spouse of subfamily RP 3
Nonfamily householder 22213
Child 18+ spouse of subfamily RP 126
Spouse of householder 41695
Grandchild 18+ never marr RP of subfamily 6
Grandchild 18+ spouse of subfamily RP 10
Child <18 never marr not in subfamily 50326
Secondary individual 6122
Other Rel <18 ever marr not in subfamily 1
Other Rel 18+ ever marr not in subfamily 1956
Grandchild <18 never marr RP of subfamily 2
Child <18 never marr RP of subfamily 80
Other Rel <18 never marr child of subfamily RP 656
Other Rel <18 never marr not in subfamily 584
RP of unrelated subfamily 685
Child <18 ever marr RP of subfamily 9
Householder 53248
Other Rel 18+ ever marr RP of subfamily 656
Child 18+ never marr Not in a subfamily 12030
Child under 18 of RP of unrel subfamily 732
Spouse of RP of unrelated subfamily 52
Child 18+ never marr RP of subfamily 589
Child 18+ ever marr RP of subfamily 671
Other Rel 18+ never marr RP of subfamily 94
Other Rel <18 ever marr RP of subfamily 6
Child <18 ever marr not in subfamily 36
Grandchild 18+ ever marr not in subfamily 34
Other Rel <18 never married RP of subfamily 4




detailed household summary in household
---------------------
distinctvalue	count
---------------------

Child under 18 never married 50426
Child under 18 ever married 47
Spouse of householder 41709
Nonrelative of householder 7601
Child 18 or older 14430
Group Quarters- Secondary individual 132
Householder 75475
Other relative of householder 9703




migration code-change in msa
---------------------
distinctvalue	count
---------------------

Abroad to nonMSA 73
MSA to MSA 10601
Not in universe 1516
Nonmover 82538
MSA to nonMSA 790
Abroad to MSA 453
NonMSA to nonMSA 2811
Not identifiable 430
? 99696
NonMSA to MSA 615



migration code-change in reg
---------------------
distinctvalue	count
---------------------

Different division same region 465
Same county 9812
Different region 1178
Not in universe 1516
Nonmover 82538
Different county same state 2797
Different state same division 991
Abroad 530
? 99696



migration code-move within reg
---------------------
distinctvalue	count
---------------------

Different state in South 973
Same county 9812
Different state in Northeast 431
Different state in Midwest 551
Not in universe 1516
Nonmover 82538
Different county same state 2797
Different state in West 679
Abroad 530
? 99696




live in this house 1 year ago
---------------------
distinctvalue	count
---------------------

Not in universe under 1 year old 101212
Yes 82538
No 15773



migration prev res in sunbelt
---------------------
distinctvalue	count
---------------------

Yes 5786
Not in universe 84054
? 99696
No 9987


family members under 18
---------------------
distinctvalue	count
---------------------

Mother only present 12772
Neither parent present 1653
Father only present 1883
Not in universe 144232
Both parents present 38983




country of birth father
---------------------
distinctvalue	count
---------------------

Canada 1380
Dominican-Republic 1290
Italy 2212
Ireland 508
Panama 25
Laos 154
Scotland 247
Cambodia 196
France 191
Peru 335
Iran 233
Thailand 107
Ecuador 379
Columbia 614
Cuba 1125
Guatemala 445
Germany 1356
China 856
Haiti 351
Hong Kong 106
Poland 1212
? 6713
Holand-Netherlands 51
Philippines 1154
Vietnam 457
Hungary 306
Honduras 194
Taiwan 199
Jamaica 463
England 793
Portugal 388
Mexico 10008
El-Salvador 982
India 580
Puerto-Rico 2680
Outlying-U S (Guam USVI etc) 159
Yugoslavia 217
United-States 159163
Trinadad&Tobago 113
Greece 344
Japan 392
South Korea 530
Nicaragua 315


country of birth mother
---------------------
distinctvalue	count
---------------------

Canada 1451
Dominican-Republic 1103
Italy 1844
Ireland 599
Panama 32
Laos 155
Scotland 241
Cambodia 157
France 212
Peru 355
Iran 198
Thailand 123
Ecuador 375
Columbia 612
Cuba 1108
Guatemala 444
Germany 1382
China 760
Haiti 353
Hong Kong 107
Poland 1110
? 6119
Holand-Netherlands 49
Philippines 1231
Vietnam 473
Japan 469
Honduras 218
South Korea 609
Jamaica 453
England 903
Portugal 342
Mexico 9781
El-Salvador 1108
India 581
Puerto-Rico 2473
Outlying-U S (Guam USVI etc) 157
Yugoslavia 177
United-States 160479
Trinadad&Tobago 99
Greece 261
Hungary 297
Taiwan 222
Nicaragua 301




country of birth self
---------------------
distinctvalue	count
---------------------

Canada 700
Dominican-Republic 690
Italy 419
Ireland 135
Panama 28
Laos 105
Scotland 75
Cambodia 95
France 121
Peru 268
Iran 157
Thailand 113
Ecuador 258
Columbia 434
Cuba 837
Guatemala 344
Germany 851
China 478
Haiti 228
Hong Kong 100
Poland 381
? 3393
Holand-Netherlands 23
Philippines 845
Vietnam 391
Japan 339
Honduras 144
South Korea 471
Jamaica 320
England 457
Portugal 174
Mexico 5767
El-Salvador 689
India 408
Puerto-Rico 1400
Outlying-U S (Guam USVI etc) 119
Yugoslavia 66
United-States 176989
Trinadad&Tobago 66
Greece 147
Hungary 79
Taiwan 201
Nicaragua 218



citizenship
---------------------
distinctvalue	count
---------------------

Native- Born abroad of American Parent(s) 1756
Foreign born- Not a citizen of U S 13401
Foreign born- U S citizen by naturalization 5855
Native- Born in the United States 176992
Native- Born in Puerto Rico or U S Outlying 1519

own business or self-employed
---------------------
distinctvalue	count
---------------------

1 2698
0 180672
2 16153


fill inc questionnaire for veteran's admin
---------------------
distinctvalue	count
---------------------

Yes 391
Not in universe 197539
No 1593




veterans benefits
---------------------
distinctvalue	count
---------------------
1 1984
0 47409
2 150130



year
---------------------
distinctvalue	count
---------------------
95 99696
94 99827




6. For the numeric features, use R to make 2-dimensional scatter plots
of two features at a time (some sample code is at the end of this assignment).

Check data-summarize.r for the code. 
Check plotfile.png for the result of the scatterplots.



7. Extra problem:
We used R to make the scatterplot of weeks worked in year against age. 
We found the following relationship between the two variables:
From the dense scatterplot of age against weeks worked in year, we see
that there is at least one person of any age between ~18 and 80 that
work for hours between 0 and 50 hours. That is, even the old (80 years) still have to
work.

Check "age vs. weeks worked in year.pdf" for the scatterplot.



