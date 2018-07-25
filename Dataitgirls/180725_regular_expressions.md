```
Match	abcdefg
Match	abcde
Match	abc
```
\>> \\w+
```
Match	abc123xyzabc12
Match	define "123"
Match	var g = 123;
```
\>> .+
```
Match	cat.
Match	896.
Match	?=+.
Skip	abc1
```
\>> .+\\.
\>> \\.$
```
Match	can
Match	man
Match	fan
Skip	dan
Skip	ran
Skip	pan
```
\>> [cmf]an
\>> ^[cmf]
```
Match	hog
Match	dog
Skip	bog
```
\>> [d-h]og
\>> ^[d-h]
```
Match	Ana
Match	Bob
Match	cpc
Skip	aax
Skip	bby
Skip	ccz
```
\>> [A-C]\w{2}
\>> ^[A-C]
```
Match	wazzzzzup
Match	wasssup
Skip	wazup
```
\>>  wazz+up
\>> zz+
```
Match	aaaabcc
Match	aabbbbc
Match	aacc
Skip	a
```
\>> aa+b*c+
\>> aa+
```
Match	1 file found?1 fil
Match	2 files found?
Match	24 files found?
Skip	No files found.
```
\>> \d\d?\sfiles?\sfound?
\>> ^\d
```
Match	1.   abc
Match	2.	abc
Match	3.           abc
Skip	4.abc
```
\>> \\d\\.\\s+abc
\>> ^(\\d\\.\\s)
```
Match	Mission: successful
Skip	Last Mission: unsuccessful
Skip	Next Mission: successful upon capture of target
```
\>> ^Mission: successful
\>> ^M
```
Capture	file_record_transcript.pdf
Capture	file_07241999.pdf
Skip	testfile_fake.pdf.tmp
```
\>> ^(file_\\w+)\\.pdf$
\>> ^(file_\w+)
```
Capture	Jan 1987
Capture	May 1969
Capture	Aug 2011
```
\>> ^(([A-Z]\\D{2})\\s(\\d{4}))$
\>> ([A-Z]\\D{2}\\s(\\d{4}))
```
Capture	1280x720
Capture	1920x1600
Capture	1024x768
```
\>> (\\d{4})x(\\d\\d\\d\\d?)
\>> (\\d{4})x(\\d{3}\\d?)
```
Match	I love cats
Match	I love dogs
Skip	I love logs
Skip	I love cogs
```
\>> I\\slove\\s(cat|dog)s$
\>> cat|dog
```
Match	The quick brown fox jumps over the lazy dog.
Match	There were 614 instances of students getting 90.0% or above.
Match	The FCC had to censor the network for saying &$#*@!.
```
\>> \\bThe(re)?\\s(\\w+\\s)+\\.+?\\.$
\>> ^The(re)?
```
Match	3.14529
Match	-255.34
Match	128
Match	1.9e10
Match	123,340.00
Skip	720p
```
\>> -?\\d+[\\.,]?\\d+[\\.e]?\\d+$
\>> \\d$
```
Capture	415-555-1234	415	To be completed
Capture	650-555-2345	650	To be completed
Capture	(416)555-3456	416	To be completed
Capture	202 555 4567	202	To be completed
Capture	4035555678	403	To be completed
Capture	1 416 555 9292
```
\>> 1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}
\>> 1?\(?(\d{3})\)?
```
Capture	tom@hogwarts.com
Capture	tom.riddle@hogwarts.com
Capture	tom.riddle+regexone@hogwarts.com
Capture	tom@hogwarts.eu.com
Capture	potter@hogwarts.com
Capture	harry@hogwarts.com
Capture	hermione+regexone@hogwarts.com
```
\>> ([a-z]{3,8}(\.riddle)?)(\+regexone)?@hogwarts\.(eu\.)?com
\>> ([a-z]+(\.riddle)?)(\+regexone)?
```
Capture	<a>This is a link</a>
Capture	<a href='https://regexone.com'>Link</a>
Capture	<div class='test_style'>Test</div>
Capture	<div>Hello <span>world</span></div>
```
\>> ^<(a|div)>?
\>> ^<(a|div)
```
Skip	.bash_profile
Skip	workspace.doc
Capture	img0912.jpg
Capture	updated_img0912.png
Skip	documentation.html
Capture	favicon.gif
Skip	img0912.jpg.tmp
Skip	access.lock
```
\>> (^[a-z]+(_img|\.)?(\d{4})?)\.(jpg|png|gif)$
\>> ^(\w+)\.(jpg|png|gif)$
```
Capture				The quick brown fox...
Capture	   jumps over the lazy dog.
```
\>> \s+((\w{3,}\s)+\w{3}(\.\.)?\.$)
\>> ((\w+\s)+\w+(\.{2})?\.)
```
Skip	W/dalvikvm( 1553): threadid=1: uncaught exception
Skip	E/( 1553): FATAL EXCEPTION: main
Skip	E/( 1553): java.lang.StringIndexOutOfBoundsException
Capture	E/( 1553):   at widget.List.makeView(ListView.java:1727)
Capture	E/( 1553):   at widget.List.fillDown(ListView.java:652)
Capture	E/( 1553):   at widget.List.fillFrom(ListView.java:709)
```
\>> E/\(\s1553\):\s\s\sat\swidget\.List\.(makeView|fillDown|fillFrom)\((ListView\.java):(\d{3,4})\)
\>> (makeView|fillDown|fillFrom)\((ListView\.java):(\d{3}\d?)
```
Capture	ftp://file_server.com:21/top_secret/life_changing_plans.pdf
Capture	https://regexone.com/lesson/introduction#section
Capture	file://localhost:4040/zip_file
Capture	https://s3cur3-server.com:9999/
Capture	market://search/angry%20birds
```
\>> ^(ftp|https|file|market)://(\w+(-\w+)?(\.com)?):?((\d{2})?(\d{2})?)
\>> (ftp|https|file|market)://(\w+[-\.]?(\w+)?\.?(\w+)?):?(\d{2,4})?