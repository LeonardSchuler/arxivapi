EMPTY_RESPONSE = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <link href="http://arxiv.org/api/query?search_query%3D%22%22%26id_list%3D%26start%3D0%26max_results%3D10" rel="self" type="application/atom+xml"/>
  <title type="html">ArXiv Query: search_query=""&amp;id_list=&amp;start=0&amp;max_results=10</title>
  <id>http://arxiv.org/api/9fhNDPT7evg2QOL9mjP9D4lH7B0</id>
  <updated>2024-05-04T00:00:00-04:00</updated>
  <opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">0</opensearch:totalResults>
  <opensearch:startIndex xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">0</opensearch:startIndex>
  <opensearch:itemsPerPage xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">10</opensearch:itemsPerPage>
</feed>
"""


ARXIV_REMOTE_LLM_QUERY_RESPONSE = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <link href="http://arxiv.org/api/query?search_query%3Dlmm%26id_list%3D%26start%3D0%26max_results%3D8" rel="self" type="application/atom+xml"/>
  <title type="html">ArXiv Query: search_query=lmm&amp;id_list=&amp;start=0&amp;max_results=8</title>
  <id>http://arxiv.org/api/BIdFhNzn1BUHc/dQFgPqE+wJOLI</id>
  <updated>2024-05-01T00:00:00-04:00</updated>
  <opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">308</opensearch:totalResults>
  <opensearch:startIndex xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">0</opensearch:startIndex>
  <opensearch:itemsPerPage xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">8</opensearch:itemsPerPage>
  <entry>
    <id>http://arxiv.org/abs/2312.02896v2</id>
    <updated>2023-12-06T03:46:47Z</updated>
    <published>2023-12-05T17:06:59Z</published>
    <title>BenchLMM: Benchmarking Cross-style Visual Capability of Large Multimodal
  Models</title>
    <summary>  Large Multimodal Models (LMMs) such as GPT-4V and LLaVA have shown remarkable
capabilities in visual reasoning with common image styles. However, their
robustness against diverse style shifts, crucial for practical applications,
remains largely unexplored. In this paper, we propose a new benchmark,
BenchLMM, to assess the robustness of LMMs against three different styles:
artistic image style, imaging sensor style, and application style, where each
style has five sub-styles. Utilizing BenchLMM, we comprehensively evaluate
state-of-the-art LMMs and reveal: 1) LMMs generally suffer performance
degradation when working with other styles; 2) An LMM performs better than
another model in common style does not guarantee its superior performance in
other styles; 3) LMMs' reasoning capability can be enhanced by prompting LMMs
to predict the style first, based on which we propose a versatile and
training-free method for improving LMMs; 4) An intelligent LMM is expected to
interpret the causes of its errors when facing stylistic variations. We hope
that our benchmark and analysis can shed new light on developing more
intelligent and versatile LMMs.
</summary>
    <author>
      <name>Rizhao Cai</name>
    </author>
    <author>
      <name>Zirui Song</name>
    </author>
    <author>
      <name>Dayan Guan</name>
    </author>
    <author>
      <name>Zhenhao Chen</name>
    </author>
    <author>
      <name>Xing Luo</name>
    </author>
    <author>
      <name>Chenyu Yi</name>
    </author>
    <author>
      <name>Alex Kot</name>
    </author>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">Code is available at https://github.com/AIFEG/BenchLMM</arxiv:comment>
    <link href="http://arxiv.org/abs/2312.02896v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/2312.02896v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cs.CV" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.CV" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/math/0611846v1</id>
    <updated>2006-11-28T01:02:29Z</updated>
    <published>2006-11-28T01:02:29Z</published>
    <title>DRP scheme optimization</title>
    <summary>  A new DRP scheme is built, which enables us to minimize the error due to the
finite difference approximation, by means of an equivalent matrix equation.
</summary>
    <author>
      <name>Claire David</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <author>
      <name>Pierre Sagaut</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <link href="http://arxiv.org/abs/math/0611846v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/math/0611846v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="math.AP" scheme="http://arxiv.org/schemas/atom"/>
    <category term="math.AP" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2404.18203v1</id>
    <updated>2024-04-28T14:47:09Z</updated>
    <published>2024-04-28T14:47:09Z</published>
    <title>LMM-PCQA: Assisting Point Cloud Quality Assessment with LMM</title>
    <summary>  Although large multi-modality models (LMMs) have seen extensive exploration
and application in various quality assessment studies, their integration into
Point Cloud Quality Assessment (PCQA) remains unexplored. Given LMMs'
exceptional performance and robustness in low-level vision and quality
assessment tasks, this study aims to investigate the feasibility of imparting
PCQA knowledge to LMMs through text supervision. To achieve this, we transform
quality labels into textual descriptions during the fine-tuning phase, enabling
LMMs to derive quality rating logits from 2D projections of point clouds. To
compensate for the loss of perception in the 3D domain, structural features are
extracted as well. These quality logits and structural features are then
combined and regressed into quality scores. Our experimental results affirm the
effectiveness of our approach, showcasing a novel integration of LMMs into PCQA
that enhances model understanding and assessment accuracy. We hope our
contributions can inspire subsequent investigations into the fusion of LMMs
with PCQA, fostering advancements in 3D visual quality analysis and beyond.
</summary>
    <author>
      <name>Zicheng Zhang</name>
    </author>
    <author>
      <name>Haoning Wu</name>
    </author>
    <author>
      <name>Yingjie Zhou</name>
    </author>
    <author>
      <name>Chunyi Li</name>
    </author>
    <author>
      <name>Wei Sun</name>
    </author>
    <author>
      <name>Chaofeng Chen</name>
    </author>
    <author>
      <name>Xiongkuo Min</name>
    </author>
    <author>
      <name>Xiaohong Liu</name>
    </author>
    <author>
      <name>Weisi Lin</name>
    </author>
    <author>
      <name>Guangtao Zhai</name>
    </author>
    <link href="http://arxiv.org/abs/2404.18203v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/2404.18203v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cs.CV" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.CV" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.AI" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2108.05102v2</id>
    <updated>2023-01-19T15:25:44Z</updated>
    <published>2021-08-11T09:01:34Z</published>
    <title>Normalized Wolfe-Powell-type local minimax method for finding multiple
  unstable solutions of nonlinear elliptic PDEs</title>
    <summary>  The local minimax method (LMM) proposed in [Y. Li and J. Zhou, SIAM J. Sci.
Comput., 23(3), 840--865 (2001)] and [Y. Li and J. Zhou, SIAM J. Sci. Comput.,
24(3), 865--885 (2002)] is an efficient method to solve nonlinear elliptic
partial differential equations (PDEs) with certain variational structures for
multiple solutions. The steepest descent direction and the Armijo-type
step-size search rules are adopted in [Y. Li and J. Zhou, SIAM J. Sci. Comput.,
24(3), 865--885 (2002)] and play a significant role in the performance and
convergence analysis of traditional LMMs. In this paper, a new algorithm
framework of the LMMs is established based on general descent directions and
two normalized (strong) Wolfe-Powell-type step-size search rules. The
corresponding algorithm framework named as the normalized Wolfe-Powell-type LMM
(NWP-LMM) is introduced with its feasibility and global convergence rigorously
justified for general descent directions. As a special case, the global
convergence of the NWP-LMM algorithm combined with the preconditioned steepest
descent (PSD) directions is also verified. Consequently, it extends the
framework of traditional LMMs. In addition, conjugate gradient-type (CG-type)
descent directions are utilized to speed up the NWP-LMM algorithm. Finally,
extensive numerical results for several semilinear elliptic PDEs are reported
to profile their multiple unstable solutions and compared for different
algorithms in the LMM's family to indicate the effectiveness and robustness of
our algorithms. In practice, the NWP-LMM combined with the CG-type direction
indeed performs much better than its known LMM companions.
</summary>
    <author>
      <name>Wei Liu</name>
    </author>
    <author>
      <name>Ziqing Xie</name>
    </author>
    <author>
      <name>Wenfan Yi</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1007/s11425-021-2093-1</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1007/s11425-021-2093-1" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">27 pages, 9 figures; Accepted by SCIENCE CHINA Mathematics on January
  17, 2023</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Science China Mathematics, 2023, Vol. 66, No. 10, pp. 2361-2384</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/2108.05102v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/2108.05102v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="math.NA" scheme="http://arxiv.org/schemas/atom"/>
    <category term="math.NA" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.NA" scheme="http://arxiv.org/schemas/atom"/>
    <category term="35J20, 35B38, 65N12, 65J15, 65Jxx" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/math/0607654v1</id>
    <updated>2006-07-26T04:56:26Z</updated>
    <published>2006-07-26T04:56:26Z</published>
    <title>Spurious solitons and structural stability of finite difference schemes
  for nonlinear wave equations</title>
    <summary>  The goal of this work is to determine classes of traveling Solitary wave
solutions for a differential approximation of a finite difference scheme by
means of a hyperbolic ansatz.
</summary>
    <author>
      <name>Claire David</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <author>
      <name>Pierre Sagaut</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <link href="http://arxiv.org/abs/math/0607654v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/math/0607654v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="math.AP" scheme="http://arxiv.org/schemas/atom"/>
    <category term="math.AP" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/math/0607680v1</id>
    <updated>2006-07-26T17:25:29Z</updated>
    <published>2006-07-26T17:25:29Z</published>
    <title>A Note On 3Solitary Wave Solutions of the Compound Burgers-Korteweg-de
  Vries Equation"</title>
    <summary>  The goal of this note is to construct a class of traveling solitary wave
solutions for the compound Burgers-Korteweg-de Vries equation by means of a
hyperbolic ansatz.
</summary>
    <author>
      <name>Claire David</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <author>
      <name>Rasika Fernando</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <author>
      <name>Zhaosheng Feng</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">UTPA</arxiv:affiliation>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1016/j.physa.2006.09.008</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1016/j.physa.2006.09.008" rel="related"/>
    <link href="http://arxiv.org/abs/math/0607680v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/math/0607680v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="math.AP" scheme="http://arxiv.org/schemas/atom"/>
    <category term="math.AP" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/0801.3017v1</id>
    <updated>2008-01-19T07:47:08Z</updated>
    <published>2008-01-19T07:47:08Z</published>
    <title>Towards optimal DRP scheme for linear advection</title>
    <summary>  Finite difference schemes are here solved by means of a linear matrix
equation. The theoretical study of the related algebraic system is exposed, and
enables us to minimize the error due to a finite difference approximation,
while building a new DRP scheme in the same time.
</summary>
    <author>
      <name>Claire David</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <author>
      <name>Pierre Sagaut</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <link href="http://arxiv.org/abs/0801.3017v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/0801.3017v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="math.AP" scheme="http://arxiv.org/schemas/atom"/>
    <category term="math.AP" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2012.03557v1</id>
    <updated>2020-12-07T09:57:14Z</updated>
    <published>2020-12-07T09:57:14Z</published>
    <title>Quasilinear Stochastic PDEs with two obstacles: Probabilistic approach</title>
    <summary>  We prove an existence and uniqueness result for two-obstacle problem for
quasilinear Stochastic PDEs (DOSPDEs for short). The method is based on the
probabilistic interpretation of the solution by using the backward doubly
stochastic differential equations (BDSDEs for short).
</summary>
    <author>
      <name>Laurent Denis</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <author>
      <name>Anis Matoussi</name>
      <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom">LMM</arxiv:affiliation>
    </author>
    <author>
      <name>Jing Zhang</name>
    </author>
    <link href="http://arxiv.org/abs/2012.03557v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/2012.03557v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="math.PR" scheme="http://arxiv.org/schemas/atom"/>
    <category term="math.PR" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
</feed>
"""

