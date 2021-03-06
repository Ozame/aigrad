# Thesis Notes
- Author Samu Kumpulainen
- Notes, and stuff for the thesis

## About

The Current State of Artificial General Intelligence

This is a memo for all the things I’ll need to save for the master’s thesis, aka
Big G. Everything is bound to change. The current plan I’ve discussed with Vagan
is that one option for the thesis focusing on the AGI would be an overview
literary review about the topic, using the top journals (Jyfu levels 2-3) that
specialize in AGI. For now, I have the following three-tiered plan:
1. Achieve general overview of the field.
2. Focus on one specific sub-field, such as generalization efforts.
3. Produce a demo or pilot of some kind, for example an application of an
   existing model, or try a proven solution in a somehow different application
   (generalization). Advancing in order, these levels are based on the previous
   ones, and each step (with the previous one) could work as a topic of the
   thesis. The higher levels will prove more difficult, and just staying in
   levels 1-2 would be maybe preferred. However, if something interesting comes
   up during the research, I’ll also consider focusing on that. For now, I’ll
   proceed on the first step.

Method-wise this would mean:
1. Systematic literature mapping: overview
2. Systematic literature review: focused literature review
3. Design research(?): application on the area

## Current Goals:
-> Proposal ok, journal option #1 goal, conference papers included!

1.  Dive deeper on the journal based option, which journals would it be, how
    would they be ranked, number of material, date range etc.
    - 3 journals plus 1 conference collection -> ~1000 articles, should provide
      enought material
2. How to proceed? Figure out the process better.  
3.  Also find sources for the background chapters
   - AGI & its history, definition
   - Method


### Possible research Questions (?)
1. **How much, and what type of research is done in the field of AGI?**
      - What is the current state of AGI research? -> How much research is done
        in recent years? What is the overall trend (interest growth/decline)? 
      - What type of research it is (research methods, types)
2.  **Where is the AGI research focused on?**
    - This includes
       - topics
       - techniques
       - technology
    - What are the current techniques (and topics) used and researched?
    - How the research is focused on the field? 
    - *(How it has changed over time? Can this be observed on such short time)*
3. **Has there been any major breakthroughs?**
    - What have been the most successful attempts?
4. **Where and when were the studies published?**
    - Time
    - Journal

