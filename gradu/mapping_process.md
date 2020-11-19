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

  