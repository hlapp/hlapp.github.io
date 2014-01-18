Title: Data flirting, or an attempt to save a beautiful tree? 
Tags: data sharing, data reuse
Slug: data-flirting-or-saving-beautiful-tree
Category: Lab

Recently, [TreeBASE](http://treebase.org "TreeBASE") received the following request.

> Hello!
>
> I am just beginning to compile a submission.
>
> The data-matrix is no problem. But in your introductory screens I see nothing explicit about the file format to be used for trees. By implication, these too should be in Nexus format, whereas I would prefer to submit tiff files of the actual published figures.
>
> Please advise.

If you care about preservation, sharing, and reusability of phylogenetic data as much as I do, your first reaction might be that combination of annoyance and incredulity we typically refer to by three capital letters. And never mind that the [submission instructions](http://treebase.org/treebase-web/submitTutorial.html) say _"Data are uploaded to TreeBASE in the NEXUS format"_. 

But upon closer inspection, as much as it appears like a case of data flirting[^1], it might just be a case of someone trying to save a beautiful tree. As Rob Guralnick, Mark Westneat, and I [wrote in a submission to the 2012 iEvoBio Conference](http://dx.doi.org/10.7287/peerj.preprints.206v1)[^2]:

> The story of biological evolution is highly complex and the subject of an enduring quest for better understanding. Yet it is also one of remarkable beauty, as given testimony by the numerous phylogenetic illustrations in publications that show in fascinating detail how traits, function, or morphology may have evolved along a tree. [Almost] all of them end up buried in articles, undiscoverable on their own, locked away behind paywalls, copyrighted by the publisher rather than the creator, and unavailable for repurposing.

<figure style="max-width: 380px;" class="floatright">
<a href="http://www.pnas.org/content/108/14/5690/F1.expansion.html"><img class="img-responsive" src="/images/Wiegmann_et_al_Figure1.png"/></a><figcaption>
Phylogenetic tree for Diptera. Reproduced from Figure 1 in Wiegmann BM et al. (2011) <a href="http://dx.doi.org/10.1073/pnas.1012675108" target="_blank">Episodic radiations in the fly tree of life</a>. Proc Natl Acad Sci U S A 108: 5690–5695.
</figcaption></figure>
Phylogenetic tree illustrations, such as the one to the right, can be rich in information much beyond the topology. Today, no good format exists for archiving this information, let alone in a machine-interpretable form[^3], other than archiving the image and archiving the accompanying (natural language) arcticle text. Text-based and thus machine-readable phylogenetic data formats such as [NeXML](http://nexml.org)[^4], NEXUS[^5], and [Newick](http://en.wikipedia.org/wiki/Newick_format), to different degrees allow one to store metadata about elements of a tree right along with the tree, but at present even NeXML doesn't even come close[^4] to cover the whole breadth of visual adornments that authors might use to convey information. Hence, If one were to archive only the machine-readable version of a phylogeny, phylogenetic knowledge near and dear to an author's heart may easily be lost.

So why not archive both? Unfortunately, TreeBASE will not take an image of a tree, only a (text-based) NEXUS file. Or fortunately, depending on your perspective. At least it ensures that the phylogenies it holds are available in machine-readable form. The digital data archive [Dryad](http://datadryad.org) shows that this otherwise isn't to be taken for granted. Although it gives [some general guidelines](http://datadryad.org/pages/faq#depositing-acceptable-data), due to its broad disciplinary scope Dryad does not and arguably cannot impose strict requirements on the format of deposited data. This gives authors of published papers the flexibility to archive any kind of data they deem supporting the article or otherwise worth preserving. On the flip side this flexibility then doesn't prevent records which include a phylogeny _only_ in image format. And looking at some examples ([here](http://dx.doi.org/10.5061/dryad.vp634306) and [here](http://datadryad.org/resource/doi:10.5061/dryad.3mt58823)), these don't even look like containing information in visual form that would be difficult or impossible to include in a text format.

Even a phylogeny that is archived in machine-readable format is not necessarily fit for a purpose that would require machine readability[^6]. In response to the difficulties the Open Tree has encountered[^7] in synthesizing a Tree of Life from all published trees, investigators from this and other large-scale phylogenetic knowledge synthesis projects are now drafting guidelines for how to archive a phylogeny so it can best be built upon by others in the future. [Public comment and input is welcome](https://docs.google.com/document/d/1rDHUQYBM079w0v8xpWw2t292m2N3FeaaZucEsWAywYI/edit#), and will likely become part of phylogenetic data sharing mandates that NSF [appears determined to include in funding opportunities](http://blog.opentreeoflife.org/2014/01/15/data-sharing-opentree-and-golife/)[^8].

[^1]: To my knowledge, the term _data flirting_ was coined by [Carole Goble](http://en.wikipedia.org/wiki/Carole_Goble), although it seems difficult to find a direct citation. I first heard her use it during [her keynote at ISMB 2013](http://www.iscb.org/ismbeccb2013-program/ismbeccb2013-keynotes/ismbeccb2013-carolegoble), and it caught on instantly with the audience. The following is the best mention I could find on the interwebs, giving meaning _and_ context: <blockquote class="twitter-tweet" lang="en"><p>&quot;Papers are data flirting exercises&quot;, says .<a href="https://twitter.com/CaroleAnneGoble">@CaroleAnneGoble</a> - show some metadata to make people want the real thing. <a href="https://twitter.com/search?q=%23ismbeccb&amp;src=hash">#ismbeccb</a> <a href="https://twitter.com/search?q=%23openscience&amp;src=hash">#openscience</a></p>&mdash; Daniel Mietchen (@EvoMRI) <a href="https://twitter.com/EvoMRI/statuses/359578812226347008">July 23, 2013</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

    Here I'm extending the meaning of _data flirting_ to include _"show some non-reusable form of the data so I want to ask you for the real thing"_. 

[^2]: [Slides for the presented talk](http://www.slideshare.net/hlapp/liberating-our-beautiful-trees-a-call-to-arms) are on Slideshare. Interestingly, although it is a purely aspirational talk, in the sense that there is no active project or community initiative behind it (yet?), it is my second-most viewed slideshow on Slideshare. Perhaps it's the title that gets people to click on it accidentally? 

[^3]: Efforts to address this have emerged. The Phylotastic II hackathon by NESCent's [Hackathons, Interoperabiliy, Phylogenetics](http://www.evoio.org/wiki/HIP) (HIP) Working Group gave rise to a subgroup named [PhyloStyloTastic](http://www.evoio.org/wiki/.TSS_and_extended_NeXML) aiming to create a CSS-like standard for "styled" phylogenies. [jsPhyloSVG](http://www.jsphylosvg.com/) is a JavaScript library that renders [phyloXML](http://www.phyloxml.org/)-formatted phylogenies with graphical adornment markup.

    See also this publication: Smits SA., Ouverney CC (2010) [jsPhyloSVG: A Javascript Library for Visualizing Interactive and Vector-Based Phylogenetic Trees on the Web](](http://dx.doi.org/10.1371/journal.pone.0012267)). PLoS ONE 5: e12267.

[^4]: Vos RA, Balhoff JP, Caravas JA, Holder MT, Lapp H, et al. (2012) [NeXML: rich, extensible, and verifiable representation of comparative data and metadata](http://dx.doi.org/10.1093/sysbio/sys025). Syst Biol 61: 675–689.

    One of the novelties of NeXML is that allows arbitrary (RDFa-style) metadata annotation of any element of a phylogeny. In principle, this could include stylistic or graphical markup, but a convention or standard for such a markup annotation does not exist yet, let alone software that would interpret it.

[^5]: Maddison D, Swofford D, Maddison W (1997) [NEXUS: an extensible file format for systematic information](http://www.ncbi.nlm.nih.gov/pubmed/11975335). Syst Biol 46: 590–621.

[^6]: [This abstract](http://dx.doi.org/10.6084/m9.figshare.902865), and the [slides](http://www.slideshare.net/hlapp/miapa-i-evobio-2013), for a lightning talk I and a group of collaborators presented at the 2013 iEvoBio Conference give some high-level background. See also this paper: Leebens-Mack J, Vision T, Brenner E, Bowers JE, Cannon S, et al. (2006) [Taking the first steps towards a standard for reporting on phylogenies: Minimum Information About a Phylogenetic Analysis (MIAPA)](http://dx.doi.org/10.1089/omi.2006.10.231). OMICS 10: 231–237.

[^7]: Drew BT, Gazis R, Cabezas P, Swithers KS, Deng J, et al. (2013) [Lost Branches on the Tree of Life](http://dx.doi.org/10.1371/journal.pbio.1001636). PLoS Biol 11: e1001636.

[^8]: Instead of the typically vague and generic statements found in past NSF program solicitations, recent ones have become increasingly specific (e.g., see the  [2014 Dimensions of Biodiversity](http://www.nsf.gov/pubs/2014/nsf14525/nsf14525.htm) solicitation). Why these are problematic deserves its own discussion. I'll update this footnote with a link once that post is up.
