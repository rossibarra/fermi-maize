---
title: "Maize Population Genetics — Fermi Math Cheatsheet"
author: "Jeffrey Ross-Ibarra"
description: "Rules of thumb, length scales, population-genetic parameters and worked Fermi problems for maize, with references."
bibliography: references.bib
csl: nature-compact.csl
link-citations: true
---

<!--
HOW TO EDIT
- Text is pandoc markdown. Superscript: 10^9^   Subscript: N~e~   Italic: *π*   Bold: **text**
- Cite with [@key] right after the text, no space: "39,756 genes[@b73v5]". Several: [@key1; @key2].
  Keys live in references.bib; add a BibTeX entry there for any new source. Numbering is automatic.
- Math in the worked examples uses LaTeX between $...$.
- The ::: {#p1 .page} blocks are the three PDF pages. Keep each block's content to roughly its current length:
  the PDF build scales the font so each page is full, so very long additions make the text small.
- Run `python scripts/build.py` to preview locally, or just open a pull request: GitHub Actions builds the
  web page and PDF and uploads them as an artifact you can download from the PR's checks.
-->

<!-- ===================== PAGE 1: the cheatsheet ===================== -->
::: {#p1 .page}
# Maize Population Genetics — Fermi Math Cheatsheet

## The “Rule of Thumb” Top 10

| Quantity                               | Fermi Number                      | Exact / Literature Range                                                                                                                                                               |
|--------------------|------------------|--------------------------------------------------------------------------------------------|
| Haploid genome size (*G*)              | ∼2 Gb (2 × 10^9^ bp)              | 2.13 Gb in 10 chromosomes[@b73v5] (2*n* = 20)[@gaut2000]; up to 3.1 Gb in landraces[@realini2016; @bilinski2018]                                                                |
| Protein-coding genes                   | ∼4 × 10^4^                        | 39,756 in B73[@b73v5]; ∼103,000 pan-genes (∼1/3 core)[@hufford2021]                                                                                                              |
| Mutation rate (*μ*)                    | ∼3 × 10^−8^ bp^−1^ gen^−1^        | 3–7.3 × 10^−8^ (∼65–155 new mutations/gamete)[@clark2005; @yang2017]                                                                                                                |
| Recombination rate (*r*)               | ∼10^−8^ bp^−1^ (∼1 cM/Mb)         | 0.7 cM/Mb mean; ∼1,500 cM map (∼15 COs/gamete)[@ogut2015; @mcmullen2009; @finemap]                                                                                                      |
| Nucleotide diversity (*π*)             | ∼1.5% (1.5 × 10^−2^)              | 1.4 × 10^−2^ genome-wide; 1.2 × 10^−2^ at genes, 2.1 × 10^−2^ far from genes[@liu2025]                                                                                              |
| Pop-scaled mutation (*θ* = 4*N*~e~*μ*) | ∼0.015                            | *θ*~W~ ≈ 0.015 across 26 NAM founders (1 SNP / 18 bp)[@liu2025]                                                                                                                     |
| Pop-scaled recomb. (*ρ* = 4*N*~e~*r*)  | ∼0.004 bp^−1^ (∼4 kb^−1^)         | *ρ*/*θ* = *r*/*μ* ≈ 0.1–0.35 (ignores gene conversion)                                                                                                                                |
| Effective pop. size (*N*~e~)           | ∼10^5^ (long-term)                | 0.7–1.8 × 10^5^ from *π*~0~[@liu2025]; bottleneck ∼8k (9 kya), modern ∼10k[@peqg2026]                                                                                           |
| Census size (*N*~c~) & density         | ∼10^12^ plants (∼3 × 10^4^/ha)    | ∼10^12^ open-pollinated plants[@beissinger2016]; 2–8 × 10^4^ plants/ha (dryland to irrigated)[@ogtr2008]                                                                        |
| Fecundity & mating                     | ∼500 kernels/ear; ∼95% outcrossed | 300–1,000 kernels/ear[@ogtr2008] (400–600 typical[@nielsen2007]); 5–50 × 10^6^ pollen grains/plant/season[@hofmann2014]; ∼5% selfing[@ogtr2008]; 1 yr/gen[@wang2017] |

## Genomic Length Scales (smallest → largest)

-   **Conserved noncoding sequence (CNS): ∼30 bp** (median 12–40 bp across species; 73% upstream of their gene, ∼25% >25 kb away)[@amundson2026]; 27 bp–15 kb in maize[@song2021]
-   **Exon / intron: ∼150 bp** each (160 bp exon, 140 bp intron medians; 90% of introns < 1.4 kb)[@b73v5]
-   **TIR transposon copy: ∼300 bp** (310 bp median)[@b73v4te]
-   **Coding sequence (CDS) per gene: ∼900 bp** (880 bp median; 3 exons/gene median; 23% single-exon)[@b73v5]
-   **Pre-mRNA gene span: ∼3 kb** (2.7 kb median; 90% < 9 kb)[@b73v5]
-   **Intact TE copy: ∼10 kb** (LTR retrotransposons 11 kb; Helitrons 7 kb medians)[@b73v4te]
-   **Intergenic distance: ∼25 kb** (26 kb median; 10–90%: 0.8–136 kb)[@b73v5]
-   **Extent of LD (distance to mean *r*^2^ = 0.1): ∼10–50 kb** in annual teosintes (e.g. *parviglumis n* = 70, *mexicana n* = 81) vs. **∼200 kb** in 507 maize inbreds[@chen2022]; within genes, *r*^2^ < 0.1 by 1.5 kb in 102 diverse inbreds (6 genes)[@remington2001]
-   **Distal regulatory elements: ∼2–100 kb** from genes (∼1/3 of accessible chromatin >2 kb from a gene[@ricci2019]; *tb1* ∼60 kb[@studer2011], *Vgt1* 70 kb[@salvi2007], *b1* 100 kb[@stam2002])
-   **Domestication sweep: ∼300 kb** (mean selected region)[@hufford2012]
-   **Centromere (CENH3 domain): ∼2 Mb** (1.8 Mb)[@wang2014]
-   **Chromosome length: ∼200 Mb** (152–308 Mb; ∼16 genes/Mb median, 35/Mb near tips vs. 10/Mb mid-chromosome)[@b73v5]

## Genome Composition, Variation & Selection

-   **Genome fractions: ∼85% TEs** (∼74% LTR, ∼8.5% DNA TEs)[@hufford2021; @schnable2009]; 200k intact copies in 29k families; *huck*, *ji*, *cinful-zeon*, *opie* 7–11% each[@b73v4te; @jiao2017]; **∼8% genic**; **∼2% CDS**[@b73v5]; **42% callable** across NAM assemblies[@liu2025].
-   **Conserved noncoding sequence: ∼5%** of the genome (∼107 Mb conserved across Andropogoneae, 42 Mb in all species; ∼half in UTRs and introns; 87% of genes have a CNS within 2 kb upstream)[@song2021]; 80% of maize CNSs carry a predicted TF binding site[@amundson2026].
-   **Protein evidence:** peptides detected for **66%** of annotated B73 proteins across public mass-spec data[@vanwijk2024]; proteins from ∼18,500 genes in a 33-tissue atlas[@walley2016].
-   **Paleopolyploidy:** ancient allotetraploid (subgenomes split ∼12 MYA[@swigonova2004]; polyploidy shared with *Tripsacum*[@chen2022]); **≥50%** of duplicate genes lost[@lai2004].
-   **Polymorphism & SVs: ∼1 SNP / 70 bp** between two random haplotypes[@liu2025]; **>83M SNPs** (1,218 lines)[@bukowski2018]; **∼8 × 10^5^ SVs** (>100 bp) in 26 NAM founders (50% < 5 kb)[@hufford2021].
-   **Divergence & admixture:** landraces retain **∼83%** of *parviglumis* *π* (*F*~ST~ ≈ 0.11)[@hufford2012]; *parviglumis* vs. *mexicana* *F*~ST~ ≈ 0.33[@pyhajarvi2013]; modern maize carries **∼18%** (15–25%) *mexicana* ancestry[@yang2023].
-   **Selection & constraint:** background selection reduces *π* **∼43%** at genes (*B* = 0.57; recovers by 0.1 cM) and **∼26%** genome-wide (mean *B* = 0.74)[@liu2025; @finemap]; only ∼10% of the genome (>1 cM/Mb) nears neutral *π*[@tittes2025]. Deleterious rate **∼3 × 10^−10^ bp^−1^** (*U*~d~ ≈ 0.6 per gamete; *u*/*μ* ≈ 0.5–1%, an equivalent target of ∼10–20 Mb)[@liu2025]. Domestication ***s* ≈ 0.015**[@hufford2012].

## Evolutionary Timeline (approximate)

-   **∼12 MYA:** maize–sorghum & subgenome split[@swigonova2004] • **<3 MYA:** LTR expansion[@sanmiguel1998] (median intact LTR ∼0.8 MY[@b73v4te; @clark2005])
-   **∼650 kya:** *Zea*–*Tripsacum*[@chen2022] → **∼120 kya:** *Z. luxurians*[@chen2022] → **∼30–60 kya:** *parviglumis*–*mexicana* split[@chen2022; @rossibarra2009]
-   **∼9 kya:** Balsas domestication[@matsuoka2002] (microfossils 8.7 kya[@piperno2009]; cobs 6.25 kya[@piperno2001]) → **∼6.5 kya:** S. America[@kistler2018] → **∼5 kya:** *mexicana* admixture[@yang2023] → **∼4.1 kya:** US Southwest[@merrill2009] → **1493 CE:** Europe[@tenaillon2011]
:::

<!-- ===================== PAGE 2: notes and references ===================== -->
::: {#p2 .page}
## Notes on Derived & Computed Values

-   **Genome size & DNA mass:** landrace 2C = 4.62–6.29 pg[@realini2016; @bilinski2018]; haploid size = 2C/2 × 0.978 Gb/pg = 2.26–3.08 Gb (B73: 2.13 Gb ≈ 2.18 pg per 1C).
-   **Mutations & crossovers per gamete:** *μ* × 2.13 × 10^9^ bp for *μ* = 3–7.3 × 10^−8^[@clark2005; @yang2017]; 7.3 × 10^−8^ is from unpublished mutation-accumulation lines. The NAM consensus map has 1,478 markers at 1-cM spacing across 10 chromosomes (∼1,470 cM)[@ogut2015; @mcmullen2009]; map/100 ≈ 15 COs/gamete; 1,470 cM / 2,132 Mb ≈ 0.69 cM/Mb.
-   **Gene & TE annotations:** canonical transcripts of 39,756 protein-coding genes in `Zm-B73-REFERENCE-NAM-5.0_Zm00001eb.1.gff3`[@b73v5]; density in 2,128 1-Mb windows ("tips"/"mid-chromosome" = outer/inner 10% of each chromosome half). Intact TEs (198,875) from `Zm-B73-REFERENCE-GRAMENE-4.0.TEs.1.0.gff3` (2,106 Mb v4)[@b73v4te; @jiao2017]; nested TEs overlap.
-   **Diversity, *θ*~W~, *N*~e~, *B*:** across 904,011,088 callable sites (42% of B73 v5; ≤6 of 25 non-B73 NAM founders missing)[@liu2025]. Fitting *π* = *π*~0~e^−*u*/*r*^ gives *π*~0~ = 0.0189 (single-locus asymptote 0.0212) and mean *B* = 0.74[@liu2025; @finemap]. *θ*~W~ = (51,554,740 / 904,011,088) / *a*~26~ (*a*~26~ = 3.82). *N*~e~ = *π*~0~/4*μ*; equivalent target fraction = *u*/*μ*. Masked regions (56%) are high-recombination and low-constraint, so *π*, *N*~e~ and *u* are probably underestimates.
-   **Demography & census:** ARG *N*~e~ trajectory (Magalang, Fairbanks et al., unpublished) read from a plot (±10–20%)[@peqg2026]; ∼85% bottleneck over ∼2,500 years, ending near the earliest archaeological maize at Xihuatoxtla[@piperno2009]. Census: 47.9M ha of open-pollinated maize × ∼25,000 plants/ha[@beissinger2016].
-   **LTR ages:** *T* = *K*/2*μ* (*K* = 1 − LTR identity; *μ* = 3.3 × 10^−8^/bp/yr[@clark2005]; 128,481 elements[@b73v4te]; median identity 94.9%; 62% < 1 MY). The 85% identity cutoff truncates ages at ∼2.3 MY.

## References

<!-- The numbered reference list is generated here from references.bib; do not edit it by hand. -->
::: {#refs}
:::
:::

<!-- ===================== PAGE 3: worked examples ===================== -->
::: {#p3 .page}
# Worked Fermi Math Examples in Maize Genetics

[Back-of-the-envelope calculations showing how the Top 10 constants and genomic length scales combine to answer practical biological, evolutionary and experimental questions.]{.lede}

::: example
#### 1. How many paired-end short reads are needed for 10× sequencing coverage?

$\frac{10 \times \left( 2 \times 10^{9}\,\text{bp} \right)}{2 \times 150\,\text{bp/pair}} = \frac{2 \times 10^{10}\,\text{bp}}{300\,\text{bp/pair}} \approx$ **7 × 10^7^ read pairs** (70 million pairs)

Only ∼42% of the genome (∼900 Mb) aligns cleanly across assembled NAM genomes; most of the rest is repetitive TE sequence. Expect usable ∼10× depth over roughly that fraction, while reads from high-copy TE families pile up or map ambiguously.
:::

::: example
#### 2. What is the global mutation supply per site each crop generation?

(10^12^ OP plants) × (2 gametes/plant) × (3 × 10^−8^ mutations/bp/gamete) ≈ **6 × 10^4^ transmitted substitutions per site per generation**

This is the expected number of new mutations transmitted at a site in one crop generation, averaged across sites, under the stated census and mutation rate. For adaptation, the useful next calculation is 2*Nμ*~target~ in the population under selection, where *μ*~target~ is the rate to the relevant allele or set of alleles.
:::

::: example
#### 3. How many differences do you expect in a typical gene between two random inbred lines?

(3 × 10^3^ bp gene span) × (*π*~genic~ ≈ 1.2 × 10^−2^) ≈ **36 expected differences per gene**

A rough estimate for a 3 kb gene at the reported genic *π*. The ∼11 differences you would get for the ∼900 bp CDS is an equal-diversity benchmark; for a coding estimate, use CDS-specific *π*. The genic mean is not an upper bound for any individual gene.
:::

::: example
#### 4. How long until recombination splits a 100 kb segment?

*r*~block~ = (0.1 Mb) × (1 cM/Mb) = 0.1 cM = 10^−3^ crossovers/gen → $T \approx \frac{1}{r_{\text{block}}}$ ≈ **1,000 generations**

This is the mean waiting time for a recombination event across 100 kb along one lineage at 1 cM/Mb; at the measured mean of 0.7 cM/Mb it is ∼1,400 generations.
:::

::: example
#### 5. How many new deleterious mutations enter the genome per gamete?

*U*~d~ = (2 × 10^9^ bp) × (3 × 10^−10^ deleterious mutations/bp) ≈ **0.6 deleterious mutations/gamete** under the fitted model

Dividing the modeled deleterious rate by the total substitution rate gives *u*/*μ* ≈ 0.5–1%, an equivalent target size of ∼10–20 Mb under the model. This does not identify a physical set of bases at which every possible substitution is deleterious.
:::

::: example
#### 6. How many crossovers occur in a 100-plant F~2~ mapping population, and how far apart are they?

(100 F~2~ plants) × (2 gametes/plant) × (15 COs/gamete) = 3,000 COs → $\frac{2.13 \times 10^{9}\,\text{bp}}{3{,}000\,\text{COs}}$ ≈ **0.7 Mb between breakpoints**

About 0.7 Mb is the mean physical spacing between pooled crossover breakpoints. Bin size sets the limit on mapping resolution; QTL support intervals from 100 plants are usually far wider.
:::

::: example
#### 7. How big a field plot is needed to grow 10,000 plants for a selection experiment?

$\text{Area} = \frac{10^{4}\,\text{plants}}{3 \times 10^{4}\,\text{plants/ha}}$ ≈ **0.33 hectares** (∼0.8 acres, or a ∼55 m × 60 m plot)

At ∼500 kernels per ear, harvesting the top 1% (100 ears) yields ∼50,000 seeds, more than enough to replant the next cycle at the same population size.
:::
:::
