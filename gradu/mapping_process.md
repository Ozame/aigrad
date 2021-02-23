# Systematic literature mapping - AGI

This document describes the process of systematic mapping. Notes, decision
descriptions etc. will be stored here during the study.

- As search is performed within journal/conference issues, missing papers in
  sense is not possible, if the issues truly cover the field (wohlin samplesize)
- If initial papers from journals are searched automatically instead of manual
  search, missing papers is possible.

## Research questions
- Derived from the research goal: Overview of the field.
- Using PICO here might help? 

## Search 

- Might have to use combination of manual and automatic search, 
  as searching through all material by hand is not feasible, but also might not be possible to find everything by automatic searches.

### How to search different venues

#### Artificial Intelligence
- https://www.journals.elsevier.com/artificial-intelligence/
- https://www-sciencedirect-com.ezproxy.jyu.fi/journal/artificial-intelligence

- Either use search on above link, or limit scopus there:
  - https://www-scopus-com.ezproxy.jyu.fi/results/results.uri?sort=plf-f&src=s&nlo=&nlr=&nls=&sid=2924507b14c32f4fb64d46114d17cf1a&sot=a&sdt=cl&cluster=scoexactsrctitle%2c%22Artificial+Intelligence%22%2ct&sl=17&s=SOURCE-ID+%2823675%29&origin=resultslist&zone=leftSideBar&editSaveSearch=&txGid=e389835a97e9acafe2c9e8543eaa4fe1
- Automatic search should be performed, is viable

#### Journal of artificial intelligence research
- https://www.jair.org/index.php/jair
- scopus: https://www-scopus-com.ezproxy.jyu.fi/sourceid/24330?origin=resultslist

- Scopus search possible, doable manually but would be easier

#### Journal of artificial general intelligence
- https://content.sciendo.com/view/journals/jagi/jagi-overview.xml?language=en

- Very little material, manual search preferred

#### International conference on artificial general intelligence
- https://link-springer-com.ezproxy.jyu.fi/conference/agi 
- Many papers, manual search viable, automatic good as well (springer)

#### International joint conference on artificial intelligence
- scopus https://www-scopus-com.ezproxy.jyu.fi/results/results.uri?sort=plf-f&src=s&st1=International+joint+conference+on+artificial+intelligence&nlo=&nlr=&nls=&sid=a09ad57cfa20f5f9c12f2be1afbe370a&sot=b&sdt=cl&cluster=scoexactsrctitle%2c%22Ijcai+International+Joint+Conference+On+Artificial+Intelligence%22%2ct&sl=67&s=SRCTITLE%28International+joint+conference+on+artificial+intelligence%29&origin=resultslist&zone=leftSideBar&editSaveSearch=&txGid=b1a476ec5cf5e0fa8ebb000d88c5fe3b

- automatic search via scopus. Very little articles of interest

##### See search results in the excel files 

- Need to justify the journal choice in general, why not just do the general search?
- Focusing only on the most relevant journals, as the goal is to map the AGI not
  it's relation to the other ai research (altho this is a plus)
- Target papers are topically relevant and high ranking.
- AIJ, JAIR, IJCAI were possible to search through via scopus, JAGI manually,
  ICAGI with springer 
    - TODO: Get exact internal search strings (at least from scopus)

  **Excel files:**
  - search_terms = preliminary search term testing on different databases.
  - material_search = Scopus and sciendo papers.
  - ICAGI = ICAGI conference papers exported via proquest, only names and links
  - scopus_ai_jair_ijcai = Aforementioned articles, exported from scopus, good info
  - articles_combined = results from the scraping script, which gets more info
    on the papers from their springer-link pages. Also other papers 
    **!PRONE TO CHANGE!**
  - final_results = the working file, should be kept clean and safe. Has all the
    articles and will be used in the mapping process.


- **Should cognitive architechture related papers be alway included?**
  - Many such papers don't always directly mention AGI or HLAI, but are still related in a way... E.g. Micropsi, and especially OpenCog. 

###### Terms mentioned often, possible keywords
- Symbolic/subsymbolic 
- Cognitive architectures
- NARS
- OpenCog
- AGI safety
- AIXI?
- Universal induction & Solomonoff induction 


Initial search yielded total of 187 papers. After first phase of inspection, 122
were considered potential. They were further examined in the second phase, where
the inclusion criteria was further considered.  

Remember to note how many were excluded for being duplicates or reporting same
thing (2).

