Title: A Creative Commons license chooser macro for Pelican blogs 
Tags: open source, hacking
Slug: macro-for-creative-commons-licence-mark
Date: 2014-01-12 21:02:42
Category: Open Dev

As creative expression, blogs and other authored web content qualify for copyright protection. Yet, a number of Pelican (a static site and blog generator) themes, including the default `notmyidea` and [the one I am using](https://github.com/DandyDev/pelican-bootstrap3), do not include configuration variables for displaying copyright, and more importantly, the terms of reuse, i.e., the license. 

Presumably this is not because most blog writers don't expect their content to ever be reused. Of course, it is easy enough to tweak a theme's template(s) to include the author's choice of license. However, every tweak to a theme's templates makes it diverge a little more from its origin, and thus a little more difficult to upgrade it when the theme developer improves it. This is exactly the situation with the `pelican-bootstrap3` theme I am using - it is under active development, including in fact by myself.

## A Creative Commons license chooser as a macro

So I decided to address this in a way that would be reusable by the [Pelican](http://docs.getpelican.com/) community. I'm a big fan of [Creative Commons](http://creativecommons.org) and their legal work to make the world's online content better shareable, and so I wrote a [Jinja2 macro](http://jinja.pocoo.org/docs/templates/#macros) that generates, in a configurable way, a Creative Commons license mark, mirroring the choices that the [Creative Commons license chooser](http://creativecommons.org/choose/) offers, and the HTML markup that it generates. Jinja2 is the templating language that Pelican uses, and so any [Pelican theme](https://github.com/getpelican/pelican-themes) or Pelican-powered blog could take advantage of it. You can see the result at the bottom of this blog.

The code for the macro is on Github: [http://github.com/hlapp/cc-tools](http://github.com/hlapp/cc-tools)

Here are its current capabilities as per its documentation:
```text
{# Choose the license either by name (CC-BY, CC-BY-SA, CC-BY-NC-SA, or      #}
{# CC-BY-NC-ND), or by its features (allow derivatives: Yes, No, ShareAlike;#}
{# allow commercial reuse: Yes, No). Name, if provided, takes precedence,   #}
{# and case is ignored.                                                     #}
{#                                                                          #}
{# Optional:                                                                #}
{#   br_after_icon: if true put a line break after the license icon         #}
{#   attr_markup: if true create markup for fulll attribution               #}
{#   attr_props: if attr_markup, a dict with title, name, and url keys      #}
{#               specifying how under which title, to which creator, and    #}
{#               to which URL to attribute the work                         #}
```

## How does it work?

As an example for how to apply this to a Pelican theme to add a configurable license mark, consider the [change set in the pull request](https://github.com/DandyDev/pelican-bootstrap3/pull/43) that applies it to the `pelican-bootstrap3` theme. Apart from dropping the macro in an appropriate location, and adding configuration documentation to the README, [here is where the macro is called](https://github.com/hlapp/pelican-bootstrap3/blob/acf6a0a1b0efb0ff4c6711cd5b5b6d33c2999bde/templates/includes/footer.html#L14-17):

```html
          {%- if CC_LICENSE or CC_LICENSE_DERIVATIVES or CC_LICENSE_COMMERCIAL %}
              {% from 'includes/cc-license.html' import cc_license_mark %}
              <p><small>{{ cc_license_mark(cc_name=CC_LICENSE,derivatives=CC_LICENSE_DERIVATIVES,commercial=CC_LICENSE_COMMERCIAL,attr_markup=CC_ATTR_MARKUP,attr_props={'title':SITENAME,'name':article.author if article else AUTHOR,'url':SITEURL}) }}</small></p>
          {% endif %}
```   

In `pelicanconf.py`, you can then enable the license mark in two ways. Either you simply set its name, like so:

```python
# Content licensing: CC-BY
CC_LICENSE = "CC-BY"
```

Alternatively, you can specify which features you want the license mark to fulfill:
```python
# Content licensing: permit derivatives, permit commercial use
CC_LICENSE_DERIVATIVES = "yes"
CC_LICENSE_COMMERCIAL = "yes"
```

Optionally, you can ask for full RDFa-compliant markup for the title, author, and source URL with which attribution should be made:

```python
# Include human and machine-readable markup for title (name of the site), 
# author (article author or AUTHOR),  and URL (SITEURL) in license mark
CC_ATTR_MARKUP = true
``` 

## Why not a plugin that uses the CC API?

Good question. For one, I haven't figured out yet how to cast this as a Pelican plugin. The documenation is not very details, and speaks about generators and writers, neither of which strikes me as an immediate fit. If it could be a generator plugin, how would it be invoked? 

Second, sadly the [Creative Commons API](http://api.creativecommons.org/docs/index.html) seems to have been neglected from maintenance. The [1.5 version](http://api.creativecommons.org/docs/readme_15.html) is several years old, and even the "[development](http://api.creativecommons.org/docs/readme_dev.html)" version still returns the 3.0 versions of the licenses. On the flip side, using the API probably wouldn't simplify anything, and instead would require being online when the site is generated.

## Why no public domain ([CC Zero](http://creativecommons.org/about/cc0)) choice?

I haven't gotten to that yet. Most people I know would rather assert copyright [even on content that isn't eligible](http://dx.doi.org/10.6084/m9.figshare.799766), rather than waive it. But [the feature is registered](https://github.com/hlapp/cc-tools/issues/1), and if you know how to add it, please fork the repo and submit a pull request. 

Also, please add issues for any other features you'd like to see.

## And why does a license mark matter?

Many people understand meanwhile that stating a license for software source code is important, because it achieves clarity on the terms of reuse. [Creative Commons explains this](http://wiki.creativecommons.org/Frequently_Asked_Questions) much better, but in a nutshell, the same principle as for source code applies to authored content. As creative expression, copyright vests in its creator whether they assert it or not. A license grants rights that users would otherwise not have, and it is explicit about them.
