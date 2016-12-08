# Straighten-Quotes

## Usage
Some word processors or text editors will automatically replace some typed characters with more attractive or typologically-correct versions, such as "smart quotes" or dedicated ellipses characters. This behavior can make it difficult to copy text into code documents.

This package addresses this issue. Envoking "Straighten Quotes" in the **Edit** menuwill replace directional quotes (a.k.a. "smart quotes"), ellipses characters, and em- and en-dashes with their code-friendly counterparts.

The full set of character replacements is:

	“ : "   #start quote
	” : "   #end quote
	… : ... #ellipses
	– : --  #en-dash
	— : --- #em-dash

## Installation
1. Open **Sublime Text > Preferences > Browse Packages...**
2. Navigate one directory upward to find the "Installed Packages" directory
3. Copy *Straighten Quotes.sublime-package* into "Installed Packages" and restart Sublime