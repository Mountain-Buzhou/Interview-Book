import argparse
import markdown
import os, os.path
import string, codecs
 
parser = argparse.ArgumentParser(add_help=True)
 
parser.add_argument('files', metavar='mdFile', type=str, nargs='+', 
    help='md files to be converted')
                    
parser.add_argument('--aside-width', dest='asideWidth',type= int, 
    default=20, help='the width of the aside toc, specified as percents. e.g., 15 means 15 percents')
                    
parser.add_argument('--no-number', dest='noNumber',action='store_true', 
    default=False, help='do not prepend numbers for headers')                    
 
args = parser.parse_args()
 
htmlTemplate = string.Template('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Interview Questions & Answers</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="assets/css/modest.css">
        <style>
            html, body {width: 100%}
            body {margin: 0px;}
            aside.toc { position:fixed; top:0px; left: 0px; width: ${asideWidth}%; border-right: 2px solid grey; overflow: scroll}
            main { position: relative; width: ${mainWidth}%; left: ${asideWidth2}%; margin-left: 25px; }

            .markdown-body {
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 0 auto;
                padding: 30px;
            }
        
            @media (max-width: 767px) {
                .markdown-body {
                    padding: 15px;
                }
                aside.toc {
                    display: none;
                }
                main {
                    left: 0;
                }
            }
        </style> 
    </head>
    <body>
    <aside class="toc markdown-body">$toc</aside>
    <main>
        <article class="markdown-body">
            $mainContent
        </article>
    </main>
    <script>
        var tocElem = document.querySelector("aside.toc");
        tocElem.style.setProperty("height", window.innerHeight+'px');
        
        window.addEventListener("resize", resizeThrottler, false);
        
        var resizeTimeout;
        function resizeThrottler() {
            // ignore resize events as long as an actualResizeHandler execution is in the queue
            if (!resizeTimeout) {
                resizeTimeout = setTimeout(function() {
                    resizeTimeout = null;
                    actualResizeHandler();
                }, 300);
            }
        }
    
        function actualResizeHandler() {
            tocElem.style.setProperty("height", window.innerHeight+'px');
        }
    </script>
    <body>
''')

if (args.files[0] == '*'):
    files = filter(os.path.isfile, os.listdir(os.getcwd()))
    files = filter(lambda x: x.endswith('.md'), files)
else:
    files = filter(lambda x: x.endswith('.md'), args.files)
     
md = markdown.Markdown(extensions=['markdown.extensions.toc'], output_format="html5") 

if not files:
    print 'Error: File not found!'
else:
    for fname in files:
        # md.convert() accepts only unicode
        infile = codecs.open(fname, mode="r", encoding="utf-8")
        mdtext =infile.read()
         
        # use convert() instead of convertFile() as convertFile() output the result to either a file or stdout.
        mainContent = md.reset().convert(mdtext)
     
        # warning: there should not be a marker such as [TOC] for toc in the converted .md file, 
        # or else md would not have attribute toc
        # 100-3 : 3 percent for margin 
        
        html = htmlTemplate.substitute(asideWidth = args.asideWidth, asideWidth2 = args.asideWidth + 5, mainWidth = 100,
            toc= md.toc, mainContent=mainContent) 
     
        outfile = open(fname[:-2]+'html', 'w')
        outfile.write(html.encode('utf-8'))
         
        infile.close()
        outfile.close()