ARXIV_REMOTE_A_DEL_MAESTRO_AUTHOR_QUERY_RESPONSE = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <link href="http://arxiv.org/api/query?search_query%3Dau%3A%22A.%20Del%20Maestro%22%26id_list%3D%26start%3D0%26max_results%3D10" rel="self" type="application/atom+xml"/>
  <title type="html">ArXiv Query: search_query=au:"A. Del Maestro"&amp;id_list=&amp;start=0&amp;max_results=10</title>
  <id>http://arxiv.org/api/nRLM9eDdevfkqTi73OBL1i1CPDU</id>
  <updated>2024-05-04T00:00:00-04:00</updated>
  <opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">12</opensearch:totalResults>
  <opensearch:startIndex xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">0</opensearch:startIndex>
  <opensearch:itemsPerPage xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">10</opensearch:itemsPerPage>
  <entry>
    <id>http://arxiv.org/abs/1303.6954v2</id>
    <updated>2013-09-03T01:06:36Z</updated>
    <published>2013-03-27T20:00:04Z</published>
    <title>Local Superfluidity at the Nanoscale</title>
    <summary>  We have performed quantum Monte Carlo simulations measuring the finite size
and temperature superfluid response of helium-4 to the linear and rotational
motion of the walls of a nanopore. Within the two-fluid model, the portion of
the normal liquid dragged along with the boundaries is dependent on the type of
motion and the resulting anisotropic superfluid density saturates far below
unity at T=0.5 K. The origin of the saturation is uncovered by computing the
spatial distribution of superfluidity, with only the core of the nanopore
exhibiting any evidence of phase coherence. The superfluid core displays
scaling behavior consistent with Luttinger liquid theory, thereby providing an
experimental test for the emergence of a one dimensional quantum liquid.
</summary>
    <author>
      <name>B. Kulchytskyy</name>
    </author>
    <author>
      <name>G. Gervais</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1103/PhysRevB.88.064512</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1103/PhysRevB.88.064512" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">Added a figure and extended discussion</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Physical Review B 88, 064512 (2013)</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/1303.6954v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1303.6954v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.mes-hall" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.mes-hall" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.stat-mech" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/1412.6529v2</id>
    <updated>2015-02-25T23:04:37Z</updated>
    <published>2014-12-19T21:00:08Z</published>
    <title>Particle partition entanglement of bosonic Luttinger liquids</title>
    <summary>  We consider the R\'{e}nyi entanglement entropy of bosonic Luttinger liquids
