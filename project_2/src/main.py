from grammar.cfg import CFG

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cfg = CFG(
    #     variables={'S', 'A', 'B'},
    #     terminals={'a', 'b'},
    #     productions={
    #         ('S', ('A', 'S', 'A')),
    #         ('S', ('a', 'B')),
    #         ('A', ('B', 'b')),
    #         ('B', ('b',)),
    #         ('B', ('',)),
    #     },
    #     start_symbol='S'
    # )
    cfg = CFG(
        variables={'S', 'A', 'B'},
        terminals={'a', 'b'},
        productions={
            ('S', ('a',)),
            ('S', ('A', 'B')),
            ('A', ('b',))
        },
        start_symbol='S'
    )
    cfg.accept(())
    print(cfg)
    # g1 = CFG(
    #     variables={'F', 'O', 'A', 'N'},
    #     terminals={'->', '/\\', '\\/', '!', '(', ')', 'p', 'q', 'r'},
    #     productions={
    #         ('F', ('O', '->', 'F')),
    #         ('F', ('O',)),
    #         ('O', ('O', '\\/', 'A')),
    #         ('O', ('A',)),
    #         ('A', ('A', '/\\', 'N')),
    #         ('A', ('N',)),
    #         ('N', ('!', 'N')),
    #         ('N', ('(', 'F', ')')),
    #         ('N', ('p',)),
    #         ('N', ('q',)),
    #         ('N', ('r',))
    #     },
    #     start_symbol='F'
    # )
    # print(g1.accept(string=('J', 'a', 'i', 'r', 'o')))
    #
    # g2 = CFG(
    #     variables={'D', 'H', 'I', 'L', 'M', 'O', 'T'},
    #     terminals={
    #         '<html>', '</html>', '<head>', '</head>', '<title>', '</title>', '<body>',
    #         '</body>', '<b>', '</b>', '<ul>', '</ul>', '<ol>', '</ol>', '<li>', '</li>',
    #         'theory of computation', 'automata', ' ', 'grammars'},
    #     productions={
    #         ('D', ('<html>', '<head>', '<title>', 'T', '</title>', '</head>', '<body>', 'H',
    #                '</body>', '</html>')),
    #         ('H', ('I', 'H')),
    #         ('H', ('I',)),
    #         ('I', ('<b>', 'H', '</b>')),
    #         ('I', ('T',)),
    #         ('I', ('L',)),
    #         ('L', ('<ul>', 'M', '</ul>')),
    #         ('L', ('<ol>', 'M', '</ol>')),
    #         ('M', ('M', 'O')),
    #         ('M', ('O',)),
    #         ('O', ('<li>', 'H', '</li>')),
    #         ('T', ('theory of computation',)),
    #         ('T', (' ',)),
    #         ('T', ('automata',)),
    #         ('T', ('grammars',))
    #     },
    #     start_symbol='D'
    # )
    # print(g2.accept(string=('J', 'a', 'i', 'r', 'o')))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
