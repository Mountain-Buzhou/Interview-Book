import argparse
import markdown
import os, os.path
import string, codecs
import re
 
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
        body {margin: 0px;padding: 0px;}
        aside.toc {
            position: absolute;
            top: 0;
            left: 0;
            bottom: 0;
            z-index: 1;
            overflow-y: auto;
            width: 380px;
            color: #364149;
            background: #fafafa;
            border-right: 1px solid 
        }
        main {
            position: absolute;
            top: 0;
            right: 0;
            left: 380px;
            bottom: 0;
            overflow-y: auto;
            color: #000;
            background: #fff;
        }

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
                margin-left: 0;
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
        
        html = htmlTemplate.substitute(asideWidth = args.asideWidth, toc = md.toc, mainContent = mainContent) 

        def replaceMd(val) :
            return 'https://github.com/Liyuk/Interview-Questions-Answers/blob/master' + val.group(0);
        
        def replaceImg(val) : 
            return 'https://raw.githubusercontent.com/Liyuk/Interview-Questions-Answers/master' + val.group(0);

        html = re.sub(r'\/[\/\w]+.md', replaceMd, html)
        html = re.sub(r'\/[\/\w]+.(jpeg|png)', replaceImg, html)

        # outfile = open(fname[:-2]+'html', 'w')
        outfile = open('index.html', 'w')
        outfile.write(html.encode('utf-8'))

        print '>>>>> html factory mission complete!'
         
        infile.close()
        outfile.close()