under a particle bipartition and demonstrate that the leading order finite-size
scaling is logarithmic in the system size with a prefactor equal to the inverse
Luttinger parameter. While higher order corrections involve a microscopic
length scale, the leading order scaling depends only on this sole dimensionless
parameter which characterizes the low energy quantum hydrodynamics. This result
contrasts the leading entanglement entropy scaling under a spatial bipartition,
for which the coefficient is universal and independent of the Luttinger
parameter. Using quantum Monte Carlo calculations, we explicitly confirm the
scaling predictions of Luttinger liquid theory for the Lieb-Liniger model of
$\\delta$-function interacting bosons in the one dimensional spatial continuum.
</summary>
    <author>
      <name>C. M. Herdman</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1103/PhysRevB.91.184507</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1103/PhysRevB.91.184507" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">10 pages, 8 figures; updated figure 5, added references, revised
  text, reformatted</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Phys. Rev. B 91, 184507 (2015)</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/1412.6529v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1412.6529v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.quant-gas" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.quant-gas" scheme="http://arxiv.org/schemas/atom"/>
    <category term="quant-ph" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/1312.6177v1</id>
    <updated>2013-12-20T23:48:25Z</updated>
    <published>2013-12-20T23:48:25Z</published>
    <title>Quantum Monte Carlo measurement of the chemical potential of helium-4</title>
    <summary>  A path integral Monte Carlo method based on the worm algorithm has been