5. How has the generalization of specific techniques advanced recently? (Should
   this be the main focus, or left out? Based on my opponent, more focused topic
   would be better. This one also doesn't fit in with the others.)

RQ->PICO->keywords->search terms->dataset->inclusion/exclusion->...

## Notes

### Ideas
- What about: sysmap if whole gai field, sysrev, describing sysrev or something,
  if just generalization or other subtopic. OR a complementary approach of
  these??
- Googles bubble chart?
  https://developers.google.com/chart/interactive/docs/gallery/bubblechart 

- RQX: AGI testing - which tests (wozniak, nilsson) are popular?
- TODO: GS citation count, easy with python script (search name, take count)
  - On the other hand :/, citation counts variability betweeen search engines
    differs, is this something that could be just stated, justifying e.g. GS's
    wide usage, or something similar? Or just count means or something :D

### Journals
Publication Forum, Julkaisufoorumi, ranks the journals, with 1-3, 3 being the
top quality journal. (https://www.tsv.fi/julkaisufoorumi/haku.php?lang=en)

- Artificial Intelligence (3)
  https://www.journals.elsevier.com/artificial-intelligence
    - Best AI journal, whole field of AI. Useful, but not specific
- Journal of Artificial Intelligence Research (3)
  https://www.jair.org/index.php/
    - All areas of AI. Open Access. Not Specific
- Journal of Artificial General Intelligence (1)
  https://content.sciendo.com/configurable/contentpage/journals$002fjagi$002fjagi-overview.xml
    - Owned by AGIS
    - Only level 1, which prolly has to do with the fact it’s really specific

Which journals are good? Only 2 of level 3 journals on any AI field

- International conference on AGI: https://link.springer.com/conference/agi
  Conference papers collected each year !!

CHECK IEEE, SCHOLAR

### Books

- Heuristics: Intelligent search strategies for computer problem solving (Pearl)
- The book of why (Pearl)
- B Artificial intelligence : a modern approach (Norvig)
- AGI (Goertzel, Pennachin)
  https://web.archive.org/web/20130320184603/http://people.inf.elte.hu/csizsekp/ai/books/artificial-general-intelligence-cognitive-technologies.9783540237334.27156.pdf


### People:
- Goertsel
- Nilson 
- Norvig
- Ben Goertsel and others -> AGI community

Check Kopernio,  scholar for papers!


### Artificial General Intelligence

- General roadmaps developed by community (S. Adams et al)
- AGIS - http://www.agi-society.org/ (seems dead since 2015)

- The Wozniak test
- Transfer learning

## Research Method


Tips from Ville Isomöttonen: Either systematic mapping study, which is more
common in MTs, or systematic literature review, maybe more specific,
descriptive?. The following finnish material is from the IT Research Methods
lecture slides:

### Kuvaileva kirjallisuuskartoitus - Descriptive litrev
- Yleiskatsaus, rakentaa kokonaiskuvaa tietystä asiakokonaisuudesta
- Aineistot laajoja, aineiston valintaa eivät rajaa tiukat metodiset säännöt. 
- Tutkittava ilmiö pystytään kuvaamaan laaja-alaisesti ja tarvittaessa
  luokittelemaan tutkittavan ilmiön ominaisuuksia. 
- Tutkimuskysymykset ovat väljempiä kuin systemaattisessa katsauksessa tai
  meta-analyysissä. 
- Kuvaileva katsaus toimii itsenäisenä metodina, mutta se myös tarjoaa uusia
  tutkittavia ilmiöitä systemaattista kirjallisuuskatsausta varten.
- Kaksi hieman erilaista orientaatiota: narratiivinen ja integroiva katsaus.
- Narratiivinen yleiskatsaus tiivistää aiempia tutkimuksia, analyysin muoto on
  kuvaileva synteesi, jonka yhteenveto on ytimekäs ja johdonmukainen. 
- Integroiva katsaus (IK) kuvaa tutkittavaa ilmiötä mahdollisimman
  monipuolisesti. 
- IK auttaa kirjallisuuden tarkastelussa, kriittisessä arvioinnissa ja
  syntetisoinnissa. Verrattuna systemaattisen katsaukseen integroiva katsaus
  tarjoaa selvästi laajemman kuvan aihetta käsittelevästä kirjallisuudesta
- IK yhdistää narratiivista ja systemaattista katsausta metodiseksi jatkumoksi
  ### Systemaattinen kirjallisuuskartoitus - Systematic literature mapping
- Antaa selkeästi vastauksen tiettyyn kysymykseen/ratkaisun ongelmaan.
- Analyyttinen ja objektiivinen tiivistelmä aiheen aiempien merkittävien
  tutkimusten oleellisesta sisällöstä. 
- Kiinnitetään huomiota kirjallisuuden hakutekniikkaan ja lähteiden keskinäiseen
  loogiseen yhteyteen
- Käytetyt hakukoneet ja tietokannat, hakusanat, karsinta (operandit) ym.
- Etsitään kirjallisuutta, johon tietyssä lähdemateriaalissa on viitattu
- Etsitään kirjallisuutta, joka viittaa tiettyyn lähdemateriaaliin.
- Tietotekniikan opinnäytetöissä (gradut) ei yleensä raportoida
  kirjallisuushakujen yksityiskohtia, ellei haluta korostaa jonkin asian olevan
  erityisen vähän/paljon tutkittua tai metodi on systematic mapping study.
  Yleisin tapa pro gradu -tutkielmissa. Kuvaileva kartoitus on myös hyvä, mikäli
  aihe sopii siihen paremmin kuin systemaattiseen kartoitukseen.
  Meta-analyysinkin voi tehdä, mutta on harvinaisempi pro gradu -tutkielmissa.

There is also other styles of litrev mentioned in the lecture slides,
qualitative meta-analysis (meta synthesis, classification, summary) and
quantitative meta-analysis( statistical approach), but they might not be so
ideal for this topic (?).

### Literature review process
1. Forming research problem and research questions (idea to goal)
2. Specifying the goal (limiting the topic, decide on the viewpoint)
3. Literature search
    - DB/search engines/search terms/time interval/publication type/logical
      operands
4. Literature review about the topic
5. Processing the lit found, choosing the material, forming the research
   results, reporting (also Fink model; Salminen 2011, s11. Fig 2: process
   model)

Each phase produces a subresult to be used in the next one. This process results
in a **systematic map of the area.** This can and should be further visualized
using for example **bubblegraphs or heatmaps** (Mononen 2018 and Petersen et al.
2008). This helps to more easily spot the **focus points and gaps** in the
research.


#### Some references on the litrev methods:
- Webster, J. & Watson, R.T. (2002). Analyzing the past to prepare for the
  future: Writing a literature review. MIS Quarterly 26(2), 13-23.
- Salminen, Ari. Mikä kirjallisuuskatsaus? Johdatus kirjallisuuskatsauksen
  tyyppeihin ja hallintotieteellisiin sovelluksiin. Vaasan yliopiston
  julkaisuja. Opetusjulkaisuja 62, Julkisjohtaminen 4. (2011).
  www.uva.fi/materiaali/pdf/isbn_978-952-476-349-3.pdf
- Brereton, P., Kitchenham, B., Budgen, D., Turner, M. & Khalil, M. (2007).
  Lessons from applying the systematic literature review process within the
  software engineering domain. The Journal of Systems and Software 80, 571-583.
- Kitchenham et al. (2010). Systematic literature reviews in software
  engineering – A tertiary study. Information and Software Technology 52(8),
  792–805.
- Bandara, W., Fuertmueller, E., Gorbacheva, E., Miskon, S. & Beekhuyzen, J.
  (2015). Achieving Rigor in Literature Reviews: Insights from Qualitative Data
  Analysis and Tool-Support. Communications of the Association for Information
  Systems 37(1), 154 - 204. Available at:
  http://aisel.aisnet.org/cais/vol37/iss1/8

These ones are the ones recommended by Isomöttönen:
- Petersen, K., Feldt, R., Mujtaba, S., & Mattsson, M. (2008, June). Systematic
  mapping studies in software engineering. In Ease (Vol. 8, pp. 68-77).
- Petersen, K., Vakkalanka, S., & Kuzniarz, L. (2015). Guidelines for conducting
  systematic mapping studies in software engineering: An update. Information and
  Software Technology, 64, 1-18.

Also check on the thesis’ of Niko Mononen, Sari Ryynänen and Mari Kasanen from
JYX:

- Mononen, Niko. 2018. ”Systemaattinen kirjallisuuskartoitus luovasta
  ohjelmoinnista ope- tuskontekstissa”. Master’s thesis.
  http://urn.fi/URN:NBN:fi:jyu-201801281
350.

- Ryynänen, Sari. 2017. ”Immateriaalioikeuksien esiintyminen
  SIGCSE-konferenssien julka- isuissa”. Master’s thesis.
  http://urn.fi/URN:NBN:fi:jyu-201705112298.

- Wieringa et al. 2006 -> classification schema??


## Thesis structure

1. Introduction
2. AGI-explanation chapter
    - What?
    - Background/history summary
3. Method explanation
    - Process
    - Differences from other secondary studies
    - In IT-field
4. The implementation/process
    - Background
    - Research questions
    - Sources (search terms, databases, search engines)
    - Criteria 
    - Source Control
5. Results & Analysis
    - What was found
    - Graphs, numbers, most used, least used keywords
6. Thoughts
    - About the results
    - Possible future research topics based on findings

- Bibliography
- Appendix
    - Table of sources: year, name, authors, type, keywords


Some Information (in finnish): 
  http://users.jyu.fi/~santanen/info/kirjoittamisesta.html


## Data Management
- Mononen used sqlite db to save data about articles and their criteria info
- Excel?
- Python: matplotlib?



## Criteria

- publication range 5+ years, 2015-2019, to limit material?
- free to access
- digital
- no books
- english
- abstract (or quick skimming) shows the article is about AGI


## Search terms

### See excel for search terms trials
### Possible keywords
- AGI
- AI
- artificial intelligence
- general artificial intelligence & artificial general intelligence
- superintelligence?
- computer science
- strong ai
- success, advances, development, breakthrough
- turing test

## Guidance sessions

### Gohjaus 13.10.2020 (SK,VT)
- Having a comprehensive history chapter is good.
- Having a separate section about method's usage in IT might be ok, but rather
    combine it with other sections.
  - Combine it with reasoning section and place in chapter 3.
    - In the end discussion see how the method choice worked out
- Being "a journalist" looking into AGI. Own vision?
- How AGI research is related to current trends?
  - Quantative DL is not the solution 
  - Self-inputting neural networks
  - GANs and fast learning, evolving
- Historical comparison
  - AGI papers now vs. 20 years ago would be nice, but in thesis scope not
    feasible.
  - trends over time
  - critics and suggestions
- Business potential in the AGI research?
- **International joint conference on AI** would be good to include.
- Using citation count, popularity etc. in search? Might not be good in this
  method, as overview is the goal. 

- TODO: Check usage of term _strong ai_, might require more precise definition







#############################################################

## Analysis

### History of AI


- Asimov's stories in 40s inspired others
- 1950s into academia
  - Alan Turing's test to measure machine intelligence
  - Minsky, McCarthy hosted *DSRPAI* summit in darthmouth in 56 => AI coined
  - Arthus Samuel's first checkers program, amateur challenged
- Summer
  - ELIZA, General Problem Solver (turing tested) -59
  - MIT AI lab founded by mccarthy and minsky
    - Hanoi -> funding
  - Minsky's interview -> 3-8 years
- Winter
  - Lighthill report 1973
    - Criticism about spending, questioning outlook -> defunded
    - UK all but few Unis' AI research 
- Fall
- Expert systems -> Deep Blue, chess 
    - ES requires formalization of problem
  - Learning is necessary
  - Neural networks
- Present
  - 2015 Alphago
  - NNs and deep learning form most of industrial AI today




#############################################################

## Paper notes

### Guideline update - petersen

- [Wieringa's
  classification](https://link.springer.com/article/10.1007/s00766-005-0021-6)
- combined with petersons guidelines
- Multiple sources for differences have been discussed, e.g. research question
  phrasing (open versus specific), scoping (where to draw the boundaries for the
  research area), restrictions on research types and methods (e.g. only
  including empirical work), time span, and exclusion of specific publication
  types (e.g. gray literature)
- PICO (Population, Intervention, Comparison and Outcomes) suggested by
  Kitchenham and Charters [1] was developed to identify keywords and formulate
  search strings from research questions.
- Backward snowball sampling
- Three new dimensions not highlighted by Petersen et al. [2] have been
  identified, namely **venue, study focus, and research method**. The study
  focus refers to the context being studied. Examples are distinctions between
  academic, industrial, government, project, and organization context. The venue
  is the type of publication venue (e.g. journal, conference, and workshop) as
  well as the concrete venues being targeted. The research method refers to the
  scientific method used, e.g. case study, experiment, or survey
- Existing categories or new ones that emerge from papers?
- validity threats reported?
- Search evaluation via test sets of papers (most common) etc.
- [58] good RQs:
    - what RQs in X are being addressed?
    - what original research exists in intersection of x and y?
    - what areas in x require more research?
- usually questions about the meta-level is included, like venues, methods etc.
- **Wohlin et al, 7, population representation over paper quantity <-> population not known beforehand**
- **Questions to think about regarding population:**
    - Are different a priori known sub-areas of the field covered?
    - Are the main publication forums specific to this area (e.g.
      conferences), or general software engineering forums (e.g. journals),
      represented when identifying relevant articles?
    - Are there explanations for major changes in the number of studies
        published per year? For example, this may point to new areas that
        should be added to classifications established earlier.
- Standards like SWEBOK, IEE, ISO useful in categorization
- The approaches identified (consult experts, iteratively improve the search,
  identify keywords from known papers, and use standards, encyclopedias, and
  thesaurus, see Table 5 and Fig. 7) are not highly time intensive and may
  greatly improve the quality of the search. Overall, such early quality
  assurance may save effort due to rework when mistakes were made in the early
  search activity. They may also help in focusing the search and hence reduce
  the noise, making the study selection process more time efficient.
- Incl/excl. criteria are important: Venue, language, focus etc. p11
- Finnish publication types: useful for classification and study selection.
- **Research types** and **research methods**
- Topic specific classification? Should be decided which would be more useful,
  emergent or an existing one?See petersen's keywords->classification
  scheme->categorize (not clear? portillo-rodriguez 20)
- 5.3 Mapping reporting guide
- rubrics: table 9-13 and table 8 activity ratio should be utilized on
  evaluation of process.

#### Guideline updates

##### Planning
  - All decisions about conduct are decided
  - Need identification and scoping
    - examine existing research activity
    - determine the value of full SLR
    - to summarize and disseminate research findings
    - to identify research gaps
  - Study identification (wohlin questions ^)
    - search strategy (manual, db, snowballing included?)
      - PICO,  standards
      - evaluation
      - inclusion/exclusion criteria
      - quality assesment(not common, but might be useful in some situations
  - Data extraction and classification
    - General vs topic dependant classification schemes
      - majority topic specific (emerging, existing)
        - usage of swebok and other standards?
        - emergent: categories -> categorization of papers
    - Venue, research type, research method facets
      - JUFO, wieringa's types
    - ??? is combining this possible?

##### Conducting
  - Implement planned mapping
  - Report all information on all stages
##### Reporting

### AI History - Haenlein, Kaplan

- 1950s into academia
- When ai hits mainstream, it's usually not considered as such anymore (magic
  disappears)
- AGI systems speculated here and there
- Spring
    - Asimov's stories in 40s inspired others
    - Turing's machine, turing test
    - Minsky, McCarthy hosted *DSRPAI* summit in darthmouth
- Summer
  - ELIZA, General Problem Solver (turing tested)
    - Hanoi -> funding
  - Minsky's interview -> 3-8 years
- Winter
  - Criticism about spending, questioning outlook -> defunded
- Fall
  - Expert systems -> Deep Blue
    - ES requires formalization of problem
  - Learning is necessary
  - Neural networks
- Present
  - 2015 Alphago
  - NNs and deep learning form most of industrial AI today

### AI History - Russell & Norvig Book

- Alan Turing
  - turing test
  - machine learning
  - Child Programme - simulate child's, not adult's mind
- Mccarthy's workshop in 1956
  - Logic Theorist program by Newell and Simon
  - The most prominent people met
- 1952-1969 early years
  - Proving machine capabilities
  - GPS by Newell, Simon
  - Arthur Samuel's checker programs
  - 1958 Mccharthy's accomplishments
    - Lisp
    - Time sharing
    - Advice Taker - hypothetical but complete AI system - GENERAL
  - Followed years of research into formal reasoning and logic
  - Work on neural networks also flourished
    - Building on McCulloch, Pitts and Hebb
      - Winograd & Cowan, Widrow, Block
- 1966-1973 realitys strikes back
  - 1954 Herbert Simon confident quote
  - Lighthill report 1973
    - combinatorial explosion
  - Problems:
    - limiting basic structures
    - difficulty of difficult problems
    - system not knowing what it was doing
  - Expert systems research 
    - Corporations involved
  - Fifth Gen project in Japan, MCC in USA 
  - AI winter hit because promises were not fulfilled
    - before this was a billion dollar boom
- Return of neural networks 1986-present
  - Back-propagation reinvented (og. 1969 Bryson and Ho)
- AI & Scientific method 1987-present
  - Experiment, analysis
  - Building on existing theories, less intuition, real world applications
  - NNs etc. used with other techniques
  - Judea Pearl & Bayesian networks, uncertain reasoning
    - normative expert systems, Horwitz and Heckerman 
  - Emerging of Agents
    - Newell, Laird, Rosenbloom => SOAR, intelligent agent architecture
    - Founders have been returning to roots
      - mccarthy: Human-Level AI
      - goertzel, pennachin: AGI
      - Yudkowsky, omohundro: Friendly AI?
  - Data beats algorithm:
    - Banko and Brill 2001
    - Hays and Efros 2007
    - ! Halevy er all 2009
- Ai in use everywhere, but like earlier, when it start to being used, maybe not
  thought to be AI anymore?

### Mappping the landscape of human level agi
Adams et al, 2012

- Builds on the previous literature on AI evaluation
- Builds a roadmap on the goals of AI, with milestones and example scenarios
  - Prior work e.g. Laird and Wray 2010 architecture requirements
- Presents modified set of environmental and architectural requirements for AGI.
  - Starting point for the community to build on.
- Different ways of defining human intelligence, piaget, vygotsky
- Effect of human sensory input and other competencies
- Scenarios offer way to keep all approaches open by not taking specifying the
  order in which the competences and capabilities are developed.
  - Video games, preschool, reading comprehension, story comprehension, school
    learning, the wozniak test
- Scenarios and the tasks, and how the agent is able to complete them, serves as
  a general way of measurement regarding the AGI development progress. E.g. is
  the system able to complete 25% or 80% of the given tasks tells immediately
  about the level of competence.



### From here to human-level AI
John McCarthy

- Two approaches to machine intelligence:
  - simulating mind
  - intelligent programs
- Bounded informatic situation vs common sense informatic situation
  - cs: approximate concepts, theories, nonmonotonic reasoning. What is relevant
    to situation?
- Limits of mathematical logic in expressing uncertainty and imprecision of
  humans
- Mt. Everest and welfare of a chicken
  - Trying to precisely define approximate concept is futile
- Elaboration tolerance
- Formalization of context, outer level concept 
- Event & action reasoning
- Introspection

McCarthy's article presents some challenges on the way of reaching HLAI. Some
have research and work to build upon, some are just in the beginning. Argues
that logical approach would be more useful than the one achieved via
computerized evolution.

### Human-Level Artificial Intelligence? Be Serious
Nils J. Nilsson

- Focus should be on building general AI that can learn.
  - Employment test
    - Opposition:
      - Physical tasks
      - hlai impossible, weak instead
      - political/economical opposition
- "Habile systems"
  - Instead of thousands of specialized systems, build ones that can be taught
- Child machines
  - Turing's "the child project" 1950
  - Core + outer layers
- Perception, reps, action hierarchies
- Prediction, planning
- Reinforcement learning (pos, neg responses)
- Language
  - trumps reinf. learning
- Which level to start? Infant, High School, College? Building on top of these
  might make the initial foundation easier to reach.


### Requirements engineering paper classification and evaluation criteria
Wieringa et al. 2006

**Useful as a classification facet**

- Need for criteria for different types of papers
- Engineering cycle: list of activities
  1. Problem investigation
  2. Solution design
  3. Solution validation
  4. Solution selection
  5. Solution implementation
  6. Implementation evaluation
->
- Proposed classification scheme 
  - Evaluation research
  - Validation research
  - Proposal of a solution
  - Philosophical papers
  - Opinion paperss
  - Experience papers
- Papers may belong to multiple classes, but point is to prevent wrong type of 
    evaluation based on wrong criteria.


