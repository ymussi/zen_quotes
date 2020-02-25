# zen_quotes

A simple library that returns the Zen of Python quotes.

- Installation

    pip install zen_quotes

- Usage
```

from zen_quotes.quote import Quotes

Quotes().get_quotes() # That will return you all quotes in English.

# Altogether there are 19 quotations, but if you need only one quotation, then pass the quotation position number on the list.

Quotes().get_quotes(quote=2) # this will return you the second quote on the list in English.

Quotes().get_quotes(lang='pt', quote=2) # this will return you the second quote on the list in Portuguese.

```

# TODO

- [] add other languages