developed to compute the chemical potential of interacting bosonic quantum
fluids. By applying it to finite-sized systems of helium-4 atoms, we have
confirmed that the chemical potential scales inversely with the number of
particles to lowest order. The introduction of a simple scaling form allows for
the extrapolation of the chemical potential to the thermodynamic limit, where
we observe excellent agreement with known experimental results for helium-4 at
saturated vapor pressure. We speculate on future applications of the proposed
technique, including its use in studies of confined quantum fluids.
</summary>
    <author>
      <name>C. M. Herdman</name>
    </author>
    <author>
      <name>A. Rommal</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1103/PhysRevB.89.224502</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1103/PhysRevB.89.224502" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">7 pages, 4 figures</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Phys. Rev. B 89, 224502 (2014)</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/1312.6177v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1312.6177v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.stat-mech" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.stat-mech" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.other" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2402.17843v1</id>
    <updated>2024-02-27T19:17:11Z</updated>
    <published>2024-02-27T19:17:11Z</published>
    <title>Efficient simulations of Hartree--Fock equations by an accelerated
  gradient descent method</title>
    <summary>  We develop convergence acceleration procedures that enable a gradient
descent-type iteration method to efficiently simulate Hartree--Fock equations
for atoms interacting both with each other and with an external potential. Our
development focuses on three aspects: (i) optimization of a parameter in the
preconditioning operator; (ii) adoption of a technique that eliminates the
slowest-decaying mode to the case of many equations (describing many atoms);
and (iii) a novel extension of the above technique that allows one to eliminate
multiple modes simultaneously. We illustrate performance of the numerical
method for the 2D model of the first layer of helium atoms above a graphene
sheet. We demonstrate that incorporation of aspects (i) and (ii) above into the
``plain" gradient descent method accelerates it by at least two orders of
magnitude, and often by much more. Aspect (iii) -- a multiple-mode elimination
-- may bring further improvement to the convergence rate compared to aspect
(ii), the single-mode elimination. Both single- and multiple-mode elimination
techniques are shown to significantly outperform the well-known Anderson
Acceleration. We believe that our acceleration techniques can also be gainfully
employed by other numerical methods, especially those handling hard-core-type
interaction potentials.
</summary>
    <author>
      <name>Y. Ohno</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <author>
      <name>T. I. Lakoba</name>
    </author>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">main text (39 pages); supplement appended (7 pages)</arxiv:comment>
    <link href="http://arxiv.org/abs/2402.17843v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/2402.17843v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="physics.comp-ph" scheme="http://arxiv.org/schemas/atom"/>
    <category term="physics.comp-ph" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.other" scheme="http://arxiv.org/schemas/atom"/>
    <category term="nlin.PS" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/cond-mat/0607501v2</id>
    <updated>2006-11-06T19:33:40Z</updated>
    <published>2006-07-19T20:12:54Z</published>
    <title>A striped supersolid phase and the search for deconfined quantum
  criticality in hard-core bosons on the triangular lattice</title>
    <summary>  Using large-scale quantum Monte Carlo simulations we study bosons hopping on