(Initially on the second phase, 104 papers were directly accepted, and 18 further
excluded. Out of the inspected 122 potential papers, 17 were borderline cases
that had to be carefully decided. Out of those, 9 were excluded and 8 included.
However, everything was looked through more thoroughly to further exclude
papers.)

In the second phase, 122 potential papers were examined more thoroughly to
further exclude the less topical papers. Most of the papers could be accepted
based on the title or abstract alone, but in many cases inspection of
introduction and conclusion sections was required. After preliminary inspection,
small set of papers with their inclusion status was sent to the thesis councilor
to confirm the selection. During the second phase it became apparent that having
such a broad topic would raise the amount of relevant papers to very high
number. In the end 93 papers were included, and would be further analysed in the
next phase.

Also, could be important to mention that some papers relating to mentioned
systems were excluded because of the criteria.

### Example papers and some questions

>The search results can be seen in the spreadsheet file "final_results.xlsx"
>found in the material-directory. Here examples are each presented  with
>spreadsheet number, title, link, and reasoning behind decision.

**|#| Title | Link | Reasoning |**

#### **Accepted papers**

|6|*AGI safety literature review*|[Scopus](https://www.scopus.com/inward/record.uri?eid=2-s2.0-85055692095&doi=10.24963%2fijcai.2018%2f768&partnerID=40&md5=49cfad723b47562b085cc806e7337cc3)| Clearly relates to AGI|

|24|*Towards General Evaluation of Intelligent Systems: Lessons Learned from Reproducing AIQ Test Results*
|[Sciendo]([Sciendo](https://doi.org/10.2478/jagi-2018-0001))| Clearly relates to AGI agents|

|100|*A Formal Model of Cognitive Synergy*|[Springer Link](http://link.springer.com/chapter/10.1007/978-3-319-63703-7_2)|Presented Cognitive Architecture is related to general intelligences, AGI design|

#### **Not accepted papers**

|84|*Instrumental Properties of Social Testbeds*|[Springer Link](http://link.springer.com/chapter/10.1007/978-3-319-21365-1_11)|Focuses on social intelligence, and even though AGI is mentioned (once), the subject isn't related to it later on.|

|152|*Lifelong Learning Starting from Zero*|[Springer Link](http://link.springer.com/chapter/10.1007/978-3-030-27005-6_19)|Even though lifelong learning and neuroplasticity are important subjects, the paper doesn't directly relate its results to general intelligence, but is more related to DNN design|

|9|*A common-sense conceptual categorization system integrating heterogeneous proxytypes and the dual process of reasoning*|[Scopus](https://www.scopus.com/inward/record.uri?eid=2-s2.0-84949788233&partnerID=40&md5=38fbbfe06200ec391b5e23501c8ba1ba)|While knowledge representation is also important part of AGI, this work only relates itself to cognitive architectures without explicitly mentioning general intelligences.|

#### **Borderline papers**

|10|*The off-switch game*|[Scopus](https://www.scopus.com/inward/record.uri?eid=2-s2.0-85031899623&doi=10.24963%2fijcai.2017%2f32&partnerID=40&md5=f857e16f5d257fb5ef83d2aa969af1ac)|This paper focuses on the safety measures of AI not wanting itself to be shutdown. While it could be implicitly understood that this kind of self-preserving rational agent could also be a general agent, it is once again not specified, so I'm inclined to **exclude** this paper as too not-focused one.|

|12|*Should robots be obedient?*|[Scopus](https://www.scopus.com/inward/record.uri?eid=2-s2.0-85031901993&doi=10.24963%2fijcai.2017%2f662&partnerID=40&md5=c4d1b4c90b2481342324af23892fc336)|Again, this is something that can be focused either on general or narrow agents, and as such is **excluded**. Intuitively robot obedience is more prominent problem in general AI, but the general approach of this paper is not focused enough.|

|22|*Computable Variants of AIXI which are More Powerful than AIXItl*|[Sciendo](https://www.doi.org/10.2478/jagi-2019-0001)|Specifically focuses on AIXI and its computability, doesn't relate to AGI -> **excluded**|

|131|*Reflective Variants of Solomonoff Induction and AIXI*|[Springer Link](http://link.springer.com/chapter/10.1007/978-3-319-21365-1_7)|Relation between agent and environment is mentioned, and generality is somewhat brought forward -> **included**|


#### **Summary**

As can be seen from previous examples, some papers can be clearly seen as part
of the general intelligence research, but some are hard to distinguish from more
commonplace AI papers. On the other hand some very theoretical and specific
papers that might be deeply inherent part of the area are easily dismissed on
the basis that they don't mention certain umbrella terms and concepts. These
kind of papers are usually about Universal Induction, AIXI, or some Cognitive
Architecture. But including every paper relating to let's say, cognitive
architectures like OpenCog or NARS whether they mention goal of general
intelligence, raises the amount of papers too high for me to handle.

>My question is, **how could I limit the amount of relevant papers without accidentally excluding something important?**

I would suggest deliberately excluding papers unless they clearly relate
themselves to general intelligence/general agents in the
abstract/introduction/conclusion sections. This would lead to some possible
relevant papers to be excluded but as can be seen in the last 2 borderline
examples, some papers focusing on same topics would still remain, keeping the
sample relatively representative.


>The more intensive inspection was performed, and total number of papers limited
>to 93.

## Keywording

### What to do when analyzing a paper?

On the first read through finding papers' keywords and classifying them
according to Wieringa's class is the main goal. After that, combining keywords
and creating categories takes place. 

- Keywording:
  - Keywording is done in two steps. First, the reviewers read abstracts and
    look for keywords and concepts that reflect the contribution of the paper.
    While doing so the reviewer also identifies the context of the research.
    When this is done, the set of keywords from different papers are combined
    together to develop a high level understanding about the nature and
    contribution of the research.

- **Wieringa's classification**:
  This should be shown in a table in the thesis.

  - Validation Research
    - Novel techniques not implemented in practice.
  - Evaluation Research
    - Implementation in practice and its evaluation.
  - Solution Proposal
    - Solution is presented and arguments shown.
  - Philosophical Paper
    - Present new way to look things via taxonomy or conceptual framework.
  - Opinion Paper
    - Personal opinion on existing things. No related work or methods used.
  - Experience Paper
    - Explain what has been done in practice, relates to author's work.

-sidenote: It's interesting how the relation of embodiment and more theoretical
approach differs on many papers. Some say body is required to learn like human,
others steer clear of it to avoid too complex situations.


During this keywording phase, one paper (#23) was excluded because upon more
close inspection it was noticed that it didn't explicitly relate itself to
general ai.

Couple papers were difficult to give a Wieringa classification to (#6, #45). #6
was a traditional SLR, a type not separately classified by wieringa (technical
oriented), so it was decided to be classified as PP, as it in a way summarizes
existing research which helps the future research considerations. #45 was also
very much focused on the literature survey, and the results can't really be said
to be any novel solution as much as a viewpoint, so PP was chosen.

#74 was more of a project description, but it fit the criteria and presented a
one possible approach to AI evaluation, so it was classified as PP and included.

## Categorization and data extraction

### Cycle 1

Python script was used to take all the found keywords and calculate the initial
frequency distribution (how many instances of each kw was found). These were
then written to an spreadsheet where the creating and merging categories took
place.

Initial categories were formed by picking similar and closely relating concepts
by hand and grouping them together. From these groups, 39 initial categories was
formed. After that, further merging and removal of small categories was
performed. Here is the categorization (25) that is first tested on the material:

1 Cognitive architectures,
2 AI safety,
3 Universal AI,
4 Lifelong learning,
5 HCI,
6 Agent environment,
7 Human-like qualities,
8 AGI design,
9 Computer vision & perception,
10 AI research,
11 AI evaluation,
12 AI ethics,
13 Planning & decision making,
14 Philosophical aspects,
15 Reasoning and Inference,
16 Multi-agent systems,
17 Probabilistic approaches,
18 Game playing,
19 Problem specific research,
20 Nature-inspired approaches,
21 Neural networks,   
22 Physical robots,
23 Category theory,
24 Reinforcement learning,
25 Other

--> Frequencies: OrderedDict([(1, 27), (2, 16), (3, 14), (24, 11), (4, 8), (8,
8), (11, 8), (20, 8), (5, 7), (6, 7), (7, 7), (14, 7), (15, 7), (9, 5), (12, 5),
(13, 5), (16, 5), (17, 5), (18, 4), (19, 4), (10, 3), (22, 3), (23, 3), (21, 2),
(25, 1)])

Based on the first categorization of papers, it seems some minor work is needed:
- Nurture/pedagogy, imitation learning, and cumulative learning combined to Experiental Learning (Renamed from LLL)
- Neural networks? --> Removed category, only 2 papers with better more descriptive categories (Prolly many related but this is a really general category implementation wise)
- Separate RSI and AI safety. Can be explained on text to be closely related, but now this makes sense.
- Remove "Other" category as it is unnecessary and it is better to have proper categories
- Rename "AI research" to AGI research
- Remove "Problem specific research" as unnecessary category. Having a more
  concrete examples isn't a good enough reason for having a separate category.
- Merge "AI ethics" into "Philosophical aspects" 

### Phase 3 (Cycle 2)

1 Cognitive architectures,
2 AI safety,
3 Universal AI,
4 Experiential learning,
5 HCI,
6 Agent environment,
7 Human-like qualities,
8 AGI design,
9 Computer vision & perception,
10 AGI research,
11 AI evaluation,
13 Planning & decision making,
14 Philosophical aspects,
15 Reasoning and Inference,
16 Multi-agent systems,
17 Probabilistic approaches,
18 Game playing,
20 Nature-inspired approaches,  
22 Physical robots,
23 Category theory,
24 Reinforcement learning,
26 RSI

-> Frequencies: [(1, 26), (3, 14), (2, 12), (4, 11), (14, 11), (24, 11), (11,
8), (15, 8), (20, 8), (5, 7), (6, 7), (7, 7), (8, 6), (9, 5), (13, 5), (16, 5),
(17, 5), (10, 4), (18, 4), (26, 4), (22, 3), (23, 3), (12, 0), (19, 0), (21, 0),
(25, 0)])

### Final categories

1	Cognitive architectures
2	AGI design
3	Reasoning and Inference
4	Planning and decision making
5	Probabilistic approaches
6	Category theory
7	Universal AI
8	Physical robots
9	Computer vision and perception
10	Nature-inspired approaches
11	Reinforcement learning
12	Recursive self-Improvement
13	Experiential learning
14	Agent environment
15	Multi-agent systems
16	Human-computer interaction
17	AI safety
18	Philosophical aspects
19	Human-like qualities
20	AGI research
21	AI evaluation
22	Game playing

-> Frequencies: [(1, 26), (7, 14), (17, 12), (11, 11), (13, 11), (18, 11), (3,
8), (10, 8), (21, 8), (14, 7), (16, 7), (19, 7), (2, 6), (4, 5), (5, 5), (9, 5),
(15, 5), (12, 4), (20, 4), (22, 4), (6, 3), (8, 3)]

In the end, 22 noticeable categories/topics was found. As each paper could be
classified to many categories, there is overlap among them. This enables the
inspection of relation of categories, providing useful data. On the other hand
this might cause confusion on visualization.

## Visualization

### What to search for

Research questions were:
  - RQ1 How much, and what kind of research is done in the field of AGI?
  - RQ2 Where and when were the studies published?
  - RQ3 What are the major research topics in the field and have they changed
    over time?

What are the useful visualizations, numbers and such that should be found out
from the data? 

- Major themes can be mentioned on the text, but as they are very vague, not
  sure if they are useful as graph. DONE
- Type of research: 
  - Frequencies (bar plot) DONE
  - Relations between research types and topics (bubble/heatmap) DONE
- Topics
  - Yearly most researched DONE
  - Topics usually met together DONE
- Table describing each category DONE
- Publication forum frequency (most are from conference but still) DONE
  - Forum, additional limitations, total results, potential results, accepted results, accepted results(%)
- Publications per year per forum? DONE
- Research groups?
  - Authors and their paper frequencies
  - Affiliations and geographical locations?

PGFPlots was used to create the bubble plot, proved to be difficult to achieve
wanted results in matplotlib.


### Possible additions
- Authors -> Countries -> Bubble map
  - Interesting to see where the research is actually done and published. DONE
- ArXiv comparison: Compare research results to the actual publications in arxiv, where often studies are published directly.


## Finalization

- Appendices:
  - Accepted papers (maybe potential as well?) DONE
- Missing text:
  - Conclusion DONE
  - Abstract DONE
- TODOs DONE
- Chapter introduction paragraphs? DO THIS!!!
- CHECK THAT RQS ARE ANSWERED!!!
- Paper inclusion constraints (comments)
- JUFO forum etc paragraph edit
- search space volume numbers?
- clarify themes' connections to topics DONE?
- Fix topic/category term in table (and elsewhere) DONE
- clarify reason for just numbering topics DONE?
- bubble graph data order to same as elsewhere DONE
