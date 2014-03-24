Title: Scientific peer-review as web-annotations: an experiment
Slug: open-peer-review-as-annotations
Tags: open content, scholarly publishing
Category: Lab

Recently I was invited by the journal [F1000 Research] to review an article about [Software Carpentry], a wildly popular programming best-practices teaching workshop. As I sat down to write the review, loathing the highly antiquated and onerous process that peer-review remains to this day, I realized that the publishing model of the journal might just be the perfect prerequisite for trying out an entirely new way of pee-reviewing, namely by annotating online text, using the [Hypothes.is] platform. What follows is an account of what motivated me to experiment with this, and what resulted from it.

## One step in fixing peer-review: open reviews

I have been among those arguing that scientific peer-review is broken, in particular the traditional anonymous closed peer-review model. Peer-reviews in [F1000 Research] are strictly [open and associated with the reviewer's identity](https://f1000research.com/referee-guidelines#key-points) [^1]. Furthermore, the jounal practices post-publication review: It publishes manuscripts online almost immediately (after passing some basic quality checks) upon submission. Peer-reviews, which the journal invites, as done traditionally, from peers in pertinent fields, comment on and issue verdicts on an article's scientific soundness. The reviews then determine whether a major revision is required, and whether the article is indexed for searching by F1000 itself or by other scientific literature search services (such as Pubmed).

This model offered the opportunity to experiment without concern for comments being public or associated with my identity or not.

## Why the peer-review process is still loathsome

As anyone who has ever written or received a scientific peer-review will know, the way this is done, specifically the way we reference, comment, and respond to comments on parts of the text, still follows antiquated procedures from the days of print-only publishing and typewriters. This is the case whether peer-reviews are open or not. Articles are typically sent to reviewers with line and page numbers added to the margins by a publisher's manuscript management system. To comment on specific parts of the text, a reviewer then cites the page and line number, and possibly quotes pieces of text. In an age in which nobody uses typewriters anymore the line numbers and their spacing is often unaligned with the line spacing of the text, some systems reset line numbers on every page, some journals[^2] use 2-column manuscript templates yet number only one column, and some, including in fact F1000 Research, have disposed of line numbers altogether, forcing reviewers to create some numbering of paragraphs or sentences for themselves. Authors, upon receiving the reviews weeks (or months) after submission, the time they last looked at the manuscript, then have to painstakingly link each reviewer comment to the exact position in their editable version of the manuscript (which does not have line numbers, and whose page numbers will differ from the version sent to reviewers due to cover pages etc). The "links" are typically only in the authors' heads; as there is no way to insert clickable hyperlinks from the review comments to the text position or vice versa, associating comments to text being commented on would require painstakingly copy and pasting each one of them into marginal comments (or footnotes, depending on word processor and editor).

The litany doesn't end there. Once a revision of the manuscript is prepared, authors do copy and paste each reviewer comment, this time into a rebuttal letter, and then add their responses to each comment. Formatting choices for distinguishing reviewers' from authors' comments vary wildly. The most diligent authors then also copy and paste the actual verbatim changes to the text they made in response to a reviewer comment; many don't, and many times the changes to the text are extensive and scattered enough to defy even the best intentions. The process then cycles back to the reviewers, who are asked to evaluate whether the author's responses and text changes satisfy their concerns. Precisely because of the revisions to the text, the line and page numbers and quotes of original text that the reviewer used in their original comment to identify the text location are now typically no longer valid or present, so if the author didn't, or couldn't copy and paste their text changes into the rebuttal letter, the reviewer has to then re-identify the text location, an inexact science by definition.

### The cost to knowledge production and consumption

Perhaps most importantly, a reader of the *article* will see none of this. No markers in the article text will highlight which specific claims, data, or method a reviewer has questioned. There is no indication where reviewers agree or disagree in their criticisms. There is no hint which claims were deleted, or restated in a revision, and why; likewise, why some claims were not changed even though a reviewer questioned them is also not immediately visible.

With peer-reviews that are open instead of closed, someone with enough understanding, skill, and time at least *can* extract this information from the peer-reviews and rebuttal letter(s), which is clearly a huge step forward towards research transparency. However, in the digital age there is little justification anymore for erecting (or leaving) a wall between the articles containing our scientific knowledge, and the fine-grained comments experts make on them. And there's also little justification for the peer-review process being as onerous to experts and as inscrutable to non-experts as it is.

## The experiment: review comments as online text annotations

Enter [Hypothes.is]. The project, launched in 2011 through a [Kickstarter campaign] [^3], boldly aims to make the world's online knowledge and information peer-reviewed, by developing [standards](http://www.openannotation.org/spec/core/) and an open-source [platform for online annotation](https://hypothes.is/contribute):

<figure style="max-width: 128px;" class="floatright">
<a href="http://hypothes.is"><img class="img-responsive" src="/images/hypothes.is_logo.jpg"/></a></figure>
> Hypothes.is will be an open platform for the collaborative evaluation of knowledge. It will combine sentence-level critique with community peer-review to provide commentary, references, and insight on top of news, blogs, scientific articles, books, terms of service, ballot initiatives, legislation and regulations, software code and more.

Reviewer comments in scientific peer-review for the most part _are_ annotations. With F1000 Research articles being already fully on the web at the time of review[^4], and my review comments to be openly available and associated with my name by definition, this seemed like a perfect opportunity to try open annotation in Hypothes.is as a scientific peer-review tool that wouldn't suffer from many of the shortcomings outlined above[^other work].

## Results: Lots of potential, lots of ways to go

There are two ways to see the review comments made with Hypothes.is. One is to install the [browser extension] (if you haven't already), navigating to the [article URL], and turning on the extension. At present this unfortunately requires Google Chrome. (The extension is also required for making, or replying to annotations.) The other is the [Hypothes.is "stream" interface][comments URL].

The full review, with overarching comments preceding the link to the detailed annotations, is available form the article's onlne version at F1000 Research. You will notice that the review includes a complete transcript of the online annotations; see below for why.

Some of the lessons learned from the experiment follow.

### What worked (or could have worked) well 

* Even though characterized as "alpha" software, making my comments with the [Hypothes.is Annotator] via direct annotation of an online text as I read through it was far more efficient than making notes with the usual cumbersome way of citing line, page, and paragraph numbers and quoting. Essentially, one highlights the sentence or phrase one wishes to comment on, clicks the [Annotator] icon that appears and enters the comment.

* Comments can be edited or deleted later, such as if later parts of the manuscript put the commented text in a different light. Comments can also be tagged, which could be used to distuingish between major and minor comments (but I didn't).

* An author (or in fact anyone else) could directly respond to the comments, establishing a discussion thread that is directly linked to the part of the text that is its subject. Obviously, this can't be seen yet, and in fact may never be, see below.

### Much room for improvement

1. Although the comments comprising a review can be [retrieved in whole through a URL reference][comments URL], bundling them up in the form needed remains lacking.
    * The Hypothes.is platform doesn't yet have a URL that resolves as the review annotations as a whole, or a single annotation on top of the online text[^Diigo link feature]. This view requires manually [installing a browser extension](http://hypothes.is/alpha), turning it on when on the article page, and activating highlighting mode. 
    * The URL interface that exists for retrieving review comments (the ["stream" interface](http://hypothes.is/stream)) shows them in reverse chronological order (most recent first), and for now there is no option to control the ordering. The awkward consequence of this is that if a reviewer comments on an article from start to end (as would be typical), the author would need to read the comment stream last to first to be consistent with the direction of article and comment flow.
2. Critical kinds of integration with a scientific journal's workflow and requirements remain challenging.
    * As will likely any journal, F1000 Research wants a permanent record of the annotations that comprise a peer-review, and one that can accompany the article's PDF version. There is no direct way to create a PDF yet from Hyppthes.is annotations, leaving print-to-file as the only alternative. But this loses many of the advantages of using online annotation to start with, such as easy pinpointing of text position, establishing a conversation thread, and making the conversation accessible to the public, unless some way is found to keep offline and online versions in syncrony. 
    * Although reviewer comments on F1000 Research do become public, they normally don't do so instantly, but are reviewed for meeting professional standards by F1000 staff first. A journal exercising and enforcing quality control is certainly a Good Thing. The comments I made using Hypothes.is became public immediately[^5], though presumably a journal-hosted version could keep them private until checked and approved.
    * To aid in later retrievability, I added a tag "F1000 Review" to each comment. In this experiment I had to repeat this myself for every comment; ideally, a journal would have set up the [Hypothes.is Annotator] for itself such that comments entered by a reviewer would automatically be tagged uniquely such that they can subsequently be linked to the review and reviewer.

In the concrete case, the deficiencies in fitting with the journal's record keeping and workflow requirements were strong enough that F1000 staff ended up transcribing the comments into an offline text that form the permanent record, and which will thus likely be what the article author ends up responding to (lest they create yet more transcription work for the F1000 staff). So in the end my experiment caused more work rather than less for the journal staff.

### Open questions

Most reviews will include some overarching commentary, often a summary or synthesis of the more detailed comments. If a reviewer recommends rejection (or in the case of F1000 Research, [withholds "approval"](https://f1000research.com/referee-guidelines#your-role)), the most serious concerns about the work will usually be highlighted there. It's unclear to me whether that part fits the mold of a text annotation equally well; it really applies to the article as a whole than some part of the text.

In my case, I entered the overarching commentary into the review submission form. However, a solution that is better integrated with online annotation might have a more seamless way of providing, and showing them at the article level. 

## Conclusions

Given how antiquated, inefficient, and wholly unnecessary the current way of conducting peer-reviews is in the digital age, it's hard to imagine that this isn't on the verge of being innovated. I think the shift in ecosystem and economic driving forces in scholarly publishing are providing the perfect fertile ground. A journal's subject area is becoming increasingly less critical as a sustaining market niche; instead, the emerging category of "mega-journals" pioneered by [PLoS ONE](http://plosone.org) will increasingly compete on the basis of customer service and maximizing the impact of their publications (and thus contributions to their quality). I'm willing to bet that this will soon include overhauls of the peer-review process.

I hope that online annotation platforms and standards will figure prominently in this transformation, so that peer-review commentary, and the scholars who make them, can become a seamless part of the web's discussion layer. However, the experiment also shows that integration of online annotation tools, as sophisticated and promising as they are, has still a long ways to go. Making this happen will take journals and publishers assuming ownership of it.

Finally, as excited as I have been about [Hypothes.is] ever since it appeared on the scene, as an ambition, as a community nurturing initiave, and as an actual software project, my sense is that it would benefit well from pushing itself more from aspiration towards actual production uses. The browser extension is still only available for Chrome (and in fact not even advertised on the front page). The stream interface is unadvertised and misses basic features (including an ability as fundamental to the ideas as responding to an annotation). Perhaps scholarly publishing is only a small pond in the greater picture. But at a time when scandals of scientific fraud, data fabrication, and lack of repeatibility shake the public's trust in science more than ever, creating an online conversation around scientific critique, in particular with a platform that is designed open throughout, would seem as an opportunity with potential benefits for everyone.

[F1000 Research]: http://f1000research.com/
[Software Carpentry]: http://software-carpentry.org
[Hypothes.is]: http://hypothes.is
[Hypothes.is Annotator]: https://hypothes.is/what-is-it
[Annotator]: http://annotatorjs.org/
[browser extension]: http://hypothes.is/alpha
[Kickstarter Campaign]: https://www.kickstarter.com/projects/dwhly/hypothesis-taking-peer-review-to-the-internet
[article URL]: http://f1000research.com/articles/3-62/v1
[comments URL]: https://hypothes.is/stream#?user=hlapp&uri=http:%2F%2Ff1000research.com%2Farticles%2F3-62%2Fv1

[^1]: Unlike closed anonymous reviews, this allows a scholar to receive credit for the reviews she writes. It could also be used to "rate" the quality of reviews (as perhaps measured by depth, constructiveness, etc), which would provide more direct incentives for more in-depth reviews. But F1000 Research doesn't seem to be using it for this purpose (yet?); arguably, doing so is also fraught with problems (how to measure review quality? who should do the rating? how to prevent review rating from biasing reviewers towards positivity? etc).

[^2]: Bioinformatics (OUP), I am looking at you.

[^3]: Disclosures: I was one of the campaign's backers. I was also chair of the organizing committee that invited Dan Whaley (founder of Hypothes.is) to present [one of the 2012 iEvoBio Conference keynote addresses](https://www.youtube.com/watch?v=cNrAS979MfA) (which is well worth watching, BTW. And yes, that's me introducing him, and yes, I'm wearing a Hypothes.is t-shirt.).

[^4]: This is more novel than one might think. For journals that publish articles only post-acceptance (as almost all do) manuscripts can take a significant amount of time after acceptance -- sometimes weeks, or months -- before they appear online. Some publishers have introduced "early online access" sections for their journals; manuscripts in those sections are typically only available in the form of "preliminary" PDFs, not in HTML. Most online annotation platforms don't, or don't yet work on PDFs, and the preliminary PDFs are expressly intended to be superseded by the final typeset version, rather than to have a persistent presence. 

[^other work]: I am of course far from the first one to think about open online annotation and Hypothes.is for scientific peer-review. Peter Brantley, Hypothes.is' Director of Scholarly Communication, in his [interview for The Scholarly Kitchen](http://scholarlykitchen.sspnet.org/2013/10/09/scholarly-kitchen-podcast-peter-brantley-on-annotating-the-web/) speaks specifically about the possibility of utilizing open annotation for scientific peer-review, and there's a [post on Researchity](http://researchity.net/2011/11/01/peer-review-should-be-more-like-hypothes-is-than-hypothes-is-should-be-like-peer-review/) from the time of the Kickstarter campaign, to name a few.

[^5]: I realized only after the fact that this is a difference to how comments would have become public if submitted solely through the journal's review submission form. However, F1000 Research's reviewer guidelines didn't prohibit (or even mention) the use of external online annotation tools; perhaps this is something that journals innovating scholarly peer-review should be more cognizant, and explicit about.

[^Diigo link feature]: [Diigo](http://www.diigo.com), an online bookmarking and annotation service, does allow to provide a link to the annotated version of an online page. For example, this is an [article with highlights I made](https://diigo.com/01j2ng) for a journal club. It works well in Chrome and Firefox but only if the respective browser extension is installed. Diigo is a pretty mature product that I use frequently and could have used for this experiment as well; however, it is commercial and not an open-source platform, whereas Hypothes.is could be adapted, contributed to, extended, and deployed by anyone.