a triangular lattice with nearest (V) and next-nearest (V') neighbor repulsive
interactions. In the limit where V=0 but V' is large, we find an example of an
unusual period-three striped supersolid state that is stable at 1/2-filling. We
discuss the relationship of this state to others on the rich ground-state phase
diagram, which include a previously-discovered nearest-neighbor supersolid, a
uniform superfluid, as well as several Mott insulating phases. We study several
superfluid- and supersolid-to-Mott phase transitions, including one proposed by
a recent phenomenological dual vortex field theory as a candidate for an exotic
deconfined quantum critical point. We find no examples of unconventional
quantum criticality among any of the interesting phase transitions in the
model.
</summary>
    <author>
      <name>R. G. Melko</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <author>
      <name>A. A. Burkov</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1103/PhysRevB.74.214517</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1103/PhysRevB.74.214517" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">10 pages, 11 figures: new data for superfluid density anisotropy</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Phys. Rev. B 74, 214517 (2006)</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/cond-mat/0607501v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/cond-mat/0607501v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.str-el" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.str-el" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/cond-mat/0308092v2</id>
    <updated>2004-05-03T21:52:24Z</updated>
    <published>2003-08-05T20:23:10Z</published>
    <title>The Spin Liquid State of the Tb2Ti2O7 Pyrochlore Antiferromagnet: A
  Puzzling State of Affairs</title>
    <summary>  The pyrochlore antiferromagnet Tb2Ti2O7 has proven to be an enigma to
experimentalists and theorists working on frustrated magnetic systems. The
experimentally determined energy level structure suggests a local &lt;111&gt; Ising
antiferromagnet at low temperatures, T &lt; 10 K. An appropriate model then
predicts a long-range ordered Q = 0 state below approximately 2 K. However,
muon spin resonance experiments reveal a paramagnetic structure down to tens of
milli-Kelvin. The importance of fluctuations out of the ground state effective
Ising doublet has been recently understood, for the measured paramagnetic
correlations can not be described without including the higher crystal field
states. However, these fluctuations treated within the random phase
approximation (RPA) fail to account for the lack of ordering in this system
below 2 K. In this work, we briefly review the experimental evidence for the
collective paramagnetic state of Tb2Ti2O7. The basic theoretical picture for
this system is discussed, where results from classical spin models are used to
motivate the investigation of quantum effects to lowest order via the RPA.
Avenues for future experimental and theoretical work on Tb2Ti2O7 are presented.
</summary>
    <author>
      <name>M. Enjalran</name>
    </author>
    <author>
      <name>M. J. P. Gingras</name>
    </author>
    <author>
      <name>Y. -J. Kao</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <author>
      <name>H. R. Molavian</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1088/0953-8984/16/11/014</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1088/0953-8984/16/11/014" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">Latex2e,6 pages, IOP format, introduction shortened and other minor
  corrections, replaced with published version in the Proceedings of the Highly
  Frustrated Magnetism 2003 Conference, Grenoble</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">J. Phys.: Condens. Matter 16 (2004) S673</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/cond-mat/0308092v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/cond-mat/0308092v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.stat-mech" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.stat-mech" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.mtrl-sci" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/1310.8332v2</id>
    <updated>2014-04-07T23:49:16Z</updated>
    <published>2013-10-30T21:43:06Z</published>
    <title>Particle entanglement in continuum many-body systems via quantum Monte
  Carlo</title>
    <summary>  Entanglement of spatial bipartitions, used to explore lattice models in
condensed matter physics, may be insufficient to fully describe itinerant
quantum many-body systems in the continuum. We introduce a procedure to measure
the R\'enyi entanglement entropies on a particle bipartition, with general
applicability to continuum Hamiltonians via path integral Monte Carlo methods.
Via direct simulations of interacting bosons in one spatial dimension, we
confirm a logarithmic scaling of the single-particle entanglement entropy with
the number of particles in the system. The coefficient of this logarithmic
scaling increases with interaction strength, saturating to unity in the
strongly interacting limit. Additionally, we show that the single-particle
entanglement entropy is bounded by the condensate fraction, suggesting a
practical route towards its measurement in future experiments.
</summary>
    <author>
      <name>C. M. Herdman</name>
    </author>
    <author>
      <name>P. -N. Roy</name>
    </author>
    <author>
      <name>R. G. Melko</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1103/PhysRevB.89.140501</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1103/PhysRevB.89.140501" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">6 pages, 4 figures</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Phys. Rev. B 89, 140501 (2014)</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/1310.8332v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1310.8332v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.quant-gas" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.quant-gas" scheme="http://arxiv.org/schemas/atom"/>
    <category term="quant-ph" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/1404.7104v2</id>
    <updated>2014-08-04T17:50:52Z</updated>
    <published>2014-04-28T19:25:04Z</published>
    <title>A path integral Monte Carlo method for Rényi entanglement entropies</title>
    <summary>  We introduce a quantum Monte Carlo algorithm to measure the R\'enyi
entanglement entropies in systems of interacting bosons in the continuum. This
approach is based on a path integral ground state method that can be applied to
interacting itinerant bosons in any spatial dimension with direct relevance to
experimental systems of quantum fluids. We demonstrate how it may be used to
compute spatial mode entanglement, particle partitioned entanglement, and the
entanglement of particles, providing insights into quantum correlations
generated by fluctuations, indistinguishability and interactions. We present
proof-of-principle calculations, and benchmark against an exactly soluble model
of interacting bosons in one spatial dimension. As this algorithm retains the
fundamental polynomial scaling of quantum Monte Carlo when applied to
sign-problem-free models, future applications should allow for the study of
entanglement entropy in large scale many-body systems of interacting bosons.
</summary>
    <author>
      <name>C. M. Herdman</name>
    </author>
    <author>
      <name>Stephen Inglis</name>
    </author>
    <author>
      <name>P. -N. Roy</name>
    </author>
    <author>
      <name>R. G. Melko</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1103/PhysRevE.90.013308</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1103/PhysRevE.90.013308" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">19 pages, 13 figures; updated figures, fixed typos, and fixed
  notational inconsistencies</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Phys. Rev. E 90, 013308 (2014)</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/1404.7104v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1404.7104v2" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.quant-gas" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.quant-gas" scheme="http://arxiv.org/schemas/atom"/>
    <category term="quant-ph" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/1412.5124v1</id>
    <updated>2014-12-16T19:00:08Z</updated>
    <published>2014-12-16T19:00:08Z</published>
    <title>Critical Flow and Dissipation in a Quasi-One-Dimensional Superfluid</title>
    <summary>  In one of the most celebrated examples of the theory of universal critical
phenomena, the phase transition to the superfluid state of $^{4}$He belongs to
the same three dimensional $\\mathrm{O}(2)$ universality class as the onset of
ferromagnetism in a lattice of classical spins with $XY$ symmetry. Below the
transition, the superfluid density $\rho_s$ and superfluid velocity $v_s$
increase as power laws of temperature described by a universal critical
exponent constrained to be equal by scale invariance. As the dimensionality is
reduced towards one dimension (1D), it is expected that enhanced thermal and
quantum fluctuations preclude long-range order, thereby inhibiting
superfluidity. We have measured the flow rate of liquid helium and deduced its
superfluid velocity in a capillary flow experiment occurring in single $30~$nm
long nanopores with radii ranging down from 20~nm to 3~nm. As the pore size is
reduced towards the 1D limit, we observe: {\\it i)} a suppression of the
pressure dependence of the superfluid velocity; {\\it ii)} a temperature
dependence of $v_{s}$ that surprisingly can be well-fitted by a powerlaw with a
single exponent over a broad range of temperatures; and {\\it iii)} decreasing
critical velocities as a function of radius for channel sizes below $R \\simeq
20$~nm, in stark contrast with what is observed in micron sized channels. We
interpret these deviations from bulk behaviour as signaling the crossover to a
quasi-1D state whereby the size of a critical topological defect is cut off by
the channel radius.
</summary>
    <author>
      <name>P-F Duc</name>
    </author>
    <author>
      <name>M. Savard</name>
    </author>
    <author>
      <name>M. Petrescu</name>
    </author>
    <author>
      <name>B. Rosenow</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <author>
      <name>G. Gervais</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1126/sciadv.1400222</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1126/sciadv.1400222" rel="related"/>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Science Advances 1, e1400222 (2015)</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/1412.5124v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1412.5124v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.mes-hall" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.mes-hall" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.other" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.quant-gas" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.str-el" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/1610.08518v1</id>
    <updated>2016-10-26T20:00:04Z</updated>
    <published>2016-10-26T20:00:04Z</published>
    <title>Entanglement area law in superfluid $^4$He</title>
    <summary>  Area laws were first discovered by Bekenstein and Hawking, who found that the
