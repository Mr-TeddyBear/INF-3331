import re

def parse_nwodkram(text):
    """
    Parser for nwodkram to HTML

    Accepts raw string in nwodkran and returns raw string in HTML
    """
    def https_sub(m):
        if m[2].startswith("https:/") or m[2].startswith("http:/"):
            return r'<a href="{}">{}</a>'.format(m[2],m[1])
        else:
            return r'<a href="{}">{}</a>'.format("http://"+m[2],m[1])


    regex_italic = r"(?<!\\)\*(.*?)(?<!\\)\*"
    regex_bold = r"(?<!\\)%(.*?)(?<!\\)%"
    regex_hyplnk = r"\[([\w\s]+)\]\((\S+)\)"
    regex_picture = r"\<([\w\s\:/\.-]+)\>\(w=(\d)+,h=(\d+)\)"
    regex_quote = r'^\>\>(.+)'
    regex_wiki = r'\[wp:([.\S]*)\]'
    regex_remove = r'\\([\*%])'


    HTML =  re.sub(regex_italic, r"<i>\1<i>" ,text)
    HTML = re.sub(regex_bold, r"<b>\1<b>", HTML)
#    HTML = re.sub(regex_hyplnk, "<a href=\"\\2\">\\1</a>", HTML)
    HTML = re.sub(regex_hyplnk, https_sub, HTML)
    HTML = re.sub(regex_picture, r'<img src="\1" width="\2" heigth="\3">',HTML)
    HTML = re.sub(regex_quote,r'<blockquote>\1</blockquote>', HTML, flags=re.MULTILINE)
    HTML = re.sub(regex_wiki, r'<a href="https://en.wikipedia.org/w/index.php?title=Special:Search&search=\1">',HTML)
    HTML = re.sub(regex_remove,r'\1', HTML)
    return (HTML)



if __name__ == "__main__":
    sample_input = r"""
    %Lorem% ipsum *dolor sit amet*, consectetur *adipiscing elit. Nullam tempor* nunc at justo tincidunt congue. %Aliquam hendrerit mollis pretium! Praesent id% mi est. [Praesent,](www.praesent.com) sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

    >>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla *eget eros euismod volutpat. Suspendisse* id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat %molestie \*libero vel\%\% pulvinar? Sed% a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.

    Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in \%% urna. \% Fusce% in *sapien %mau\*ris.% Duis purus dui*, viverra in tellus eu, imperdiet fringilla [felis. Curabitur rhoncus tincidunt varius. Cras](inf3331.no) gravida metus ut [wp:vestibulum] vestibulum. \*Integer cursus* ex\* in rutrum volutpat*. Nunc scelerisque gravida risus sed ullamcorper. Proin [lorem,](https://www.malesuada.com) massa <https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif>(w=100,h=40) quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio *bibendum.*
    """
    print (parse_nwodkram(sample_input))
