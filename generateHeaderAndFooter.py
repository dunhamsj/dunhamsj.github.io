#!/usr/bin/env python3

header = \
"""  <head>
    <script>
      /* Button functions taken from:
         https://www.w3schools.com/howto/
         tryit.asp?filename=tryhow_css_dropdown_navbar_click */

      /* When the user clicks on the button, toggle between hiding
         and showing the dropdown content */
      function ToggleMenuOnOff()
      {
        document.getElementById("DropdownMenu").classList.toggle("ShowMenu");
      }

      /* End of button scripts */
    </script>

    <meta charset="UTF-8"/>
    <meta name="description" content="Professional webpage for Samuel
      J. Dunham, astronomy PhD working on 14-moment resistive GRMHD"/>
    <meta name="keywords"
     content="astronomy, astrophysics, astro,
              computational astrophysics, computational astrophysicist,
              supernovae, core-collapse supernovae,
              Sam Dunham, Sam J Dunham, Sam J. Dunham,
              Samuel Dunham, Samuel J Dunham, Samuel J. Dunham,
              Sam Dunham astro, Sam J Dunham astro, Sam J. Dunham astro,
              Samuel Dunham astro, Samuel J Dunham astro,
              Samuel J. Dunham astro,
              sam dunham, sam j dunham, sam j. dunham,
              samuel dunham, samuel j dunham, samuel j. dunham,
              sam dunham astro, sam j dunham astro, sam j. dunham astro,
              samuel dunham astro, samuel j dunham astro,
              samuel j. dunham astro"/>
    <meta name="author" content="Samuel J. Dunham"/>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <meta name="google-site-verification"
      content="2Dwac9idP9vLbFSeAk0kUjXs6IeXM0I0acfLPQOh_IA"/>
    <meta name="robots" content="nofollow"/>

    <title>Samuel J. Dunham</title>
    <link rel="icon" href="Images/Initials.png"/>

    <link rel="stylesheet" href="style.css"/>

  </head>

  <body>

    <!-- Header -->

    <div class="Header">

      <div class="Name">
        Samuel J. Dunham
      </div>

      <div class="Links">
        <a href="./index.html"         class="navlink">About Me</a>
        <a href="./research.html"      class="navlink">Research</a>
        <a href="./presentations.html" class="navlink">Presentations</a>
        <a href="CV_DunhamSamuel.pdf"  class="navlink" target="_blank">CV</a>
      </div>

      <div class="ExternalLinks">
	<li>
	  <a href="https://github.com/dunhamsj/">
	    <img src="Images/GitHub.png" class="rounded-corners"
	     style="width:1.2em;height=1.2em"/></a>&nbsp;
	  <a href="https://www.linkedin.com/in/samueljdunham/">
	    <img src="Images/LinkedIn.png" class="rounded-corners"
	     style="width:1.2em;height=1.2em"/></a>&nbsp;
	  <a href="https://bsky.app/profile/astrodunham.bsky.social">
	    <img src="Images/Bluesky.png" class="rounded-corners"
	     style="width:1.2em;height=1.2em"/></a>&nbsp;
	</li>
      </div>

    </div>

    <!-- End of Header -->
"""

footer = \
"""    <!-- Footer -->

    <div class="footer">
      <div class="Updated">Last updated: October 5, 2024</div>
      <img class="Logo" src="Images/Initials.png"></img>
      <div class="FigAcknowledgements">
      Icons from iconfinder.com | Figures from APOD</div>
    </div>

    <!-- End of Footer -->
"""

fileNames = [ 'index.html', 'research.html', 'presentations.html' ]

for fileName in fileNames:

    with open( fileName, 'r' ) as f:
        data = f.read()
    
    # Header
    n0 = -1
    n1 = -1
    s = ''
    with open( fileName ) as f:
        n = 0
        for line in f.readlines():
            if ( '<head>' in line ) :
                n0 = n
            if ( ( n0 != -1 ) & ( n1 == -1 ) ) :
                s += line
            if ( 'End of Header' in line ) :
                n1 = n
            n += 1
    
    if ( s in data ) :
        d = data.replace( s, header )
    
    # Footer
    n0 = -1
    n1 = -1
    s = ''
    with open( fileName ) as f:
        n = 0
        for line in f.readlines():
            if ( '<!-- Footer -->' in line ) :
                n0 = n
            if ( ( n0 != -1 ) & ( n1 == -1 ) ) :
                s += line
            if ( '<!-- End of Footer -->' in line ) :
                n1 = n
            n += 1
    
    if ( s in data ) :
        dd = d.replace( s, footer )
    
    with open( fileName, 'w' ) as f:
        f.write( dd )