entropy of a black hole grows proportional to its surface area, and not its
volume. Entropy area laws have since become a fundamental part of modern
physics, from the holographic principle in quantum gravity to ground state
wavefunctions of quantum matter, where entanglement entropy is generically
found to obey area law scaling. As no experiments are currently capable of
directly probing the entanglement area law in naturally occurring many-body
systems, evidence of its existence is based on studies of simplified theories.
Using new exact microscopic numerical simulations of superfluid $^4$He, we
demonstrate for the first time an area law scaling of entanglement entropy in a
real quantum liquid in three dimensions. We validate the fundamental principles
underlying its physical origin, and present an "entanglement equation of state"
showing how it depends on the density of the superfluid.
</summary>
    <author>
      <name>C. M. Herdman</name>
    </author>
    <author>
      <name>P. -N. Roy</name>
    </author>
    <author>
      <name>R. G. Melko</name>
    </author>
    <author>
      <name>A. Del Maestro</name>
    </author>
    <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom">10.1038/nphys4075</arxiv:doi>
    <link title="doi" href="http://dx.doi.org/10.1038/nphys4075" rel="related"/>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">main text: 4 pages, 4 figures + supplementary information: 3 pages, 2
  figures</arxiv:comment>
    <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom">Nature Phys. 13, 556 (2017)</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/1610.08518v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/1610.08518v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="cond-mat.other" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cond-mat.other" scheme="http://arxiv.org/schemas/atom"/>
    <category term="quant-ph" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
</feed>
"""


QUERY_RESPONSE_MAP = {
    "llm": ARXIV_REMOTE_LLM_QUERY_RESPONSE,
    'au:"A. Del Maestro"': ARXIV_REMOTE_A_DEL_MAESTRO_AUTHOR_QUERY_RESPONSE,
}
