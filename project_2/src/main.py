from grammar.cfg import CFG

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    g1 = CFG(
        variables={'F', 'O', 'A', 'N'},
        terminals={'->', '/\\', '\\/', '!', '(', ')', 'p', 'q', 'r'},
        productions={
            ('F', ('O', '->', 'F')),
            ('F', ('O',)),
            ('O', ('O', '\\/', 'A')),
            ('O', ('A',)),
            ('A', ('A', '/\\', 'N')),
            ('A', ('N',)),
            ('N', ('!', 'N')),
            ('N', ('(', 'F', ')')),
            ('N', ('p',)),
            ('N', ('q',)),
            ('N', ('r',))
        },
        start_symbol='F'
    )
    g1 = g1.normalize()
    print(g1.accept(string=('p', '/\\', '!', 'r', '\\/', 'q', '->', '!', '!')))
    print(g1.accept(string=('p', '/\\', '!', 'r', '\\/', 'q', '->', '!', 'q')))

    g2 = CFG(
        variables={'D', 'H', 'I', 'L', 'M', 'O', 'T'},
        terminals={
            '<html>', '</html>', '<head>', '</head>', '<title>', '</title>', '<body>',
            '</body>', '<b>', '</b>', '<ul>', '</ul>', '<ol>', '</ol>', '<li>', '</li>',
            'theory of computation', 'automata', ' ', 'grammars'},
        productions={
            ('D', ('<html>', '<head>', '<title>', 'T', '</title>', '</head>', '<body>', 'H',
                   '</body>', '</html>')),
            ('H', ('I', 'H')),
            ('H', ('I',)),
            ('I', ('<b>', 'H', '</b>')),
            ('I', ('T',)),
            ('I', ('L',)),
            ('L', ('<ul>', 'M', '</ul>')),
            ('L', ('<ol>', 'M', '</ol>')),
            ('M', ('M', 'O')),
            ('M', ('O',)),
            ('O', ('<li>', 'H', '</li>')),
            ('T', ('theory of computation',)),
            ('T', (' ',)),
            ('T', ('automata',)),
            ('T', ('grammars',))
        },
        start_symbol='D'
    )
    g2 = g2.normalize()
    print(g2.accept(string=(
        '<html>',
        '<head>',
        '<title>',
        'theory of computation',
        '</title>',
        '</head>',
        '<body>',
        'automata',
        '<b>',
        '<ul>',
        '<li>',
        'automata',
        '</li>',
        '<li>',
        '<ol>',
        '<li>', '<b>', ' ', '</b>', '</li>',
        '</ol>',
        '</li>',
        '<li>',
        '<b>', 'theory of computation', '</b>',
        '</li>',
        '</ul>',
        '</b>',
        'grammars',
        '</body>',
        '</html>',
    )))
    print(g2.accept(string=(
        '<html>',
        '<head>',
        '<title>',
        'theory of computation',
        '</title>',
        '</head>',
        '<body>',
        'automata',
        '<b>', '</b>',  # generate error
        '<ul>',
        '<li>',
        'automata',
        '</li>',
        '<li>',
        '<ol>',
        '<li>', '<b>', ' ', '</b>', '</li>',
        '</ol>',
        '</li>',
        '<li>',
        '<b>', 'theory of computation', '</b>',
        '</li>',
        '</ul>',
        '</b>',
        'grammars',
        '</body>',
        '</html>',
    )))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
