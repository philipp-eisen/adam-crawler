#ADAM-Crawler

This small scrapy spider crawls the The A.D.A.M. Medical Encyclopedia which can be found here: https://www.nlm.nih.gov/medlineplus/encyclopedia.html .

This script ignores `patientinstructions`.

The output will be a JSON Array of JSON Objects in the following format:

```
[
{"Title":"<the title>",
"URL":"<the url of the article>",
"<section name>":"<section text>",

...

}

...

]
```

##How tu run:

first install requirements:
`pip install -r requirements.txt`

run scrapy spider:
`scrapy runspider adamcrawler/adam_spider.py -o adam-articles.json`
